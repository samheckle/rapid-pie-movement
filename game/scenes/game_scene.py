import pygame
import random
from . import *

class GameScene(BaseScene):
    def __init__(self, context):
        BaseScene.__init__(self, context)
        self.level = 1
        self.freeze = False
        self.correct_num = 0
        self.leveltxt = "Into how many pieces should we cut these {} pies to get {} slices?"
        self.btn_positions = [20,250,480]
        self.draw_scene()

    def draw_scene(self):
        self.context.screen.blit(self.context.background, (0,0))
        self.context.screen.blit(self.context.caterer, (750,100))
        self.get_vals()
        
        while self.slicenum % self.numpies != 0:
            self.get_vals()

        self.answer = self.slicenum / self.numpies
        text = self.context.font.render(self.leveltxt.format(self.numpies, self.slicenum), 1, (255,255,255))

        self.context.screen.blit(text, (20, 750))
        self.draw_pies() 
        self.draw_btns()

    def get_vals(self):
        if self.level <= 3:
            self.numpies = 2
            self.slicenum = random.randrange(2, 15, self.numpies)
        elif self.level > 3 and self.level < 10:
            self.numpies = random.randint(2,4)
            self.slicenum = random.randrange(2, 35, self.numpies)
        else:
            self.numpies = random.randint(3,4)
            self.slicenum = random.randrange(2, 60, self.numpies)

    def draw_pies(self):
        pies = self.context.pies_lst 
        startx = 20
        for x in range(self.numpies):
            self.context.screen.blit(random.choice(pies), (startx, 480))
            startx += 200

    def draw_btns(self):
        btn_pos = list(self.btn_positions)
        self.btn1_xpos = random.choice(btn_pos)
        btn_pos.remove(self.btn1_xpos)
        self.btn2_xpos = random.choice(btn_pos)
        btn_pos.remove(self.btn2_xpos)
        self.ansbtn_xpos = random.choice(btn_pos)
        lim = self.answer+10

        btn1_val = str(random.choice([i for i in range(1,lim) if i not in [self.answer]])) 
        btn2_val = str(random.choice([i for i in range(1,lim) if i not in [self.answer]])) 
        ans_val = str(self.answer)

        self.btn1 = pygame.Surface((201,73), pygame.SRCALPHA, 32)
        self.btn1.convert_alpha()
        self.btn1.blit(self.context.btn_bg, (0,0))
        text = self.context.fontbig.render(btn1_val, 1, (255,255,255))
        self.btn1.blit(text, (90,20))
        self.btn1_obj = self.context.screen.blit(self.btn1, (self.btn1_xpos, 820))

        self.ansbtn = pygame.Surface((201,73), pygame.SRCALPHA, 32)
        self.ansbtn.convert_alpha()
        self.ansbtn.blit(self.context.btn_bg, (0,0))
        text = self.context.fontbig.render(ans_val, 1, (255,255,255))
        self.ansbtn.blit(text, (90,20))
        self.ans_obj = self.context.screen.blit(self.ansbtn, (self.ansbtn_xpos, 820))
            
        self.btn3 = pygame.Surface((201,73), pygame.SRCALPHA, 32)
        self.btn3.convert_alpha()
        self.btn3.blit(self.context.btn_bg, (0,0))
        text = self.context.fontbig.render(btn2_val,1, (255,255,255))
        self.btn3.blit(text, (90,20))
        self.btn3_obj = self.context.screen.blit(self.btn3, (self.btn2_xpos, 820))
        self.arrow_box = None

    def handle_inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.ans_obj.collidepoint(pos) and not self.freeze:
                    self.freeze = True
                    self.remove_btns(self.btn1_xpos, self.btn2_xpos)
                    self.draw_correct()
                    
                    self.arrow_btn = pygame.Surface((27,29), pygame.SRCALPHA, 32)
                    self.arrow_btn.convert_alpha()
                    self.arrow_btn.blit(self.context.arrow, (0,0))
                    self.arrow_box = self.context.screen.blit(self.arrow_btn, (810,850))                  
                    self.correct_num += 1

                elif self.btn1_obj.collidepoint(pos) and not self.freeze:
                    self.freeze = True
                    self.remove_btns(self.ansbtn_xpos, self.btn2_xpos)
                    self.draw_incorrect()
                    self.arrow_btn = pygame.Surface((27,29), pygame.SRCALPHA, 32)
                    self.arrow_btn.convert_alpha()
                    self.arrow_btn.blit(self.context.arrow, (0,0))
                    self.arrow_box = self.context.screen.blit(self.arrow_btn, (810,850))                  

                elif self.btn3_obj.collidepoint(pos) and not self.freeze:
                    self.freeze = True
                    self.remove_btns(self.ansbtn_xpos, self.btn1_xpos)
                    self.draw_incorrect()
                    self.arrow_btn = pygame.Surface((27,29), pygame.SRCALPHA, 32)
                    self.arrow_btn.convert_alpha()
                    self.arrow_btn.blit(self.context.arrow, (0,0))
                    self.arrow_box = self.context.screen.blit(self.arrow_btn, (810,850))                  

                if self.arrow_box != None and self.arrow_box.collidepoint(pos):
                    self.freeze = False
                    self.level += 1
                    self.draw_scene()
                    
    def remove_btns(self, x1, x2):
        surf = pygame.Surface((201,73))
        surf.fill((255,255,255))
        self.context.screen.blit(surf, (x1, 820))
        self.context.screen.blit(surf, (x2, 820))

    def draw_incorrect(self):
        correct_surface = pygame.Surface((339,141), pygame.SRCALPHA, 32)
        correct_surface.convert_alpha()
        correct_surface.blit(self.context.smalltxtbubble, (0,0))
        text = self.context.font.render("INCORRECT", 1, (255,0,0))
        correct_surface.blit(text, (90,80))
        self.context.screen.blit(correct_surface, (520,100))

    def draw_correct(self):
        correct_surface = pygame.Surface((339,141), pygame.SRCALPHA, 32)
        correct_surface.convert_alpha()
        correct_surface.blit(self.context.smalltxtbubble, (0,0))
        text = self.context.font.render("CORRECT!", 1, (102,255,102))
        correct_surface.blit(text, (90,80))
        self.context.screen.blit(correct_surface, (520,100))
        
    def render_scene(self):
        pygame.display.flip()
