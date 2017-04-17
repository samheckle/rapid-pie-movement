import pygame
import traceback
import os

from . import scenes, events, objects

class RapidPieMovementGame():
    def __init__(self):
        # Sets basePath to directory this file is in
        self.basePath = os.path.dirname(__file__)

        self.width = 1200
        self.height = 900
        self.fps = 20
        self.title = "Rapid Pie Movement"

