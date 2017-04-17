import pygame
from game import RapidPieMovementGame 
import cProfile

def main():
    pygame.init()

    # Set display to size of OLPC (1200X900)
    pygame.display.set_mode((1200,900), pygame.RESIZABLE)
    game_inst = RapidPieMovementGame()
    game_inst.run()

if __name__ == '__main__':
    main()

