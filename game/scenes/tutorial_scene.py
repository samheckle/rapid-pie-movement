import pygame
from . import *

class TutorialScene(BaseScene):
    def __init__(self, context):
        # Create scene and make transparent box over the 'x'
        BaseScene.__init__(self, context)
        self.btn = pygame.Surface((50,50), pygame.SRCALPHA, 32)
        self.btn.convert_alpha()
        context.screen.blit(self.context.tutorial, (0,0))
        self.b = context.screen.blit(self.btn, (1120,25))

    def handle_inputs(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.context.scene = TitleScene(self.context)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.b.collidepoint(pos):
                    self.context.scene = TitleScene(self.context)

    def render_scene(self):
        pygame.display.flip()
