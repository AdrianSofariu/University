// src/main/java/dao/GameDAO.java
package dao;

import models.Game;
import models.Ship;
import models.Shot;
import models.User;
import dbconnection.DBConnection;
import exceptions.DataAccessException;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class GameDAO {

    // --- Game Management ---

    // Retrieves the single active game that is not yet completed.
    public Game getActiveGame() {
        Game game = null;
        String sql = "SELECT id, player1_id, player2_id, status, current_turn_player_id, winner_id FROM games WHERE status NOT IN ('PLAYER1_WON', 'PLAYER2_WON') LIMIT 1";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    game = new Game();
                    game.setId(rs.getInt("id"));
                    game.setPlayer1Id((Integer) rs.getObject("player1_id"));
                    game.setPlayer2Id((Integer) rs.getObject("player2_id"));
                    game.setStatus(rs.getString("status"));
                    game.setCurrentTurnPlayerId((Integer) rs.getObject("current_turn_player_id"));
                    game.setWinnerId((Integer) rs.getObject("winner_id"));
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException("Failed to get active game.", e);
        }
        return game;
    }

    public Game getGameById(int gameId) throws DataAccessException {
        String sql = "SELECT id, player1_id, player2_id, status, current_turn_player_id, winner_id FROM games WHERE id = ?";
        Game game = null;
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setInt(1, gameId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    game = new Game();
                    game.setId(rs.getInt("id"));
                    // Use rs.getObject and cast to Integer for nullable columns
                    game.setPlayer1Id((Integer) rs.getObject("player1_id"));
                    game.setPlayer2Id((Integer) rs.getObject("player2_id"));
                    game.setStatus(rs.getString("status"));
                    game.setCurrentTurnPlayerId((Integer) rs.getObject("current_turn_player_id"));
                    game.setWinnerId((Integer) rs.getObject("winner_id"));
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException("Error retrieving game by ID: " + gameId, e);
        }
        return game;
    }

    // Ensures there's always one active game row, or creates one if none exists.
    public synchronized Game getOrCreateActiveGame() {
        Game activeGame = getActiveGame();
        if (activeGame == null) {
            activeGame = createNewWaitingGame();
        }
        return activeGame;
    }

    // Creates a brand new game row in 'WAITING_FOR_PLAYER' status
    private Game createNewWaitingGame() {
        String sql = "INSERT INTO games (player1_id, player2_id, status, current_turn_player_id, winner_id) VALUES (?, ?, ?, ?, ?)";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            ps.setObject(1, null);
            ps.setObject(2, null);
            ps.setString(3, "WAITING_FOR_PLAYER");
            ps.setObject(4, null);
            ps.setObject(5, null);

            int rowsAffected = ps.executeUpdate();
            if (rowsAffected > 0) {
                try (ResultSet rs = ps.getGeneratedKeys()) {
                    if (rs.next()) {
                        int gameId = rs.getInt(1);
                        return new Game(gameId, null, null, "WAITING_FOR_PLAYER", null, null);
                    }
                }
            }
            throw new DataAccessException("Failed to create a new waiting game.");
        } catch (SQLException e) {
            throw new DataAccessException("Failed to create new waiting game.", e);
        }
    }

    // Adds a player to the game. playerNum should be 1 or 2.
    public boolean addPlayerToGame(int gameId, int playerId, int playerNum) {
        String sql;
        String newStatus;
        if (playerNum == 1) {
            sql = "UPDATE games SET player1_id = ?, status = ? WHERE id = ? AND player1_id IS NULL";
            newStatus = "WAITING_FOR_PLAYER"; // Still waiting after player1 joins
        } else if (playerNum == 2) {
            sql = "UPDATE games SET player2_id = ?, status = ? WHERE id = ? AND player2_id IS NULL";
            newStatus = "IN_PROGRESS"; // Game starts once player2 joins
        } else {
            throw new IllegalArgumentException("playerNum must be 1 or 2.");
        }

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, playerId);
            ps.setString(2, newStatus);
            ps.setInt(3, gameId);
            int rowsAffected = ps.executeUpdate();
            return rowsAffected > 0;
        } catch (SQLException e) {
            throw new DataAccessException("Failed to add player to game.", e);
        }
    }

    public void updateGameStatus(int gameId, String newStatus) {
        String sql = "UPDATE games SET status = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, newStatus);
            ps.setInt(2, gameId);
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Failed to update game status.", e);
        }
    }

    public void updateCurrentTurn(int gameId, int nextPlayerId) {
        String sql = "UPDATE games SET current_turn_player_id = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, nextPlayerId);
            ps.setInt(2, gameId);
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Failed to update current turn.", e);
        }
    }

    public void setGameWinner(int gameId, int winnerId, String status) {
        String sql = "UPDATE games SET winner_id = ?, status = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, winnerId);
            ps.setString(2, status);
            ps.setInt(3, gameId);
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Failed to set game winner.", e);
        }
    }

    // Resets the game for new players by clearing ships and shots, and resetting game status.
    public boolean resetGameForNewPlayers(int gameId) {
        Connection conn = null;
        try {
            conn = DBConnection.getConnection();
            conn.setAutoCommit(false); // Start transaction

            // 1. Clear ships and shots
            // This method now also needs to handle its own connection or be passed one
            clearShipsAndShotsForGame(gameId, conn);

            // 2. Reset game status in 'games' table
            String sql = "UPDATE games SET player1_id = NULL, player2_id = NULL, status = 'WAITING_FOR_PLAYER', current_turn_player_id = NULL, winner_id = NULL WHERE id = ?";
            try (PreparedStatement ps = conn.prepareStatement(sql)) {
                ps.setInt(1, gameId);
                int rowsAffected = ps.executeUpdate();
                if (rowsAffected > 0) {
                    conn.commit(); // Commit transaction
                    return true;
                }
            }
            conn.rollback(); // Rollback if update failed (e.g., 0 rows affected or PS creation failed)
            return false;
        } catch (SQLException e) {
            try {
                if (conn != null) conn.rollback(); // Rollback on error
            } catch (SQLException rollbackEx) {
                // If rollback itself fails, we just let it be.
                // The primary exception `e` is what we care about.
            }

            // Rethrow the original exception wrapped in DataAccessException
            throw new DataAccessException("Failed to reset game.", e);
        } finally {
            // Ensure auto-commit is restored and connection is closed
            try {
                if (conn != null) conn.setAutoCommit(true); // Restore auto-commit
            } catch (SQLException autoCommitEx) {
                // If restoring auto-commit fails, we just let it be.
            }
            try {
                if (conn != null) conn.close(); // Close connection
            } catch (SQLException closeEx) {
                // If closing connection fails, we just let it be.
                // It's a cleanup error, and we're not logging or rethrowing it directly
                // as it would mask the original exception if one occurred earlier.
            }
        }
    }

    // This method needs to accept a Connection object when called within a transaction
    private void clearShipsAndShotsForGame(int gameId, Connection conn) throws SQLException {
        // Delete shots first because `sunk_ship_id` in `shots` references `ships.id`
        String deleteShotsSql = "DELETE FROM shots WHERE game_id = ?";
        try (PreparedStatement ps = conn.prepareStatement(deleteShotsSql)) {
            ps.setInt(1, gameId);
            ps.executeUpdate();
        }

        String deleteShipsSql = "DELETE FROM ships WHERE game_id = ?";
        try (PreparedStatement ps = conn.prepareStatement(deleteShipsSql)) {
            ps.setInt(1, gameId);
            ps.executeUpdate();
        }
    }

    // --- Ship Management ---

    public int countShipsForPlayerInGame(int gameId, int playerId) {
        String sql = "SELECT COUNT(*) FROM ships WHERE game_id = ? AND player_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, gameId);
            ps.setInt(2, playerId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return rs.getInt(1);
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException("Failed to count ships.", e);
        }
        return 0;
    }

    public void addShip(Ship ship) {
        String sql = "INSERT INTO ships (game_id, player_id, position_x1, position_y1, position_x2, position_y2, sunk) VALUES (?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, ship.getGameId());
            ps.setInt(2, ship.getPlayerId());
            ps.setInt(3, ship.getPositionX1());
            ps.setInt(4, ship.getPositionY1());
            ps.setInt(5, ship.getPositionX2());
            ps.setInt(6, ship.getPositionY2());
            ps.setBoolean(7, ship.isSunk()); // Should be false for new ships
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Failed to add ship.", e);
        }
    }

    public List<Ship> getShipsForPlayerInGame(int gameId, int playerId) {
        List<Ship> ships = new ArrayList<>();
        String sql = "SELECT id, game_id, player_id, position_x1, position_y1, position_x2, position_y2, sunk, hits FROM ships WHERE game_id = ? AND player_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, gameId);
            ps.setInt(2, playerId);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    Ship ship = new Ship();
                    ship.setId(rs.getInt("id"));
                    ship.setGameId(rs.getInt("game_id"));
                    ship.setPlayerId(rs.getInt("player_id"));
                    ship.setPositionX1(rs.getInt("position_x1"));
                    ship.setPositionY1(rs.getInt("position_y1"));
                    ship.setPositionX2(rs.getInt("position_x2"));
                    ship.setPositionY2(rs.getInt("position_y2"));
                    ship.setHits(rs.getInt("hits"));
                    ship.setSunk(rs.getBoolean("sunk"));
                    ships.add(ship);
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException("Failed to retrieve ships.", e);
        }
        return ships;
    }

    public void updateShipSunkStatus(int shipId, boolean sunkStatus) {
        String sql = "UPDATE ships SET sunk = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setBoolean(1, sunkStatus);
            ps.setInt(2, shipId);
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Failed to update ship sunk status.", e);
        }
    }

    public int countSunkShipsForPlayerInGame(int gameId, int playerId) {
        String sql = "SELECT COUNT(*) FROM ships WHERE game_id = ? AND player_id = ? AND sunk = TRUE";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, gameId);
            ps.setInt(2, playerId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return rs.getInt(1);
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException("Failed to count sunk ships.", e);
        }
        return 0;
    }

    // --- Shot Management ---

    public void recordShot(Shot shot) {
        String sql = "INSERT INTO shots (game_id, firing_player_id, target_player_id, x, y, hit) VALUES (?, ?, ?, ?, ?, ?)";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, shot.getGameId());
            ps.setInt(2, shot.getFiringPlayerId());
            ps.setInt(3, shot.getTargetPlayerId());
            ps.setInt(4, shot.getX());
            ps.setInt(5, shot.getY());
            ps.setBoolean(6, shot.isHit());
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Failed to record shot.", e);
        }
    }

    public void recordShipHit(Ship hitShip) {
        String sql = "UPDATE ships SET hits = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, hitShip.getHits());
            ps.setInt(2, hitShip.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Failed to record hit.", e);
        }
    }

    public void updateShip( Ship ship) {
        String sql = "UPDATE ships SET hits = ?, sunk = ? WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, ship.getHits());
            ps.setBoolean(2, ship.isSunk());
            ps.setInt(3, ship.getId());
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Failed to update ship.", e);
        }
    }

    public List<Shot> getShotsAgainstPlayerInGame(int gameId, int playerId) {
        List<Shot> shots = new ArrayList<>();
        String sql = "SELECT id, game_id, firing_player_id, target_player_id, x, y, hit FROM shots WHERE game_id = ? AND target_player_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, gameId);
            ps.setInt(2, playerId);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    Shot shot = new Shot();
                    shot.setId(rs.getInt("id"));
                    shot.setGameId(rs.getInt("game_id"));
                    shot.setFiringPlayerId(rs.getInt("firing_player_id"));
                    shot.setTargetPlayerId(rs.getInt("target_player_id"));
                    shot.setX(rs.getInt("x"));
                    shot.setY(rs.getInt("y"));
                    shot.setHit(rs.getBoolean("hit"));
                    shots.add(shot);
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException("Failed to retrieve shots against player.", e);
        }
        return shots;
    }

    public List<Shot> getShotsFiredByPlayerInGame(int gameId, int playerId) {
        List<Shot> shots = new ArrayList<>();
        String sql = "SELECT id, game_id, firing_player_id, target_player_id, x, y, hit FROM shots WHERE game_id = ? AND firing_player_id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, gameId);
            ps.setInt(2, playerId);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) {
                    Shot shot = new Shot();
                    shot.setId(rs.getInt("id"));
                    shot.setGameId(rs.getInt("game_id"));
                    shot.setFiringPlayerId(rs.getInt("firing_player_id"));
                    shot.setTargetPlayerId(rs.getInt("target_player_id"));
                    shot.setX(rs.getInt("x"));
                    shot.setY(rs.getInt("y"));
                    shot.setHit(rs.getBoolean("hit"));
                    shots.add(shot);
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException("Failed to retrieve shots fired by player.", e);
        }
        return shots;
    }

    // Helper to retrieve user details (username)
    public User getUserById(int userId) {
        User user = null;
        String sql = "SELECT id, username FROM users WHERE id = ?";
        try (Connection conn = DBConnection.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, userId);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    user = new User();
                    user.setId(rs.getInt("id"));
                    user.setUsername(rs.getString("username"));
                }
            }
        } catch (SQLException e) {
            throw new DataAccessException("Failed to get user by ID.", e);
        }
        return user;
    }
}