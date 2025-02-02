# Nine Men's Morris Game

## 🎮 Overview

This project implements a console-based version of **Nine Men's Morris**, a two-player strategy board game, using **Python**. One of the players is a **human**, while the other is an **AI** player. The AI is designed to challenge the human player by prioritizing the following strategies:
1. Completing its own mills.
2. Sabotaging the player's potential mills.
3. Blocking the player when possible.

The game leverages **Object-Oriented Programming (OOP)** principles to design its components. It aims to explore Python's flexibility in structuring the game logic, contrasting it with the more rigid structure of languages like **C++**.

This project was developed as part of an **university assignment**, aimed at applying fundamental programming concepts to build a functional game.

## 🌟 Features

- **AI Player**: The AI uses a simple **heuristic-based** decision-making strategy that prioritizes:
  1. Completing its own mills.
  2. Preventing the player from forming mills.
  3. Blocking the player's potential moves when possible.

- **Human Player**: A user can play against the AI in the console.

- **Game Phases**:
  1. **Placing pieces**: Players place pieces alternately on the board.
  2. **Moving pieces**: Once all pieces are placed, players take turns moving them to adjacent positions.
  3. **Jumping**: When a player has fewer than 3 pieces, they can "jump" to any empty spot on the board.

- **Board Display**: The board is displayed in a text-based format, with pieces represented as ‘w’ (player) and ‘b’ (AI).

- **Winning Condition**: The game ends when a player reduces the opponent to two pieces or when the opponent is unable to make a valid move.



