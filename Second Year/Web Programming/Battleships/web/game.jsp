<%-- src/main/webapp/game.jsp --%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="models.Game" %>
<%@ page import="models.User" %>
<%@ page import="models.Ship" %>
<%@ page import="models.Shot" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.Random" %>
<%
  // Retrieve data from request attributes (for initial page load)
  Game game = (Game) request.getAttribute("game");
  User loggedInUser = (User) request.getAttribute("loggedInUser");
  int userId = loggedInUser.getId();
  List<Ship> playerShips = (List<Ship>) request.getAttribute("playerShips");
  List<Ship> opponentShips = (List<Ship>) request.getAttribute("opponentShips"); // This might be null if not used
  List<Shot> shotsAgainstMe = (List<Shot>) request.getAttribute("shotsAgainstMe");
  List<Shot> myFiredShots = (List<Shot>) request.getAttribute("myFiredShots");
  String gameStatusMessage = (String) request.getAttribute("gameStatusMessage");
  boolean needsToPlaceShips = (Boolean) request.getAttribute("needsToPlaceShips");
  int shipsPlacedCount = (Integer) request.getAttribute("shipsPlacedCount");
  String errorMessage = (String) request.getAttribute("errorMessage");
  String feedbackMessage = (String) request.getAttribute("feedbackMessage");
  User opponentUser = (User) request.getAttribute("opponentUser");

  // Prepare board states for rendering (initial load)
  // Player's board:
  // 0: empty water
  // 1: player ship (not hit)
  // 2: opponent shot - miss
  // 3: opponent shot - hit (on player's ship)
  // 4: player ship - sunk
  int[][] playerBoard = new int[10][10];

  // Opponent's board (from current player's perspective):
  // 0: undiscovered water
  // 1: player fired - miss
  // 2: player fired - hit (on opponent's ship)
  int[][] opponentBoard = new int[10][10];

  // Initialize player's board with their ships
  if (playerShips != null) {
    for (Ship ship : playerShips) {
      int[][] coords = ship.getCoordinates();
      // Ensure coordinates are within bounds before accessing
      if (coords != null && coords.length == 2 && coords[0].length == 2 && coords[1].length == 2 &&
              coords[0][0] >= 0 && coords[0][0] < 10 && coords[0][1] >= 0 && coords[0][1] < 10 &&
              coords[1][0] >= 0 && coords[1][0] < 10 && coords[1][1] >= 0 && coords[1][1] < 10) {

        if (ship.isSunk()) {
          playerBoard[coords[0][0]][coords[0][1]] = 4; // Sunk
          playerBoard[coords[1][0]][coords[1][1]] = 4; // Sunk
        } else {
          playerBoard[coords[0][0]][coords[0][1]] = 1; // Ship not sunk
          playerBoard[coords[1][0]][coords[1][1]] = 1; // Ship not sunk
        }
      }
    }
  }

  // Mark shots against player on player's board
  if (shotsAgainstMe != null) {
    for (Shot shot : shotsAgainstMe) {
      // Ensure coordinates are within bounds
      if (shot.getX() >= 0 && shot.getX() < 10 && shot.getY() >= 0 && shot.getY() < 10) {
        // Only update if it's not already a sunk ship segment
        if (playerBoard[shot.getX()][shot.getY()] != 4) {
          if (shot.isHit()) {
            playerBoard[shot.getX()][shot.getY()] = 3; // Hit
          } else {
            playerBoard[shot.getX()][shot.getY()] = 2; // Miss
          }
        }
      }
    }
  }

  // Mark player's fired shots on opponent's board
  if (myFiredShots != null) {
    for (Shot shot : myFiredShots) {
      // Ensure coordinates are within bounds
      if (shot.getX() >= 0 && shot.getX() < 10 && shot.getY() >= 0 && shot.getY() < 10) {
        opponentBoard[shot.getX()][shot.getY()] = (shot.isHit() ? 2 : 1); // 2 for hit, 1 for miss
      }
    }
  }
