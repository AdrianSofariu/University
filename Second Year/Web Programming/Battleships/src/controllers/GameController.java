// src/main/java/servlets/GameServlet.java
package controllers;

import dao.GameDAO;
import exceptions.DataAccessException;
import models.Game;
import models.Ship;
import models.Shot;
import models.User;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.io.Serial;
import java.util.List;
import java.util.Random;
import java.util.logging.Logger;

public class GameController extends HttpServlet {

    @Serial
    private static final long serialVersionUID = 1L;
    private GameDAO gameDAO;

    public void init() {
        gameDAO = new GameDAO();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("loggedInUser") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        User loggedInUser = (User) session.getAttribute("loggedInUser");
        int userId = loggedInUser.getId();
        Integer sessionGameId = (Integer) session.getAttribute("currentGameId"); // Game ID from session

        try {
            // Game game = gameDAO.getActiveGame(); // Get the current global game from DB
            Game game = gameDAO.getGameById(sessionGameId);
            if (game == null) {
                // This state should ideally not happen if getOrCreateActiveGame works as expected
                response.sendRedirect("dashboard?error=no_active_game");
                return;
            }

            // Ensure the user is part of THIS active game. If not, redirect.
            if (!game.isPlayerInGame(userId)) {
                // If game is full and user not in it, they cannot proceed
                if (game.isGameFull()) {
                    response.sendRedirect("dashboard?error=game_full");
                    return;
                }
                // If game is waiting and user not in it, they must join from dashboard
                response.sendRedirect("dashboard?error=not_in_game");
                return;
            }

            // Update session gameId if it changed (e.g., after a reset on dashboard)
            if (sessionGameId == null || sessionGameId != game.getId()) {
                session.setAttribute("currentGameId", game.getId());
            }

            // --- Pass data to JSP ---
            request.setAttribute("game", game);
            request.setAttribute("loggedInUser", loggedInUser);

            // Fetch player's own ships
            List<Ship> playerShips = gameDAO.getShipsForPlayerInGame(game.getId(), userId);
            request.setAttribute("playerShips", playerShips);
            request.setAttribute("shipsPlacedCount", playerShips.size());

            // Determine if player still needs to place ships
            boolean needsToPlaceShips = (playerShips.size() < 2);
            request.setAttribute("needsToPlaceShips", needsToPlaceShips);

            // Fetch opponent's ID and User object for display
            Integer opponentId = null;
            User opponentUser = null;
            if (game.isGameFull()) {
                opponentId = (game.getPlayer1Id().equals(userId)) ? game.getPlayer2Id() : game.getPlayer1Id();
                opponentUser = gameDAO.getUserById(opponentId);
            }
            request.setAttribute("opponentId", opponentId);
            request.setAttribute("opponentUser", opponentUser);

            // Fetch shots against player (to mark hits/misses on own board)
            List<Shot> shotsAgainstMe = gameDAO.getShotsAgainstPlayerInGame(game.getId(), userId);
            request.setAttribute("shotsAgainstMe", shotsAgainstMe);

            // Fetch shots fired by player (to mark hits/misses on opponent's board)
            List<Shot> myFiredShots = gameDAO.getShotsFiredByPlayerInGame(game.getId(), userId);
            request.setAttribute("myFiredShots", myFiredShots);

            // Game Status Messages for JSP
            String gameStatusMessage = "";
            if (game.isGameOver()) {
                if (game.getWinnerId() != null && game.getWinnerId().equals(userId)) {
                    gameStatusMessage = "Congratulations! You won the game!";
                } else if (game.getWinnerId() != null) {
                    User winner = gameDAO.getUserById(game.getWinnerId());
                    if (winner != null) {
                        gameStatusMessage = winner.getUsername() + " won the game. You lost!";
                    } else {
                        gameStatusMessage = "Game Over. A player won, but their name could not be retrieved.";
                    }
                } else {
                    gameStatusMessage = "Game Over. The game ended without a clear winner (e.g., reset).";

                }
            } else if (!game.isGameFull()) {
                gameStatusMessage = "Waiting for an opponent to join...";
            } else { // Game is full
                if (needsToPlaceShips) {
                    gameStatusMessage = "Place your remaining ships!";
                } else {
                    gameStatusMessage = "Game in progress!";
                    if (game.getCurrentTurnPlayerId() != null && game.getCurrentTurnPlayerId().equals(userId)) {
                        gameStatusMessage += " It's your turn!";
                    } else if (opponentUser != null) {
                        gameStatusMessage += " Waiting for " + opponentUser.getUsername() + "'s turn.";
                    } else {
                        gameStatusMessage += " Waiting for opponent's turn.";
                    }
                }
            }
            request.setAttribute("gameStatusMessage", gameStatusMessage);

            request.getRequestDispatcher("game.jsp").forward(request, response);

        } catch (DataAccessException e) {
            request.setAttribute("errorMessage", "A database error occurred. Please try again later.");
            request.getRequestDispatcher("error.jsp").forward(request, response);
        } catch (Exception e) { // Catch any other unexpected RuntimeException
            request.setAttribute("errorMessage", "An unexpected error occurred. Please try again later.");
            request.getRequestDispatcher("error.jsp").forward(request, response);
        }
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("loggedInUser") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        User loggedInUser = (User) session.getAttribute("loggedInUser");
        int userId = loggedInUser.getId();
        Integer gameId = (Integer) session.getAttribute("currentGameId");

        if (gameId == null) {
            response.sendRedirect("dashboard?error=no_game_id");
            return;
        }

        try {
            // Game game = gameDAO.getActiveGame();
            Game game = gameDAO.getGameById(gameId);
            if (game == null || !game.isPlayerInGame(userId)) {
                // If game is null or user is not in it, redirect to dashboard.
                response.sendRedirect("dashboard?error=game_invalid_state");
                return;
            }
            // Update session gameId in case a new game was created (e.g., after prior reset)
            if (gameId != game.getId()) {
                session.setAttribute("currentGameId", game.getId());
                gameId = game.getId();
            }

            // If game is already over, only allow reset.
            if (game.isGameOver()) {
                String action = request.getParameter("action");
                if ("reset_game".equals(action)) {
                    handleResetGame(request, response, game, gameId, session);
                } else {
                    request.setAttribute("errorMessage", "The game is over. Please reset to play again.");
                    doGet(request, response);
                }
                return;
            }

            String action = request.getParameter("action");

            if ("place_ship".equals(action)) {
                handlePlaceShip(request, response, game, userId, gameId);
            } else if ("fire_shot".equals(action)) {
                handleFireShot(request, response, game, userId, gameId);
            } else if ("reset_game".equals(action)) {
                handleResetGame(request, response, game, gameId, session);
            } else {
                request.setAttribute("errorMessage", "Invalid game action.");
                doGet(request, response);
            }

        } catch (DataAccessException e) {
            request.setAttribute("errorMessage", "A database error occurred during game action: " + e.getMessage());
            doGet(request, response);
        } catch (NumberFormatException e) {
            request.setAttribute("errorMessage", "Invalid input for coordinates. Please use numbers.");
            doGet(request, response);
        } catch (IllegalArgumentException e) {
            request.setAttribute("errorMessage", e.getMessage());
            doGet(request, response);
        } catch (Exception e) { // Catch any other unexpected RuntimeException
            request.setAttribute("errorMessage", "An unexpected error occurred. Please try again later.");
            doGet(request, response);
        }
    }

