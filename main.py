import pygame
from settings import *
from sprites import *

class Game:
    
    #Constructor creates the window, sets the title, creates a clock
    def __init__(self) -> None:
        self.screen = pygame.display.set_node(WIDTH, HEIGHT)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
    
    #Creates a new game
    def new(self):
        pass
    
    #The game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
    
    def draw(self):
        self.screen.fill(BGCOLOUR)
        pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
game = Game()
while True:
    game.new()
    game.run()