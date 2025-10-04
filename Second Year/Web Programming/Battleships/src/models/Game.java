package models;

import java.io.Serial;
import java.io.Serializable;

public class Game implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    private int id; // The ID of the single active game row
    private Integer player1Id; // Use Integer to allow null
    private Integer player2Id; // Use Integer to allow null
    private String status; // e.g., "WAITING_FOR_PLAYER", "IN_PROGRESS", "COMPLETED"
    private Integer currentTurnPlayerId; // Player whose turn it is
    private Integer winnerId; // Player who won the game, null if not yet decided

    public Game() {
        // Default constructor
    }

    public Game(int id, Integer player1Id, Integer player2Id, String status, Integer currentTurnPlayerId, Integer winnerId) {
        this.id = id;
        this.player1Id = player1Id;
        this.player2Id = player2Id;
        this.status = status;
        this.currentTurnPlayerId = currentTurnPlayerId;
        this.winnerId = winnerId;
    }

    // Getters and Setters for all fields

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Integer getPlayer1Id() {
        return player1Id;
    }

    public void setPlayer1Id(Integer player1Id) {
        this.player1Id = player1Id;
    }

    public Integer getPlayer2Id() {
        return player2Id;
    }

    public void setPlayer2Id(Integer player2Id) {
        this.player2Id = player2Id;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Integer getCurrentTurnPlayerId() {
        return currentTurnPlayerId;
    }

    public void setCurrentTurnPlayerId(Integer currentTurnPlayerId) {
        this.currentTurnPlayerId = currentTurnPlayerId;
    }

    public Integer getWinnerId() {
        return winnerId;
    }

    public void setWinnerId(Integer winnerId) {
        this.winnerId = winnerId;
    }

    public boolean isPlayerInGame(int userId) {
        return (player1Id != null && player1Id.equals(userId)) ||
                (player2Id != null && player2Id.equals(userId));
    }

    public boolean isGameFull() {
        return player1Id != null && player2Id != null;
    }

    public boolean isGameWaiting() {
        // A game is waiting if its status is "WAITING_FOR_PLAYER"
        // AND it has space for at least one more player (i.e., player1_id OR player2_id is null)
        // or both are null for a brand new game.
        return "WAITING_FOR_PLAYER".equals(status) && (player1Id == null || player2Id == null);
    }

    public boolean isGameInProgress() {
        return "IN_PROGRESS".equals(status);
    }

    public boolean isGameOver() {
        return "PLAYER1_WON".equals(status) || "PLAYER2_WON".equals(status);
    }
}