    private void handlePlaceShip(HttpServletRequest request, HttpServletResponse response, Game game, int userId, int gameId) throws ServletException, IOException, DataAccessException {
        // Ensure game is in a state where ships can be placed
        if (!game.isGameFull() && !game.isGameWaiting()) { // If not full, or waiting, or player not in game.
            request.setAttribute("errorMessage", "Game is not in a state for ship placement.");
            doGet(request, response);
            return;
        }

        int shipsPlaced = gameDAO.countShipsForPlayerInGame(gameId, userId);
        if (shipsPlaced >= 2) {
            request.setAttribute("errorMessage", "You have already placed 2 ships.");
            doGet(request, response);
            return;
        }

        int startX = Integer.parseInt(request.getParameter("startX"));
        int startY = Integer.parseInt(request.getParameter("startY"));
        String orientation = request.getParameter("orientation");

        int endX, endY;
        if ("HORIZONTAL".equals(orientation)) {
            endX = startX;
            endY = startY + 1;
        } else if ("VERTICAL".equals(orientation)) {
            endX = startX + 1;
            endY = startY;
        } else {
            throw new IllegalArgumentException("Invalid orientation. Must be HORIZONTAL or VERTICAL.");
        }

        // --- VALIDATION for ship placement ---
        // 1. Check if coordinates are within board bounds (0-9 for 10x10 grid for both segments)
        if (startX < 0 || startX > 9 || startY < 0 || startY > 9 ||
                endX < 0 || endX > 9 || endY < 0 || endY > 9) {
            request.setAttribute("errorMessage", "Ship coordinates are out of bounds (0-9).");
            doGet(request, response);
            return;
        }

        // 2. Check for overlapping with existing ships for this player.
        List<Ship> existingShips = gameDAO.getShipsForPlayerInGame(gameId, userId);
        Ship newShip = new Ship(gameId, userId, startX, startY, endX, endY);
        for (Ship existingShip : existingShips) {
            for (int[] newCoord : newShip.getCoordinates()) {
                if (existingShip.containsCoordinate(newCoord[0], newCoord[1])) { // Check both X and Y
                    request.setAttribute("errorMessage", "Ships cannot overlap.");
                    doGet(request, response);
                    return;
                }
            }
        }
        // --- END VALIDATION ---

        gameDAO.addShip(newShip);

        // After placing a ship, check if both players have placed all their ships to start the game
        boolean player1Ready = gameDAO.countShipsForPlayerInGame(gameId, game.getPlayer1Id()) == 2;
        boolean player2Ready = false;
        if (game.getPlayer2Id() != null) { // Only check if player 2 exists
            player2Ready = gameDAO.countShipsForPlayerInGame(gameId, game.getPlayer2Id()) == 2;
        }

        if (game.isGameFull() && player1Ready && player2Ready) {
            gameDAO.updateGameStatus(gameId, "IN_PROGRESS");
            // Randomly decide who goes first
            int firstPlayerId = (new Random().nextBoolean()) ? game.getPlayer1Id() : game.getPlayer2Id();
            gameDAO.updateCurrentTurn(gameId, firstPlayerId);
        }

        response.sendRedirect("game?shipPlaced=true");
    }