%>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ships Game - Game Board</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; color: #333; }
    .container { max-width: 1000px; margin: auto; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    h1 { color: #0056b3; text-align: center; }
    .game-info { text-align: center; margin-bottom: 20px; font-size: 1.1em; }
    .error-message { color: red; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .feedback-message { color: green; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .game-boards { display: flex; justify-content: space-around; margin-top: 20px; }
    .board { border: 1px solid #ccc; padding: 10px; min-width: 45%; }
    .board h2 { text-align: center; color: #555; }
    .grid-container {
      display: grid;
      grid-template-columns: repeat(10, 30px); /* 10x10 grid, 30px per cell */
      grid-template-rows: repeat(10, 30px);
      width: 300px; /* 10 * 30px */
      height: 300px;
      border: 1px solid black;
      margin: 10px auto;
    }
    .grid-cell {
      width: 30px;
      height: 30px;
      border: 1px solid #eee;
      box-sizing: border-box; /* Include padding and border in the element's total width and height */
      background-color: #add8e6; /* Light blue for water */
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 0.8em;
      color: #555;
    }
    /* Player's board cells (your own ships, opponent's shots on your board) */
    .grid-cell.player-ship { background-color: #778899; } /* Gray for player's own ship */
    .grid-cell.player-hit { background-color: #ff4d4d; } /* Red for hit on player's ship */
    .grid-cell.player-miss { background-color: #b0e0e6; } /* Slightly darker blue for miss on player's board */
    .grid-cell.player-sunk { background-color: #660000; color: white; } /* Darker red for sunk ship */


    /* Opponent's board cells (your shots on opponent's board) */
    .opponent-board .grid-cell.opponent-miss { background-color: #b0e0e6; } /* Miss on opponent's board */
    .opponent-board .grid-cell.opponent-hit { background-color: #ff4d4d; } /* Hit on opponent's board */


    /* Clickable cells for shooting */
    .opponent-board .grid-cell-button {
      cursor: pointer;
      padding: 0;
      margin: 0;
      background-color: #add8e6; /* inherited from .grid-cell */
      width: 100%;
      height: 100%;
    }
    .opponent-board .grid-cell-button:hover:enabled { background-color: #cceeff; }
    .opponent-board .grid-cell-button:disabled { cursor: not-allowed; opacity: 0.7; }

    .game-actions { text-align: center; margin-top: 20px; }
    .game-actions button {
      padding: 10px 20px;
      font-size: 1em;
      cursor: pointer;
      border: none;
      border-radius: 5px;
      margin: 5px;
    }
    .reset-button { background-color: #dc3545; color: white; }
    .reset-button:hover { background-color: #c82333; }
    .back-to-dashboard { display: block; text-align: center; margin-top: 30px; }
    .game-over-message {
      font-size: 1.5em;
      font-weight: bold;
      color: #007bff;
      text-align: center;
      margin-bottom: 20px;
    }
    .placement-form {
      margin-top: 20px;
      padding: 15px;
      background-color: #f0f0f0;
      border-radius: 8px;
      text-align: center;
    }
    .placement-form label { margin-right: 10px; }
    .placement-form input[type="number"],
    .placement-form select {
      padding: 8px;
      margin-right: 10px;
      border-radius: 4px;
      border: 1px solid #ccc;
    }
    .placement-form button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .placement-form button:hover { background-color: #0056b3; }
  </style>
</head>
<body>
<div class="container">
  <h1>Ships Game</h1>
  <p class="game-info">
    Welcome, <%= loggedInUser.getUsername() %>!
    <br>Playing against: <span id="opponentUsername"><% if (opponentUser != null) { %><%= opponentUser.getUsername() %><% } else { %>Waiting...<% } %></span>
    <br>Game ID: <%= game.getId() %>
  </p>

  <% if (errorMessage != null) { %>
  <p class="error-message" id="errorMessage"><%= errorMessage %></p>
  <% } else { %>
  <p class="error-message" id="errorMessage" style="display:none;"></p>
  <% } %>

  <% if (feedbackMessage != null) { %>
  <p class="feedback-message" id="feedbackMessage"><%= feedbackMessage %></p>
  <% } else { %>
  <p class="feedback-message" id="feedbackMessage" style="display:none;"></p>
  <% } %>

  <p class="game-info" id="gameStatusMessage">
    <% if (game.isGameOver()) { %>
    <span class="game-over-message"><%= gameStatusMessage %></span>
    <% } else { %>
    <%= gameStatusMessage %>
    <% } %>
  </p>

  <%-- Ship Placement Form --%>
  <div class="placement-form" id="placementForm" <%= needsToPlaceShips && !game.isGameOver() ? "" : "style=\"display:none;\"" %>>
    <h2>Place Your Ships (<span id="shipsPlacedCount"><%= shipsPlacedCount %></span> / 2)</h2>
    <p id="placementInstructions">
      <% if (shipsPlacedCount == 0) { %>
      Place your first 2-segment ship.
      <% } else if (shipsPlacedCount == 1) { %>
      Place your second 2-segment ship.
      <% } else { %>
      All ships placed.
      <% } %>
    </p>
    <p>Enter the start (X,Y) coordinate. The ship will extend 1 unit to the right (Horizontal) or down (Vertical).</p>

    <form action="game" method="post">
      <input type="hidden" name="action" value="place_ship">
      <label for="startX">Start X:</label>
      <input type="number" id="startX" name="startX" min="0" max="9" required>
      <label for="startY">Start Y:</label>
      <input type="number" id="startY" name="startY" min="0" max="9" required>
      <label for="orientation">Orientation:</label>
      <select id="orientation" name="orientation" required>
        <option value="HORIZONTAL">Horizontal</option>
        <option value="VERTICAL">Vertical</option>
      </select>
      <button type="submit">Place Ship</button>
    </form>
  </div>


  <div class="game-boards">
    <div class="board player-board">
      <h2>Your Board (<%= loggedInUser.getUsername() %>)</h2>
      <div class="grid-container" id="playerBoardGrid">
        <% for (int y = 0; y < 10; y++) { %>
        <% for (int x = 0; x < 10; x++) { %>
        <div class="grid-cell <%=
                                (playerBoard[y][x] == 1 ? "player-ship" :
                                (playerBoard[y][x] == 2 ? "player-miss" :
                                (playerBoard[y][x] == 3 ? "player-hit" :
                                (playerBoard[y][x] == 4 ? "player-sunk" : ""))))
                            %>">
        </div>
        <% } %>
        <% } %>
      </div>
    </div>

    <div class="board opponent-board">
      <h2>Opponent's Board <span id="opponentNameDisplay"><% if (opponentUser != null) { %>(<%= opponentUser.getUsername() %>)<% } else { %>(No Opponent)<% } %></span></h2>
      <div class="grid-container" id="opponentBoardGrid">
        <% for (int y = 0; y < 10; y++) { %>
        <% for (int x = 0; x < 10; x++) { %>
        <%
          String cellClass = "grid-cell ";
          int cellState = opponentBoard[y][x]; // 0: water, 1: miss, 2: hit
          if (cellState == 1) {
            cellClass += "opponent-miss";
          } else if (cellState == 2) {
            cellClass += "opponent-hit";
          }

          boolean isDisabled = true; // Initially disabled by default
          if (!game.isGameOver() && game.isGameInProgress() && game.getCurrentTurnPlayerId() != null && game.getCurrentTurnPlayerId().equals(userId) && cellState == 0) {
            isDisabled = false; // Enable if it's current player's turn and cell hasn't been shot yet
          }
        %>
        <form action="game" method="post" style="width: 100%; height: 100%; display: flex;">
          <input type="hidden" name="action" value="fire_shot">
          <input type="hidden" name="targetX" value="<%= x %>">
          <input type="hidden" name="targetY" value="<%= y %>">
          <button type="submit" class="grid-cell grid-cell-button <%= cellClass %>" data-x="<%= x %>" data-y="<%= y %>" <%= isDisabled ? "disabled" : "" %>
                  title="
                    <% if (game.isGameOver()) { %>
                        Game Over
                    <% } else if (game.isGameWaiting() || needsToPlaceShips) { %>
                        Waiting for game to start or ships to be placed
                    <% } else if (game.getCurrentTurnPlayerId() != null && !game.getCurrentTurnPlayerId().equals(userId)) { %>
                        Not your turn
                    <% } else if (cellState != 0) { %>
                        Already shot here
                    <% } else { %>
                        Click to fire
                    <% } %>
                "
          >
          </button>
        </form>
        <% } %>
        <% } %>
      </div>
    </div>
  </div>

  <div class="game-actions">
    <% // Only allow reset if game is full (meaning it has been played or could be played) or is explicitly over.
      if (game.isGameFull() || game.isGameOver()) { %>
    <form action="game" method="post" onsubmit="return confirm('Are you sure you want to reset the game? This will clear all progress and allow new players to join.');">
      <input type="hidden" name="action" value="reset_game">
      <button type="submit" class="reset-button">Reset Game</button>
    </form>
    <% } %>
  </div>

  <p class="back-to-dashboard"><a href="dashboard">Back to Dashboard</a></p>
</div>

<script>
  // --- Initial Data from JSP ---
  var currentLoggedInUserId = <%= loggedInUser.getId() %>;
  var currentGameId = <%= game.getId() %>;
  var initialGameStatus = "<%= game.getStatus() %>";
  var initialNeedsToPlaceShips = <%= needsToPlaceShips %>;
  var initialPlayer1Id = <%= game.getPlayer1Id() %>;
  var initialPlayer2Id = <%= game.getPlayer2Id() != null ? game.getPlayer2Id() : "null" %>;

  // --- Helper function to render a board ---
  function renderBoard(boardData, boardElementId, isOpponentBoard, currentTurnPlayerId, needsToPlaceShips, isGameOver) {
    const gridContainer = $('#' + boardElementId);
    gridContainer.empty(); // Clear existing cells

    for (let y = 0; y < 10; y++) {
      for (let x = 0; x < 10; x++) {
        const cellValue = boardData[y][x];
        let cellClass = '';
        let buttonDisabled = true;
        let buttonTitle = ''; // Title for tooltip

        if (isOpponentBoard) {
          // Opponent's board (from current player's perspective)
          // 0: undiscovered water, 1: player fired - miss, 2: player fired - hit
          if (cellValue === 1) {
            cellClass = 'opponent-miss';
            buttonTitle = 'Missed shot';
          } else if (cellValue === 2) {
            cellClass = 'opponent-hit';
            buttonTitle = 'Hit opponent\'s ship!';
          } else { // cellValue === 0 (undiscovered water)
            if (isGameOver) {
              buttonTitle = 'Game Over';
            } else if (needsToPlaceShips) {
              buttonTitle = 'Place your ships first';
            } else if (currentTurnPlayerId !== currentLoggedInUserId) {
              buttonTitle = 'Not your turn';
            } else {
              buttonDisabled = false; // Enable if it's current player's turn and not shot yet
              buttonTitle = 'Click to fire';
            }
          }

          const form = $('<form action="game" method="post" style="width: 100%; height: 100%; display: flex;"></form>');
          form.append('<input type="hidden" name="action" value="fire_shot">');
          form.append('<input type="hidden" name="targetX" value="' + y + '">');
          form.append('<input type="hidden" name="targetY" value="' + x + '">');
          const button = $('<button type="submit" class="grid-cell grid-cell-button ' + cellClass + '" data-x="' + x + '" data-y="' + y + '" title="' + buttonTitle + '"></button>');

          if (buttonDisabled) {
            button.prop('disabled', true);
          }
          form.append(button);
          gridContainer.append(form);

        } else {
          // Player's board
          // 0: empty water, 1: player ship, 2: opponent shot - miss, 3: opponent shot - hit, 4: player ship - sunk
          if (cellValue === 1) {
            cellClass = 'player-ship';
          } else if (cellValue === 2) {
            cellClass = 'player-miss';
          } else if (cellValue === 3) {
            cellClass = 'player-hit';
          } else if (cellValue === 4) {
            cellClass = 'player-sunk';
          }
          gridContainer.append('<div class="grid-cell ' + cellClass + '"></div>');
        }
      }
    }
  }

  // --- Polling Logic ---
  let pollIntervalId; // Store the interval ID to clear it later

  function pollGameUpdate() {
    $.ajax({
      url: 'game-update', // New endpoint for in-game updates
      type: 'GET',
      data: { gameId: currentGameId },
      dataType: 'json',
      success: function(response) {
        if (!response.gameExists) {
          console.log("Game no longer exists or user is not in it. Stopping polling.");
          clearInterval(pollIntervalId);
          $('#errorMessage').text("Game is no longer active or you are not part of it. Returning to dashboard.").show();
          setTimeout(function() {
            window.location.href = 'dashboard';
          }, 3000); // Redirect after a short delay
          return;
        }

        // Update Opponent Username display
        const opponentUsername = response.opponentUsername !== "Opponent" ? response.opponentUsername : (response.player2Username !== "Player 2" ? response.player2Username : 'Waiting...');
        $('#opponentUsername').text(opponentUsername);
        $('#opponentNameDisplay').text('(' + opponentUsername + ')');


        // Update Game Status Message
        let statusMessage = '';
        const gameStatus = response.status;
        const currentTurnPlayerId = response.currentTurnPlayerId;
        const winnerId = response.winnerId;
        const needsToPlaceShips = response.needsToPlaceShips;

        if (gameStatus === 'PLAYER1_WON' || gameStatus === 'PLAYER2_WON') {
          clearInterval(pollIntervalId); // Stop polling if game is over
          if (winnerId === currentLoggedInUserId) {
            statusMessage = "Congratulations! You won the game!";
            $('#gameStatusMessage').html('<span class="game-over-message">' + statusMessage + '</span>');
          } else {
            statusMessage = response.opponentUsername + " won the game. You lost!";
            $('#gameStatusMessage').html('<span class="game-over-message">' + statusMessage + '</span>');
          }
        } else if (gameStatus === 'WAITING_FOR_PLAYER') {
          statusMessage = "Waiting for an opponent to join...";
        } else if (gameStatus === 'IN_PROGRESS') {
          if (needsToPlaceShips) {
            statusMessage = "Place your remaining ships!";
          } else if (currentTurnPlayerId === currentLoggedInUserId) {
            statusMessage = "It's your turn!";
          } else {
            statusMessage = "Waiting for " + opponentUsername + "'s turn.";
          }
        }
        $('#gameStatusMessage').text(statusMessage);


        // Show/Hide Ship Placement Form
        if (needsToPlaceShips && !(gameStatus === 'PLAYER1_WON' || gameStatus === 'PLAYER2_WON')) {
          $('#placementForm').show();
          $('#shipsPlacedCount').text(response.shipsPlacedCount);
          if (response.shipsPlacedCount === 0) {
            $('#placementInstructions').text('Place your first 2-segment ship.');
          } else if (response.shipsPlacedCount === 1) {
            $('#placementInstructions').text('Place your second 2-segment ship.');
          } else {
            $('#placementInstructions').text('All ships placed.');
          }
        } else {
          $('#placementForm').hide();
        }

        // Render Boards
        renderBoard(response.playerBoard, 'playerBoardGrid', false, currentTurnPlayerId, needsToPlaceShips, (gameStatus === 'PLAYER1_WON' || gameStatus === 'PLAYER2_WON'));
        renderBoard(response.opponentBoard, 'opponentBoardGrid', true, currentTurnPlayerId, needsToPlaceShips, (gameStatus === 'PLAYER1_WON' || gameStatus === 'PLAYER2_WON'));

        // Clear feedback/error messages after a delay if not critical
        // For polling, feedback messages are usually handled on the server side after a POST.
        // If you want dynamic messages, you would need to include them in the JSON response
        // for GameUpdateController. For now, assume they are set on initial page load after POST.
        if ($('#feedbackMessage').text().length > 0 && !(gameStatus === 'PLAYER1_WON' || gameStatus === 'PLAYER2_WON')) {
          setTimeout(function() {
            $('#feedbackMessage').fadeOut('slow', function() { $(this).text('').hide(); });
          }, 5000);
        }
        if ($('#errorMessage').text().length > 0 && !(gameStatus === 'PLAYER1_WON' || gameStatus === 'PLAYER2_WON')) {
          setTimeout(function() {
            $('#errorMessage').fadeOut('slow', function() { $(this).text('').hide(); });
          }, 5000);
        }

      },
      error: function(xhr, status, error) {
        console.error("Polling error:", status, error);
        // Display a persistent error message if polling fails repeatedly
        $('#errorMessage').text("Connection lost or server error. Please refresh. " + error).show();
        clearInterval(pollIntervalId); // Stop polling on major error
      }
    });
  }

  $(document).ready(function() {
    // Start polling immediately when the page loads, regardless of initial status
    // The pollGameUpdate function will handle stopping based on game status
    pollIntervalId = setInterval(pollGameUpdate, 2000); // Poll every 2 seconds

    // Initial render of boards (though JSP already does this, this ensures consistency)
    // and dynamic elements in case JS loads after initial JSP render.
    // We will call pollGameUpdate once immediately to get the fresh state.
    pollGameUpdate();
  });
</script>
</body>
</html>