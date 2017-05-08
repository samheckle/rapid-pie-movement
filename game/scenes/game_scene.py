import pygame
import random
from . import *

class GameScene(BaseScene):
    def __init__(self, context):
        BaseScene.__init__(self, context)
        self.level = 1
        self.correct = False
        self.leveltxt = "Into how many pieces should we cut these {} pies to get {} slices?"
        self.btn_positions = [20,250,480]
        self.draw_scene()

    def draw_scene(self):
        self.context.screen.blit(self.context.background, (0,0))
        self.context.screen.blit(self.context.caterer, (750,100))
         
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
        btn_pos = list(self.btn_positions)
        self.btn1_xpos = random.choice(btn_pos)
        btn_pos.remove(self.btn1_xpos)
        self.btn2_xpos = random.choice(btn_pos)
        btn_pos.remove(self.btn2_xpos)
        ansbtn_xpos = random.choice(btn_pos)

        if self.level == 1:
            btn1_val = str(random.choice([i for i in range(1,12) if i not in [6]])) 
            btn2_val = str(random.choice([i for i in range(1,12) if i not in [6]])) 
            ans_val = "6"

        elif self.level == 2:
            btn1_val = str(random.choice([i for i in range(1,15) if i not in [5]])) 
            btn2_val = str(random.choice([i for i in range(1,15) if i not in [5]])) 
            ans_val = "5"

        elif self.level == 3:
            btn1_val = str(random.choice([i for i in range(1,32) if i not in [8]])) 
            btn2_val = str(random.choice([i for i in range(1,32) if i not in [8]])) 
            ans_val = "8"
            

        self.btn1 = pygame.Surface((201,73), pygame.SRCALPHA, 32)
        self.btn1.convert_alpha()
        self.btn1.blit(self.context.btn_bg, (0,0))
        text = self.context.fontbig.render(btn1_val, 1, (255,255,255))
        self.btn1.blit(text, (90,20))
        self.context.screen.blit(self.btn1, (self.btn1_xpos, 820))

        self.ansbtn = pygame.Surface((201,73), pygame.SRCALPHA, 32)
        self.ansbtn.convert_alpha()
        self.ansbtn.blit(self.context.btn_bg, (0,0))
        text = self.context.fontbig.render(ans_val, 1, (255,255,255))
        self.ansbtn.blit(text, (90,20))
        self.ans_obj = self.context.screen.blit(self.ansbtn, (ansbtn_xpos, 820))
            
        self.btn3 = pygame.Surface((201,73), pygame.SRCALPHA, 32)
        self.btn3.convert_alpha()
        self.btn3.blit(self.context.btn_bg, (0,0))
        text = self.context.fontbig.render(btn2_val,1, (255,255,255))
        self.btn3.blit(text, (90,20))
        self.context.screen.blit(self.btn3, (self.btn2_xpos, 820))

    def handle_inputs(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.ans_obj.collidepoint(pos):
                    self.correct = True
                    self.remove_btns()
                    self.draw_correct()
                    
                    self.nextlvl_btn = pygame.Surface((201,73), pygame.SRCALPHA, 32)
                    self.nextlvl_btn.convert_alpha()
                    if self.level == 1:
                        self.nextlvl_btn.blit(self.context.lvl2_bg, (0,0)) 
                    elif self.level == 2:
                        self.nextlvl_btn.blit(self.context.lvl3_bg, (0,0))
                    self.nxtlvl_box = self.context.screen.blit(self.nextlvl_btn, (680,820))                  
                    if self.level != 3:
                        self.level += 1

                if self.nxtlvl_box.collidepoint(pos):
                    self.correct = False
                    self.draw_scene()
                    
    def remove_btns(self):
        surf = pygame.Surface((201,73))
        surf.fill((255,255,255))
        self.context.screen.blit(surf, (self.btn1_xpos, 820))
        self.context.screen.blit(surf, (self.btn2_xpos, 820))

    def draw_correct(self):
        correct_surface = pygame.Surface((201,73), pygame.SRCALPHA, 32)
        correct_surface.convert_alpha()
        correct_surface.blit(self.context.btn_bg, (0,0))
        text = self.context.font.render("CORRECT!", 1, (102,255,102))
        correct_surface.blit(text, (90,20))
        self.context.screen.blit(correct_surface, (220,480))
        
    def render_scene(self):
        pygame.display.flip()
