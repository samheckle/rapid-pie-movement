import pygame
import cProfile
import os 

class RapidPieMovementGame:
    def __init__(self):
        self.base_path = os.path.dirname(__file__)

        self.clock = pygame.time.Clock()
        self.width = 1200
        self.height = 900
        self.fps = 30
        self.caption = "Rapid Pie Movement"
        self.load_assets()

    def load_assets(self):
        self.font_path = os.path.join(self.base_path, "game/assets/fonts/Questrial-Regular.ttf")
        self.background = self.load_image("background.png")
        self.applepie = self.load_image("applepie.png")
        self.bananacreampie = self.load_image("bananacreampie.png")
        self.blueberrypie = self.load_image("blueberrypie.png")
        self.caterer = self.load_image("Caterer.png")
        self.cherrypie = self.load_image("cherrypie.png")
        self.keylimepie = self.load_image("keylimepie.png")
        self.howtobtn = self.load_image("howtobn.png")
        self.title = self.load_image("title.png")

    def load_image(self, path):
        return pygame.image.load(os.path.join(self.base_path, "game/assets/images/"+path))

    def main_loop(self):
        self.running = True

        screen = pygame.display.get_surface()
        pygame.display.set_caption(self.caption)
        while self.running:
            for event in pygame.event.get():
                # Break out of loop on QUIT
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print 'PRESSED ESCAPE!'

            screen.blit(self.title,(0,0))
            pygame.display.flip()
            self.clock.tick(self.fps) 

def main():
    pygame.init()

    # Set display to size of OLPC (1200X900)
    pygame.display.set_mode((1200,900), pygame.RESIZABLE)
    game_inst = RapidPieMovementGame()
    game_inst.main_loop()

if __name__ == '__main__':
    main()

