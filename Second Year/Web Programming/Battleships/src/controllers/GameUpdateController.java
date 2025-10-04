package controllers;

import dao.GameDAO;
import dao.UserDAO;
import exceptions.DataAccessException;
import models.Game;
import models.Ship;
import models.Shot;
import models.User;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.List;

@WebServlet("/game-update")
public class GameUpdateController extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private GameDAO gameDAO;
    private UserDAO userDAO; // You have a UserDAO, so we'll use it.

    public void init() {
        gameDAO = new GameDAO();
        userDAO = new UserDAO(); // Initialize UserDAO
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("loggedInUser") == null) {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "User not logged in.");
            return;
        }

        User loggedInUser = (User) session.getAttribute("loggedInUser");
        int userId = loggedInUser.getId();

        int gameId;
        try {
            gameId = Integer.parseInt(request.getParameter("gameId"));
        } catch (NumberFormatException e) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid game ID.");
            return;
        }

        JSONObject jsonResponse = new JSONObject();
        try {
            Game game = gameDAO.getGameById(gameId);
            if (game == null || !game.isPlayerInGame(userId)) {
                // If game no longer exists or user is not part of it, indicate this.
                // The client-side JS should then redirect or show an error.
                jsonResponse.put("gameExists", false);
                response.getWriter().write(jsonResponse.toJSONString());
                return;
            }
            jsonResponse.put("gameExists", true);

            // --- Game State Details ---
            jsonResponse.put("gameId", game.getId());
            jsonResponse.put("status", game.getStatus());
            jsonResponse.put("currentTurnPlayerId", game.getCurrentTurnPlayerId());
            jsonResponse.put("winnerId", game.getWinnerId());

            // Player usernames
            User player1 = userDAO.getUserById(game.getPlayer1Id());
            User player2 = null;
            if (game.getPlayer2Id() != null) {
                player2 = userDAO.getUserById(game.getPlayer2Id());
            }

            jsonResponse.put("player1Id", game.getPlayer1Id());
            jsonResponse.put("player1Username", (player1 != null ? player1.getUsername() : "Player 1"));
            jsonResponse.put("player2Id", game.getPlayer2Id());
            jsonResponse.put("player2Username", (player2 != null ? player2.getUsername() : "Player 2"));

            Integer opponentId = null;
            if (game.isGameFull()) {
                opponentId = (game.getPlayer1Id().equals(userId)) ? game.getPlayer2Id() : game.getPlayer1Id();
            }
            jsonResponse.put("opponentId", opponentId);
            jsonResponse.put("opponentUsername", (opponentId != null ? userDAO.getUserById(opponentId).getUsername() : "Opponent"));


            // --- Board Data for the current logged-in user ---
            List<Ship> playerShips = gameDAO.getShipsForPlayerInGame(gameId, userId);
            List<Shot> shotsAgainstMe = gameDAO.getShotsAgainstPlayerInGame(gameId, userId);
            List<Shot> myFiredShots = gameDAO.getShotsFiredByPlayerInGame(gameId, userId);

            // Determine if player still needs to place ships
            boolean needsToPlaceShips = (playerShips.size() < 2);
            jsonResponse.put("needsToPlaceShips", needsToPlaceShips);
            jsonResponse.put("shipsPlacedCount", playerShips.size());


            // Player's board:
            // 0: empty water
            // 1: player ship (not hit)
            // 2: opponent shot - miss
            // 3: opponent shot - hit (on player's ship)
            // 4: player ship - sunk
            JSONArray playerBoardJson = new JSONArray();
            int[][] playerBoard = new int[10][10];

            // Initialize player's board with their ships
            if (playerShips != null) {
                for (Ship ship : playerShips) {
                    for (int[] coord : ship.getCoordinates()) {
                        if (coord[0] >= 0 && coord[0] < 10 && coord[1] >= 0 && coord[1] < 10) {
                            if (ship.isSunk()) {
                                playerBoard[coord[0]][coord[1]] = 4; // Sunk
                            } else {
                                playerBoard[coord[0]][coord[1]] = 1; // Ship not sunk
                            }
                        }
                    }
                }
            }

            // Mark shots against player on player's board
            if (shotsAgainstMe != null) {
                for (Shot shot : shotsAgainstMe) {
                    if (shot.getX() >= 0 && shot.getX() < 10 && shot.getY() >= 0 && shot.getY() < 10) {
                        // Only update if it's not already a sunk ship segment
                        if (playerBoard[shot.getX()][shot.getY()] != 4) { // Don't overwrite sunk status
                            if (shot.isHit()) {
                                playerBoard[shot.getX()][shot.getY()] = 3; // Hit
                            } else {
                                playerBoard[shot.getX()][shot.getY()] = 2; // Miss
                            }
                        }
                    }
                }
            }

            // Convert playerBoard to JSON array
            for (int y = 0; y < 10; y++) {
                JSONArray row = new JSONArray();
                for (int x = 0; x < 10; x++) {
                    row.add(playerBoard[y][x]);
                }
                playerBoardJson.add(row);
            }
            jsonResponse.put("playerBoard", playerBoardJson);


            // Opponent's board (from current player's perspective):
            // 0: undiscovered water
            // 1: player fired - miss
            // 2: player fired - hit (on opponent's ship)
            JSONArray opponentBoardJson = new JSONArray();
            int[][] opponentBoard = new int[10][10]; // Initialize with 0s (undiscovered)

            // Mark player's fired shots on opponent's board
            if (myFiredShots != null) {
                for (Shot shot : myFiredShots) {
                    if (shot.getX() >= 0 && shot.getX() < 10 && shot.getY() >= 0 && shot.getY() < 10) {
                        opponentBoard[shot.getX()][shot.getY()] = (shot.isHit() ? 2 : 1); // 2 for hit, 1 for miss
                    }
                }
            }

            // Convert opponentBoard to JSON array
            for (int y = 0; y < 10; y++) {
                JSONArray row = new JSONArray();
                for (int x = 0; x < 10; x++) {
                    row.add(opponentBoard[y][x]);
                }
                opponentBoardJson.add(row);
            }
            jsonResponse.put("opponentBoard", opponentBoardJson);

            response.getWriter().write(jsonResponse.toJSONString());

        } catch (DataAccessException e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Database error retrieving game update.");
        } catch (Exception e) {
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "An unexpected error occurred.");
        }
    }
}