<!-- PROJECT LOGO -->
<br />
<div align="center">
    <h2>MINESWEEPER GAME - <a href="https://replit.com/@shamikaredkar/Minesweeper">Demo</a></h2>
    <br />
</div>
<!-- ABOUT THE PROJECT -->
<br />

<div align="center">
    <img src="https://github.com/shamikaredkar/Minesweeper/blob/main/MinesweeperPreview.gif" alt="Preview">
</div>

### About The Project
This project is a classic Minesweeper game implemented in Python using the Pygame library. The objective of the game is to clear a rectangular board containing hidden "mines" or bombs without detonating any of them, with help from clues about the number of neighboring mines in each field. You can flag a tile if you think it could have a mine under it.

Features:
* **Interactive Gameplay:** Click to reveal tiles and flag potential mines.
* **Win/Lose Conditions:** The game tracks whether you win by revealing all non-mine tiles or lose by clicking on a mine.
* **Responsive Design:** Adjusts to different screen sizes and resolutions.
* **Customizable Settings:** Change the number of rows, columns, and mines for varied difficulty.
* **Visual Feedback:** Different tiles have distinct graphics to indicate numbers, mines, and flags.

### Built With
* [![Python][Python]][Python-url]
* [![Pygame][Pygame]][Pygame-url]

### Project Directory

<!-- USAGE EXAMPLES -->
## Usage

### Gameplay

**Reveal Tiles:** Left-click on a tile to reveal what is underneath. If the tile is a mine, you lose the game.
**Flag Mines:** Right-click on a tile to flag it as a potential mine. This helps keep track of where you think the mines are located.
**Winning the Game:** Reveal all non-mine tiles to win the game.
**Losing the Game:** Click on a mine to lose the game. The board will reveal all mines and end the game.

### Game Settings
**Change Board Size:** Modify the number of rows, columns, and mines in the settings.py file for different difficulty levels. This allows for customizing the challenge to your preference.
**Timer:** The game includes a timer that starts as soon as you make your first move. Try to complete the game as quickly as possible to achieve a high score.

### Visual Feedback
**Tile Graphics:** Different tiles have distinct graphics to indicate whether they are empty, contain a number (indicating the count of neighboring mines), or are mines/flags.
**Game Over Screen:** When you lose the game, the board reveals all mines, and you can see where you went wrong.

###Run the Game: 

Start the game by running the main script.
```
python main.py
```


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[Pygame]: https://img.shields.io/badge/Pygame-3776AB?style=for-the-badge&logo=python&logoColor=white
[Pygame-url]: https://www.pygame.org/
