import pygame
import traceback
import os

from . import scenes

class RapidPieMovementGame():
    def __init__(self):
        # Sets basePath to directory this file is in
        self.basePath = os.path.dirname(__file__)

        self.width = 1200
        self.height = 900
        self.fps = 20
        self.title = "Rapid Pie Movement"

    def load_assets(self):
        self.font_path = os.path.join(self.basePath, "assets/fonts/Questrial-Regular.ttf")
        self.background = self.load_image("background.png")
        self.applepie = self.load_image("applepie.png")
        self.bananacreampie = self.load_image("bananacreampie.png")
        self.blueberrypie = self.load_image("blueberrypie.png")
        self.caterer = self.load_image("Caterer.png")
        self.cherrypie = self.load_image("cherrypie.png")
        self.keylimepie = self.load_image("keylimepie.png")
        
    def load_image(self, path):
        return pygame.image.load(os.path.join(self.basePath,"assets/images/"+path))

    def loop(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.font = pygame.font.Font(self.font_path, 72)
        pygame.display.set_caption(self.title)
        
        self.start_scene = scenes.HomeScene
        self.active_scene = self.start_scene(self)

        while self.active_scene is not None:
            pressed_keys = pygame.key.get_pressed()
            events = []
            for event in pygame.event.get():
                events.append(event)

            self.active_scene.ProcessInput(events, pressed_keys)
            self.active_scene.Update()
            self.active_scene.Render()

            self.active_scene = self.active_scene.next
            self.clock.tick(self.fps)

    def run(self):
        self.loop()
        
