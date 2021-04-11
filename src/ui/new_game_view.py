class NewGameView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self, nickname, color=(255, 255, 255)):
        self.lines.append(["ENTER YOUR NICKNAME", self.small,
                          self.width / 2, self.height / 2])
        self.lines.append([nickname, self.big, self.width / 2,
                          self.height / 2 + (self.small * 2.4)])
        self.lines.append(["CONTINUE ( press ENTER )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 4.8), color])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 6)])
        self.renderer.render_menu("CREATE NEW GAME", self.lines)
