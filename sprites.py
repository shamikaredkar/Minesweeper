import pygame
from settings import *
import random

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
        board_surface.blit(self.image, (self.x, self.y))
    
    def __repr__(self):
        return self.type

class Board:
    def __init__(self):
        #Size of the board is the size of the window
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        #2D list containing tiles
        self.board_list = [[Tile(col, row, tile_empty, ".") for col in range(COLUMNS)] for row in range(ROWS)]

        self.placing_mines()
        self.place_clues()
        
    #Placing mines
    def placing_mines(self):
        for _ in range(AMOUNT_MINES):
            while True: 
                #If a mine already exists, we look for another random location and place the mine there
                
                #Generate a random location for the mine
                x = random.randint(0, ROWS - 1) #0-14
                y = random.randint(0, COLUMNS - 1) #0-14
                if self.board_list[x][y].type == ".":
                    self.board_list[x][y].image = tile_mine
                    self.board_list[x][y].type = 'X'
                    break
    def place_clues(self):
        for x in range(ROWS):
            for y in range(COLUMNS):
                if self.board_list[x][y].type != 'X':
                    total_mines = self.check_neighbors(x, y)
                    if total_mines > 0:
                        self.board_list[x][y].image = tile_numbers[total_mines - 1]
                        self.board_list[x][y].type == 'C'
    
    #Check if the neighbour square that we're checking is inside the board
    @staticmethod
    def is_inside(x, y):
        return 0 <= x < ROWS and 0 <= y < COLUMNS
    
    def check_neighbors(self, x, y):
        total_mines = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                neighbour_x = x + x_offset
                neighbour_y = y + y_offset
                if self.is_inside(neighbour_x, neighbour_y) and self.board_list[neighbour_x][neighbour_y].type == "X":
                    total_mines += 1
        return total_mines
                    
    
    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0,0))
    
    def display_board(self):
        for row in self.board_list:
            print(row)