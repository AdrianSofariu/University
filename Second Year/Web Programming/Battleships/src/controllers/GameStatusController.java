package controllers;

import dao.GameDAO;
import dao.UserDAO; // Import UserDAO
import exceptions.DataAccessException;
import models.Game;
import models.User; // Import User model

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.Serial;

import org.json.simple.JSONObject;

@WebServlet("/game-status") // Map this servlet to the /game-status URL
public class GameStatusController extends HttpServlet {

    @Serial
    private static final long serialVersionUID = 1L;
    private GameDAO gameDAO = new GameDAO();
    private UserDAO userDAO = new UserDAO(); // Instantiate UserDAO

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        int gameId;
        try {
            gameId = Integer.parseInt(request.getParameter("gameId"));
        } catch (NumberFormatException e) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, "Invalid game ID");
            return;
        }

        try {
            Game game = gameDAO.getGameById(gameId);
            if (game == null) {
                response.sendError(HttpServletResponse.SC_NOT_FOUND, "Game not found");
                return;
            }

            // --- Fetch Usernames ---
            String player1Username = null;
            if (game.getPlayer1Id() != null) {
                User player1 = userDAO.getUserById(game.getPlayer1Id());
                if (player1 != null) {
                    player1Username = player1.getUsername();
                }
            }

            String player2Username = null;
            if (game.getPlayer2Id() != null) {
                User player2 = userDAO.getUserById(game.getPlayer2Id());
                if (player2 != null) {
                    player2Username = player2.getUsername();
                }
            }
            // --- End Fetch Usernames ---

            // --- Create JSON object using json-simple ---
            JSONObject jsonResponse = new JSONObject();
            jsonResponse.put("status", game.getStatus());
            jsonResponse.put("player1Id", game.getPlayer1Id());
            jsonResponse.put("player1Username", player1Username);
            jsonResponse.put("player2Id", game.getPlayer2Id());
            jsonResponse.put("player2Username", player2Username);
            jsonResponse.put("currentTurnPlayerId", game.getCurrentTurnPlayerId());
            jsonResponse.put("winnerId", game.getWinnerId());
            // --- End Create JSON object ---

            response.getWriter().write(jsonResponse.toJSONString()); // Convert JSONObject to string

        } catch (DataAccessException e) {
            System.err.println("Database error retrieving game status: " + e.getMessage());
            response.sendError(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, "Database error retrieving game status.");
        }
    }

    // Helper class for JSON serialization - NOW INCLUDES usernames
    private static class GameStatusResponse {
        String status;
        Integer player1Id;
        String player1Username; // New field
        Integer player2Id;
        String player2Username; // New field
        Integer currentTurnPlayerId;
        Integer winnerId;

        public GameStatusResponse(String status, Integer player1Id, String player1Username, Integer player2Id, String player2Username, Integer currentTurnPlayerId, Integer winnerId) {
            this.status = status;
            this.player1Id = player1Id;
            this.player1Username = player1Username; // Assign new field
            this.player2Id = player2Id;
            this.player2Username = player2Username; // Assign new field
            this.currentTurnPlayerId = currentTurnPlayerId;
            this.winnerId = winnerId;
        }
        // Gson can work directly with fields, no need for getters/setters unless you want custom serialization
    }
}