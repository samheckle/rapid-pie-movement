class ParentScene(object):
    def __init__(self, context):
        self.next = self
        self.context = context
        self.screen = self.context.screen
    
    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self):
        pass

    def SwitchScene(self, next_scene, context=None):
        if next_scene is None:
            self.next = next_scene

        self.next = next_scene(context) if context else next_scene(self.context)

    def Terminate(self):
        self.SwitchScene(None)
