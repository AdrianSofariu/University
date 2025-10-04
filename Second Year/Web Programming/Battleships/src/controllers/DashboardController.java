package controllers;



import dao.GameDAO;
import exceptions.DataAccessException;
import models.Game;
import models.User;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.io.Serial;

public class DashboardController extends HttpServlet {

    @Serial
    private static final long serialVersionUID = 1L;
    private GameDAO gameDAO;

    public void init() {
        gameDAO = new GameDAO();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("loggedInUser") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        User loggedInUser = (User) session.getAttribute("loggedInUser");
        String message = null;
        String action = null; // "play" or "view_game" or "game_full"

        try {
            Game activeGame = gameDAO.getOrCreateActiveGame(); // Ensures a game exists

            if (activeGame.isPlayerInGame(loggedInUser.getId())) {
                // User is already part of the game
                message = "You are already in a game.";
                action = "view_game"; // Redirect to GameServlet to view/continue game
                request.setAttribute("gameId", activeGame.getId()); // Pass game ID
            } else if (activeGame.isGameFull()) {
                // Game is full, user cannot join
                message = "A game is currently in progress. Please wait for it to finish.";
                action = "game_full";
            } else if (activeGame.isGameWaiting()) {
                // Game is waiting for players
                message = "A game is waiting for another player. Click Play to join!";
                action = "play"; // Show Play button to join
                request.setAttribute("gameId", activeGame.getId()); // Pass game ID
            } else {
                // This state should ideally not happen if getOrCreateActiveGame works correctly,
                // but handles edge cases if game status is not one of the expected.
                message = "Game state is ambiguous. Please try again later.";
                action = "game_full"; // Treat as full for safety
            }

            request.setAttribute("message", message);
            request.setAttribute("action", action); // Determines what button/message to show
            request.getRequestDispatcher("dashboard.jsp").forward(request, response);

        } catch (DataAccessException e) {
            request.setAttribute("errorMessage", "A database error occurred. Please try again later.");
            request.getRequestDispatcher("error.jsp").forward(request, response);
        }
    }

    // Handle POST request for joining the game
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("loggedInUser") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        User loggedInUser = (User) session.getAttribute("loggedInUser");
        int userId = loggedInUser.getId();

        try {
            Game activeGame = gameDAO.getOrCreateActiveGame();

            if (activeGame.isPlayerInGame(userId)) {
                // User is already in, redirect to game
                response.sendRedirect("game?gameId=" + activeGame.getId());
                return;
            } else if (activeGame.isGameFull()) {
                // Game is full, can't join
                response.sendRedirect("dashboard?error=game_full"); // Redirect back with error
                return;
            }

            // User is not in game, and game is not full -> attempt to join
            boolean joined = false;
            if (activeGame.getPlayer1Id() == null) {
                // If player1 slot is empty, take it
                joined = gameDAO.addPlayerToGame(activeGame.getId(), userId, 1);
            } else if (activeGame.getPlayer2Id() == null) {
                // If player2 slot is empty, take it
                joined = gameDAO.addPlayerToGame(activeGame.getId(), userId, 2);
            }

            if (joined) {
                // Store game ID in session for easier access in GameServlet
                session.setAttribute("currentGameId", activeGame.getId());
                response.sendRedirect("game"); // Redirect to GameServlet
            } else {
                // This case handles a race condition or an unexpected state
                response.sendRedirect("dashboard?error=join_failed"); // Redirect back with error
            }

        } catch (DataAccessException e) {
            response.sendRedirect("dashboard?error=db_error");
        }
    }
}