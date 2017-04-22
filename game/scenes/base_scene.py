"""
Base Scene class that all other scenes inherit from.
"""
class BaseScene(object):
    def __init__(self, context):
        self.context = context

    def handle_inputs(self, events):
        """
        Handle pygame events
        """
        print "You must override this function"

    def render_scene(self):
        print "You must override this function"

