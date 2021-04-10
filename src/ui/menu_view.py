class MenuView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self):
        self.lines.append(["THE POSSIBLE GAME", self.big, self.width / 2, self.height / 5])
        self.lines.append(["MAIN MENU", self.big, self.width / 2, self.height / 5 + (self.big * 1.2)])
        self.lines.append(["NEW GAME ( press N )", self.small, self.width / 2, self.height / 2])
        self.lines.append(["LOAD GAME* ( press L )", self.small, self.width / 2, self.height / 2 + (self.small * 1.2)])
        self.lines.append(["EXIT ( press ESC )", self.small, self.width / 2, self.height / 2 + (self.small * 2.4)])
        self.lines.append(["* Load game currently disabled", self.small, self.width / 2, self.height - (self.small * 2)])
        self.renderer.render_menu(self.lines)

