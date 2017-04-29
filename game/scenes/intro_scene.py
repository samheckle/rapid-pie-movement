import pygame
from . import *

class IntroScene(BaseScene):
    def __init__(self, context, scene_num=1):
        BaseScene.__init__(self, context)
        self.scene_num = scene_num
        self.context.screen.blit(self.get_scene_bg(scene_num), (0,0))

    def handle_inputs(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.scene_num > 4:
                        # TODO Show Game scene
                        print 'invalid'
                    else:
                        self.scene_num = self.scene_num + 1
                        if self.scene_num <= 4:
                            self.context.screen.blit(self.get_scene_bg(self.scene_num), (0,0))
                if event.key == pygame.K_LEFT:
                    if self.scene_num != 1:
                        self.scene_num = self.scene_num - 1
                        self.context.screen.blit(self.get_scene_bg(self.scene_num), (0,0))
                    elif self.scene_num == 1:
                        self.context.set_title() 

    def get_scene_bg(self, num):
        if num == 1:
            return self.context.intro_1
        elif num == 2:
            return self.context.intro_2
        elif num == 3:
            return self.context.intro_3
        elif num == 4:
            return self.context.intro_4

    def render_scene(self):
        pygame.display.flip()

    def get_scene_bg(self, num):
        if num == 1:
            return self.context.intro_1
        elif num == 2:
            return self.context.intro_2
        elif num == 3:
            return self.context.intro_3
        elif num == 4:
            return self.context.intro_4
