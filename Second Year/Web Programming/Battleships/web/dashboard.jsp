<%-- src/main/webapp/dashboard.jsp --%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="models.User" %>
<%
  // Retrieve data from request attributes and URL parameters
  User loggedInUser = (User) session.getAttribute("loggedInUser");
  String message = (String) request.getAttribute("message");
  String action = (String) request.getAttribute("action");
  String errorMessage = (String) request.getAttribute("errorMessage");
  String paramError = request.getParameter("error");
  String paramMessage = request.getParameter("message");
%>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard - Ships Game</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }
    .container { max-width: 800px; margin: auto; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    h1 { color: #0056b3; }
    .welcome-message { margin-bottom: 20px; font-size: 1.1em; }
    .game-status-message {
      padding: 15px;
      margin-bottom: 20px;
      border-radius: 5px;
      font-weight: bold;
    }
    .message-info { background-color: #e0f7fa; border: 1px solid #00bcd4; color: #00796b; }
    .message-warning { background-color: #fffde7; border: 1px solid #ffeb3b; color: #fbc02d; }
    .message-error { background-color: #ffebee; border: 1px solid #ef5350; color: #d32f2f; }
    .play-button, .view-game-button {
      display: inline-block;
      background-color: #28a745;
      color: white;
      padding: 12px 25px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      text-decoration: none;
      font-size: 1.1em;
      transition: background-color 0.3s ease;
    }
    .play-button:hover, .view-game-button:hover {
      background-color: #218838;
    }
    .logout-button {
      background-color: #dc3545;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      text-decoration: none;
      float: right;
      margin-top: -50px; /* Adjust as needed */
    }
    .logout-button:hover {
      background-color: #c82333;
    }
  </style>
</head>
<body>
<div class="container">
  <a href="logout" class="logout-button">Logout</a>
  <h1>Welcome to your Dashboard, <%= loggedInUser.getUsername() %>!</h1>

  <% if (errorMessage != null) { %>
  <p class="game-status-message message-error"><%= errorMessage %></p>
  <% } %>
  <% if (paramError != null) { %>
  <% if (paramError.equals("game_full")) { %>
  <p class="game-status-message message-warning">A game is currently in progress. Please wait for it to finish.</p>
  <% } else if (paramError.equals("join_failed")) { %>
  <p class="game-status-message message-error">Failed to join the game. Perhaps another player just joined?</p>
  <% } else if (paramError.equals("db_error")) { %>
  <p class="game-status-message message-error">A database error occurred. Please try again later.</p>
  <% } else if (paramError.equals("not_in_game")) { %>
  <p class="game-status-message message-warning">You are not currently part of the active game. Please click Play to join or wait for a game to end.</p>
  <% } else if (paramError.equals("no_active_game")) { %>
  <p class="game-status-message message-error">No active game found. Please try joining again.</p>
  <% } else if (paramError.equals("game_invalid_state")) { %>
  <p class="game-status-message message-error">The game is in an invalid state. Please try again.</p>
  <% } else if (paramError.equals("no_game_id")) { %>
  <p class="game-status-message message-error">Could not retrieve game ID. Please try again.</p>
  <% } else { %>
  <p class="game-status-message message-error">An unexpected error occurred.</p>
  <% } %>
  <% } %>
  <% if (paramMessage != null && paramMessage.equals("game_reset")) { %>
  <p class="game-status-message message-info">The game has been reset successfully. You can now join a new game.</p>
  <% } %>


  <p class="game-status-message message-info"><%= message %></p>

  <% if (action != null) { %>
  <% if (action.equals("play")) { %>
  <form action="dashboard" method="post">
    <button type="submit" class="play-button">Play Game</button>
  </form>
  <% } else if (action.equals("view_game")) { %>
  <a href="game" class="view-game-button">Continue Game</a>
  <% } %>
  <% } %>
</div>
</body>
</html>