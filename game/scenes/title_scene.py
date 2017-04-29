import pygame
from . import *

class TitleScene(BaseScene):
    """
    You can access all items in RapidPieMovementGame by doing
    self.context.<item>
    """
    def __init__(self, context):
        BaseScene.__init__(self, context)
        self.context.screen.blit(self.context.title,(0,0))
        self.create_buttons()

    def handle_inputs(self, events):
        # Handle events
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.start_box.collidepoint(pos):
                    self.context.scene = GameScene(self.context)

                elif self.help_box.collidepoint(pos):
                    self.context.set_tutorial()

    def create_buttons(self):
        self.start_btn = pygame.Surface((436,104), pygame.SRCALPHA, 32)
        self.start_btn.convert_alpha()
        self.start_btn.blit(self.context.startbtn, (0,0))
        self.start_box = self.context.screen.blit(self.start_btn, (400,500))

        self.tut_btn = pygame.Surface((436,104), pygame.SRCALPHA, 32)
        self.tut_btn.convert_alpha()
        self.tut_btn.blit(self.context.howtobtn, (0,0))
        self.help_box = self.context.screen.blit(self.tut_btn, (400, 700))
            
    def render_scene(self):
        pygame.display.flip()