    private void handleFireShot(HttpServletRequest request, HttpServletResponse response, Game game, int userId, int gameId) throws ServletException, IOException, DataAccessException {
        if (!game.isGameInProgress()) {
            request.setAttribute("errorMessage", "Game is not in progress.");
            doGet(request, response);
            return;
        }
        if (game.getCurrentTurnPlayerId() == null || !game.getCurrentTurnPlayerId().equals(userId)) {
            request.setAttribute("errorMessage", "It's not your turn.");
            doGet(request, response);
            return;
        }

        int targetX = Integer.parseInt(request.getParameter("targetX"));
        int targetY = Integer.parseInt(request.getParameter("targetY"));

        // 1. Validate shot coordinates (in bounds)
        if (targetX < 0 || targetX > 9 || targetY < 0 || targetY > 9) {
            request.setAttribute("errorMessage", "Shot coordinates are out of bounds (0-9).");
            doGet(request, response);
            return;
        }

        Integer opponentId = (game.getPlayer1Id().equals(userId)) ? game.getPlayer2Id() : game.getPlayer1Id();
        if (opponentId == null) { // Should not happen in IN_PROGRESS state
            throw new IllegalArgumentException("Opponent ID not found for game in progress.");
        }

        // Check if this spot has already been shot
        List<Shot> myFiredShots = gameDAO.getShotsFiredByPlayerInGame(gameId, userId);
        for (Shot shot : myFiredShots) {
            if (shot.getX() == targetX && shot.getY() == targetY) {
                request.setAttribute("errorMessage", "You have already shot at (" + targetX + ", " + targetY + ").");
                doGet(request, response);
                return;
            }
        }

        // 2. Determine hit/miss
        List<Ship> opponentShips = gameDAO.getShipsForPlayerInGame(gameId, opponentId);
        boolean hit = false;
        Integer sunkShipId = null;
        Ship hitShip = null; // To store the ship that was hit

        for (Ship ship : opponentShips) {
            if (ship.containsCoordinate(targetX, targetY)) {
                hit = true;
                ship.recordHit();
                hitShip = ship;
                break;
            }
        }

        String feedbackMsg = "";
        if (hit) {
            gameDAO.updateShip(hitShip);
            // Check if the hit ship has 2 hits
            if(hitShip.isSunk()) {
                feedbackMsg = "Hit! You SUNK a ship!";
                sunkShipId = hitShip.getId(); // Store sunk ship ID for win condition check
            } else {
                feedbackMsg = "Hit! You hit a ship!";
            }
        } else {
            feedbackMsg = "Miss!";
        }
        request.setAttribute("feedbackMessage", feedbackMsg);


        // 3. Record the shot
        Shot newShot = new Shot(gameId, userId, opponentId, targetX, targetY, hit);
        gameDAO.recordShot(newShot);

        // 4. Check Win Condition (only if a ship was sunk)
        if (sunkShipId != null) {
            int opponentSunkShipsCount = gameDAO.countSunkShipsForPlayerInGame(gameId, opponentId);
            if (opponentSunkShipsCount == 2) { // Assuming each player has 2 ships
                gameDAO.setGameWinner(gameId, userId, (userId == game.getPlayer1Id() ? "PLAYER1_WON" : "PLAYER2_WON"));
                // response.sendRedirect("game?gameOver=true"); // Redirect to show winner
                // doGet(request, response);
                response.sendRedirect("game");
                return;
            }
        }

        // 5. Switch Turn (only if game is still in progress)
        if (game.isGameInProgress()) { // Check game status again after potential win
            gameDAO.updateCurrentTurn(gameId, opponentId);
            response.sendRedirect("game?shotFired=true"); // Redirect to show feedback and new turn
        } else {
            // If game is over, the above redirect for gameOver=true would have handled it.
            // If not gameOver, but not IN_PROGRESS, might be an edge case. Just refresh.
            response.sendRedirect("game");
        }
    }

    private void handleResetGame(HttpServletRequest request, HttpServletResponse response, Game game, int gameId, HttpSession session) throws ServletException, IOException, DataAccessException {
        // Only allow reset if game has been played (is full) or is explicitly over.
        if (game.isGameFull() || game.isGameOver()) {
            gameDAO.resetGameForNewPlayers(game.getId());
            session.removeAttribute("currentGameId"); // Clear session for this user
            response.sendRedirect("dashboard?message=game_reset");
            return;
        }
        request.setAttribute("errorMessage", "Cannot reset game yet. Game must be full or over.");
        doGet(request, response);
    }
}