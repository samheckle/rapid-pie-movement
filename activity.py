"""
Main file for Rapid Pie Movement
"""

from sugar3.activity.activity import Activity
from sugar3.activity.widgets import StopButton, ActivityButton

from gi.repository import Gtk
from gettext import gettext as _

class RapidPieMovement(Activity):
    def __init__(self, sugar_handle):
        Activity.__init__(self, sugar_handle)

        toolbar = Gtk.Toolbar()

        self.set_toolbar_box(toolbar)

        toolbar.insert(ActivityButton(self), -1)

        
