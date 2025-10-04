// src/main/java/models/Shot.java
package models;

import java.io.Serial;
import java.io.Serializable;
import java.sql.Timestamp;

public class Shot implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    private int id;
    private int gameId;
    private int firingPlayerId;
    private int targetPlayerId;
    private int x; // X-coordinate of the shot
    private int y; // Y-coordinate of the shot
    private boolean hit; // True if it was a hit, false if a miss

    public Shot() {}

    public Shot(int gameId, int firingPlayerId, int targetPlayerId, int x, int y, boolean hit) {
        this.gameId = gameId;
        this.firingPlayerId = firingPlayerId;
        this.targetPlayerId = targetPlayerId;
        this.x = x;
        this.y = y;
        this.hit = hit;
        // shotTime will be set by the database
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getGameId() {
        return gameId;
    }

    public void setGameId(int gameId) {
        this.gameId = gameId;
    }

    public int getFiringPlayerId() {
        return firingPlayerId;
    }

    public void setFiringPlayerId(int firingPlayerId) {
        this.firingPlayerId = firingPlayerId;
    }

    public int getTargetPlayerId() {
        return targetPlayerId;
    }

    public void setTargetPlayerId(int targetPlayerId) {
        this.targetPlayerId = targetPlayerId;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public boolean isHit() {
        return hit;
    }

    public void setHit(boolean hit) {
        this.hit = hit;
    }
}