import pygame
import cProfile
import os 
import game.scenes as scenes

class RapidPieMovementGame:
    def __init__(self):
        self.base_path = os.path.dirname(__file__)

        self.clock = pygame.time.Clock()
        self.width = 1200
        self.height = 900
        self.fps = 15
        self.caption = "Rapid Pie Movement"
        self.title_scene = scenes.TitleScene
        self.load_assets()

    def load_assets(self):
        font_path = os.path.join(self.base_path, "game/assets/fonts/Questrial-Regular.ttf")
        self.font = pygame.font.Font(font_path, 27, bold=True)
        self.fontbig = pygame.font.Font(font_path, 40, bold=True)
        self.background = self.load_image("bg1.png")
        self.applepie = self.load_image("applepie.png")
        self.bananacreampie = self.load_image("bananacreampie.png")
        self.blueberrypie = self.load_image("blueberrypie.png")
        self.caterer = self.load_image("Caterer.png")
        self.cherrypie = self.load_image("cherrypie.png")
        self.keylimepie = self.load_image("keylimepie.png")
        self.howtobtn = self.load_image("howtobn.png")
        self.startbtn = self.load_image("startbtn.png")
        self.title = self.load_image("title.png")
        self.tutorial = pygame.transform.scale(self.load_image("tutorial.png"), (1200,900))
        self.intro_1 = self.load_image("intro_1.png")
        self.intro_2 = self.load_image("intro_2.png")
        self.intro_3 = self.load_image("intro_3.png")
        self.intro_4 = self.load_image("intro_4.png")
        self.btn_bg = self.load_image("numbtn.png")
        self.lvl2_bg = pygame.transform.scale(self.load_image("level2btn.png"), (201,73))
        self.lvl3_bg = pygame.transform.scale(self.load_image("level3btn.png"), (201,73))
        self.pies_lst = [self.applepie, self.bananacreampie, self.blueberrypie, self.cherrypie, self.keylimepie]

    def load_image(self, path):
        return pygame.image.load(os.path.join(self.base_path, "game/assets/images/"+path))

    def main_loop(self):
        self.running = True
        self.screen = pygame.display.get_surface()
        self.scene = scenes.TitleScene(self)
        pygame.display.set_caption(self.caption)
        while self.running:
            self.scene.handle_inputs(pygame.event.get())
            self.scene.render_scene()
            self.clock.tick(self.fps) 

    def set_intro(self):
        self.scene = scenes.IntroScene(self)

    def set_title(self):
        self.scene = scenes.TitleScene(self)

    def set_tutorial(self):
        self.scene = scenes.TutorialScene(self)

    def set_game(self):
        self.scene = scenes.GameScene(self)


def main():
    pygame.init()

    # Set display to size of OLPC (1200X900)
    pygame.display.set_mode((1200,900), pygame.RESIZABLE)
    game_inst = RapidPieMovementGame()
    game_inst.main_loop()

if __name__ == '__main__':
    main()

