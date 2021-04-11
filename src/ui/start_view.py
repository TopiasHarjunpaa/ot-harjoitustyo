class StartView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self):
        # Current record is just placeholder
        # Render also name somewhere...
        self.lines.append(["LEVEL 1 ( record 45% - press 1 )",
                          self.small, self.width / 2, self.height / 2])
        self.lines.append(["LEVEL 2 ( unlocked - press 2 )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 1.2), (70, 70, 70)])
        self.lines.append(["LEVEL 3 ( unlocked - press 3 )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 2.4), (70, 70, 70)])
        self.lines.append(["LEVEL 4 ( unlocked - press 4 )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 3.6), (70, 70, 70)])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 5.4)])
        self.renderer.render_menu("CHOOSE LEVEL", self.lines)
