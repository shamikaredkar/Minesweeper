import pygame
from settings import *
from sprites import *

class Game:
    
    #Constructor creates the window, sets the title, creates a clock
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
    
    #Creates a new game
    def new(self):
        self.board = Board()
        self.board.display_board()
    
    #The game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
    
    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.board.draw(self.screen)
        pygame.display.flip()
    
    #mouse click eventsa
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                #We want to check which tile we're clicking
                mx //= TILESIZE #gives exact location of each of the tile
                my //= TILESIZE
                
                if event.button == 1:
                    if not self.board.board_list[my][mx].flagged:
                    # DIG and check if exploded
                        if not self.board.dig(my,mx): 
                            #explode
                            for row in self.board.board_list:
                                for tile in row:
                                    if tile.flagged and tile.type != "X":
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = tile_not_mine
                                    elif tile.type == "X":
                                        tile.revealed = True
                            self.playing = False
                if event.button == 3:
                # if its not revealed then we can add the flag
                    if not self.board.board_list[my][mx].revealed:
                        self.board.board_list[my][mx].flagged = not self.board.board_list[my][mx].flagged
                
game = Game()
while True:
    game.new()
    game.run()