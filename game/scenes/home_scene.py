import pygame 
from .parent_scene import ParentScene

class HomeScene(ParentScene):
    def __init__(self, context):
        ParentScene.__init__(self, context)
        self.buttons = []
        self.static_surface = pygame.Surface((self.context.width, self.context.height), pygame.SRCALPHA)
        self.static_surface.blit(self.context.background, (0,0))

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.isClicked(event)

    def Update(self):
        pass

    def Render(self):
        self.screen.blit(self.static_surface,(0,0))
        pygame.display.update()

