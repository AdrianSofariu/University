package models; // Assuming your package is 'models' as per the snippet

import java.io.Serializable;

public class Ship implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;
    private int gameId;
    private int playerId; // Renamed from 'userId' to 'playerId' for consistency with game logic
    private int positionX1;
    private int positionY1;
    private int positionX2;
    private int positionY2;
    private boolean sunk;
    private int hits = 0;

    public Ship() {
        // Default constructor
    }

    // Constructor for creating a new ship (assuming 2-segment ships)
    public Ship(int gameId, int playerId, int positionX1, int positionY1, int positionX2, int positionY2) {
        this.gameId = gameId;
        this.playerId = playerId;
        this.positionX1 = positionX1;
        this.positionY1 = positionY1;
        this.positionX2 = positionX2;
        this.positionY2 = positionY2;
        this.sunk = false; // A new ship is never sunk
    }

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public int getGameId() { return gameId; }
    public void setGameId(int gameId) { this.gameId = gameId; }

    public int getPlayerId() { return playerId; }
    public void setPlayerId(int playerId) { this.playerId = playerId; }

    public int getPositionX1() { return positionX1; }
    public void setPositionX1(int positionX1) { this.positionX1 = positionX1; }

    public int getPositionY1() { return positionY1; }
    public void setPositionY1(int positionY1) { this.positionY1 = positionY1; }

    public int getPositionX2() { return positionX2; }
    public void setPositionX2(int positionX2) { this.positionX2 = positionX2; }

    public int getPositionY2() { return positionY2; }
    public void setPositionY2(int positionY2) { this.positionY2 = positionY2; }

    public boolean isSunk() { return sunk; }
    public void setSunk(boolean sunk) { this.sunk = sunk; }

    public int getHits() { return hits; }
    public void setHits(int hits) { this.hits = hits; }
    public void recordHit() {
        this.hits++;
        if (hits == 2) { // Assuming a 2-segment ship
            this.sunk = true;
        }
    }

    /**
     * Returns an array of coordinates (x, y) occupied by this 2-segment ship.
     * The order of (x1,y1) and (x2,y2) does not matter for calculation,
     * but they must define a valid 2-segment horizontal or vertical ship.
     *
     * @return A 2x2 array where rows are [x, y] coordinates.
     * For example, {{x1, y1}, {x2, y2}}.
     */
    public int[][] getCoordinates() {
        int[][] coords = new int[2][2];
        coords[0][0] = positionX1;
        coords[0][1] = positionY1;
        coords[1][0] = positionX2;
        coords[1][1] = positionY2;
        return coords;
    }

    /**
     * Determines if the ship is horizontal or vertical based on its coordinates.
     * Assumes a valid 2-segment straight ship.
     *
     * @return "HORIZONTAL" or "VERTICAL"
     */
    public String getOrientation() {
        if (positionY1 == positionY2 && Math.abs(positionX1 - positionX2) == 1) {
            return "HORIZONTAL";
        } else if (positionX1 == positionX2 && Math.abs(positionY1 - positionY2) == 1) {
            return "VERTICAL";
        }
        // This should not happen with valid ship placement, but good for defensive programming
        return "INVALID";
    }

    /**
     * Returns the size of the ship. Fixed at 2 for this game.
     */
    public int getSize() {
        return 2;
    }

    /**
     * Checks if a given coordinate (x, y) hits this ship.
     *
     * @param x The x-coordinate of the shot.
     * @param y The y-coordinate of the shot.
     * @return true if the shot hits any segment of the ship, false otherwise.
     */
    public boolean containsCoordinate(int x, int y) {
        return (x == positionX1 && y == positionY1) || (x == positionX2 && y == positionY2);
    }
}