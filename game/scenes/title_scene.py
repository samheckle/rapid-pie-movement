import pygame
from . import *

class TitleScene(BaseScene):
    """
    You can access all items in RapidPieMovementGame by doing
    self.context.<item>
    """
    def __init__(self, context):
        BaseScene.__init__(self, context)

    def handle_inputs(self, events):
        # Handle events
        for event in events:
            pass
            
    def render_scene(self):
        self.context.screen.blit(self.context.title,(0,0))
        pygame.display.flip()
