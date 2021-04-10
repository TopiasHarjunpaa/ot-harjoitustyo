class FinishView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self):
        self.lines.append(["THE POSSIBLE GAME", self.big, self.width / 2, self.height / 5])
        self.lines.append(["CONGRATULATIONS!", self.big, self.width / 2, self.height / 5 + (self.big * 1.2)])
        self.lines.append(["YOU GOT XX POINTS", self.small, self.width / 2, self.height / 2])
        self.lines.append(["CONTINUE ( press C )", self.small, self.width / 2, self.height / 2 + (self.small * 1.2)])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small, self.width / 2, self.height / 2 + (self.small * 2.4)])
        self.renderer.render_menu(self.lines)