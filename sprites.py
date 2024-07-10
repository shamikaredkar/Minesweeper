import pygame
from settings import *

#Types list
# . -> unknown
# X mine -> mine
# C -> clue
# / -> empty


class Tile:
    #x,y:  position
    #type: form the types list
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        #x,y is the position on the board and we multiply that by TILESIZE to get the pixel
        self.x, self.y = x * TILESIZE, y * TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged
    
    #Draws the board
    def draw(self, board_surface):
        #board_surface is the destination surface where the tile_unknown will be drawn
        #blit() -- draws the tile_unkown on the board_surface
        board_surface.blit(tile_unknown, (self.x, self.y))
    
    def __repr__(self):
        return self.type

class Board:
    def __init__(self):
        #Size of the board is the size of the window
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        #2D list containing tiles
        self.board_list = [[Tile(col, row, tile_empty, ".")
                            for row in range(ROWS)] for col in range(COLUMNS)]
    
    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0,0))
    
    def display_board(self):
        for row in self.board_list:
            print(row)