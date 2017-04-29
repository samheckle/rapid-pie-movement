import pygame
import random
from . import *

class GameScene(BaseScene):
    def __init__(self, context):
        BaseScene.__init__(self, context)
        self.level = 1
        self.correct = False
        self.leveltxt = ["Into how many pieces should we cut these 2 pies to get 12 slices?", "Into how many pieces should we cut these 3 pies to get 15 slices?", "Into how many pieces should we cut these 4 pies to get 32 slices?"]
        self.draw_scene()

    def draw_scene(self):
        self.context.screen.blit(self.context.background, (0,0))
        self.context.screen.blit(self.context.caterer, (750,100))
        
        if self.correct:
            text = self.context.font.render("CORRECT!", 1, (102,255,102))
        else:
            text = self.context.font.render(self.leveltxt[self.level-1], 1, (255,255,255))
        self.context.screen.blit(text, (20, 750))
        self.draw_pies()
        self.draw_btns()

    def draw_pies(self):
        pies = self.context.pies_lst 
        if self.level == 1:
            self.context.screen.blit(random.choice(pies), (20,480))
            self.context.screen.blit(random.choice(pies), (220,480))
        elif self.level == 2:
            self.context.screen.blit(random.choice(pies), (20,480))
            self.context.screen.blit(random.choice(pies), (220,480))
            self.context.screen.blit(random.choice(pies), (420,480))
        elif self.level == 3:
            self.context.screen.blit(random.choice(pies), (20,480))
            self.context.screen.blit(random.choice(pies), (220,480))
            self.context.screen.blit(random.choice(pies), (420,480))
            self.context.screen.blit(random.choice(pies), (620,480))

    def draw_btns(self):
        if self.level == 1:
            self.btn1 = pygame.Surface((201,73), pygame.SRCALPHA, 32)
            self.btn1.convert_alpha()
            self.btn1.blit(self.context.btn_bg, (0,0))
            text = self.context.fontbig.render("4", 1, (255,255,255))
            self.btn1.blit(text, (90,20))
            self.context.screen.blit(self.btn1, (20, 820))

            self.ansbtn = pygame.Surface((201,73), pygame.SRCALPHA, 32)
            self.ansbtn.convert_alpha()
            self.ansbtn.blit(self.context.btn_bg, (0,0))
            text = self.context.fontbig.render("6", 1, (255,255,255))
            self.ansbtn.blit(text, (90,20))
            self.context.screen.blit(self.ansbtn, (250, 820))
            
            self.btn3 = pygame.Surface((201,73), pygame.SRCALPHA, 32)
            self.btn3.convert_alpha()
            self.btn3.blit(self.context.btn_bg, (0,0))
            text = self.context.fontbig.render("8", 1, (255,255,255))
            self.btn3.blit(text, (90,20))
            self.context.screen.blit(self.btn3, (480, 820))

    def handle_inputs(self, events):
        for event in events:
            pass

    def render_scene(self):
        pygame.display.flip()
