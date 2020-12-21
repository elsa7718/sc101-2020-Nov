from campy.graphics.gobjects import GOval, GRect, GLabel

class Extension:
    def __init__(self):
        self.score=0
        self.label=GLabel('Score:'+str(self.score))
        self.label.font='Courier-15-bold-italic'
