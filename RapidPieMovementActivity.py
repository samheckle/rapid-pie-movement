"""
Main file for Rapid Pie Movement
"""
import pygame
from sugar3.activity.activity import Activity
from sugar3.activity.widgets import StopButton, ActivityButton

from gi.repository import Gtk
from gettext import gettext as _
import game

class RapidPieMovementActivity(activity.Activity):
    def __init__(self, sugar_handle):
        super(RapidPieMovementActivity, self).__init__(sugar_handle)

        # Creates a game instance
        self.game = game.RapidPieMovementGame()

        #self.create_toolbar()

        self._pygamecanvas = sugargame.canvas.RapidPieCanvas(self)

        self.set_canvas(self._pygamecanvs)
        self._pygamecanvas.grab_focus()


        # Start game
        self._pygamecanvas.run_pygame(self.game_run)

        
        
