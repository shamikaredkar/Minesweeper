import pygame
from settings import *
from sprites import *

class Game:
    # Constructor initializes the game window, sets the title, and creates a clock
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window with specified dimensions
        pygame.display.set_caption(TITLE)  # Set the window title
        self.clock = pygame.time.Clock()  # Create a clock to control the frame rate

    # Creates a new game
    def new(self):
        self.board = Board()  # Initialize a new board
        self.board.display_board()  # Display the initial state of the board

    # The main game loop
    def run(self):
        self.playing = True  # Set the playing flag to True
        while self.playing:  # Run the game loop while the game is active
            self.clock.tick(FPS)  # Cap the frame rate to the specified FPS
            self.events()  # Handle events (like mouse clicks)
            self.draw()  # Draw the current game state
        else:
            self.end_screen()  # Display the end screen when the game loop exits

    # Draws the current game state
    def draw(self):
        self.screen.fill(BGCOLOUR)  # Fill the screen with the background color
        self.board.draw(self.screen)  # Draw the board on the screen
        pygame.display.flip()  # Update the display with the new frame

    # Checks if the player has won the game
    def check_win(self):
        for row in self.board.board_list:  # Iterate over each row in the board
            for tile in row:  # Iterate over each tile in the row
                if tile.type != "X" and not tile.revealed:  # If any non-mine tile is not revealed
                    return False  # The player has not won yet
        return True  # All non-mine tiles are revealed, the player has won

    # Handles events (like mouse clicks)
    def events(self):
        for event in pygame.event.get():  # Iterate over the event queue
            if event.type == pygame.QUIT:  # If the event is a quit event
                pygame.quit()  # Quit Pygame
                quit(0)  # Exit the program

            if event.type == pygame.MOUSEBUTTONDOWN:  # If the event is a mouse button down event
                mx, my = pygame.mouse.get_pos()  # Get the mouse click position
                mx //= TILESIZE  # Convert pixel position to tile position
                my //= TILESIZE  # Convert pixel position to tile position

                if event.button == 1:  # If the left mouse button was clicked
                    if not self.board.board_list[mx][my].flagged:  # If the clicked tile is not flagged
                        # Dig and check if exploded
                        if not self.board.dig(mx, my):  # If the dig did not explode
                            # Explode
                            for row in self.board.board_list:  # Iterate over each row in the board
                                for tile in row:  # Iterate over each tile in the row
                                    if tile.flagged and tile.type != "X":  # If a flagged tile is not a mine
                                        tile.flagged = False  # Remove the flag
                                        tile.revealed = True  # Reveal the tile
                                        tile.image = tile_not_mine  # Change the image to show it's not a mine
                                    elif tile.type == "X":  # If the tile is a mine
                                        tile.revealed = True  # Reveal the mine
                            self.playing = False  # End the game

                if event.button == 3:  # If the right mouse button was clicked
                    if not self.board.board_list[mx][my].revealed:  # If the clicked tile is not revealed
                        self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged  # Toggle the flag

                if self.check_win():  # Check if the player has won
                    self.win = True  # Set the win flag to True
                    self.playing = False  # End the game
                    for row in self.board.board_list:  # Iterate over each row in the board
                        for tile in row:  # Iterate over each tile in the row
                            if not tile.revealed:  # If the tile is not revealed
                                tile.flagged = True  # Flag the tile

    # Displays the end screen
    def end_screen(self):
        while True:  # Loop indefinitely
            for event in pygame.event.get():  # Iterate over the event queue
                if event.type == pygame.QUIT:  # If the event is a quit event
                    pygame.quit()  # Quit Pygame
                    quit(0)  # Exit the program

                if event.type == pygame.MOUSEBUTTONDOWN:  # If the event is a mouse button down event
                    return  # Exit the end screen loop and start a new game

game = Game()
while True:
    game.new()  # Start a new game
    game.run()  # Run the game

