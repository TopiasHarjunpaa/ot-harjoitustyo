class GameOverView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self):
        self.lines.append(["YOU DISCOVERED 45 % OF THE LEVEL",
                          self.small, self.width / 2, self.height / 2 - self.small])
        self.lines.append(["TRY AGAIN ( press ENTER )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 1.2)])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 2.4)])
        self.renderer.render_menu("GAME OVER", self.lines)
