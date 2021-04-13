class LoadGameView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.extra_small = int(self.height / 25)
        self.lines = []

    def show(self, saves: list):
        row = 1
        for save in saves:
            text = f"{save.nickname} - {save.progress}% - CREATED: {save.created_at} ( press {row} )"
            self.lines.append([text, self.extra_small, self.width / 2,
                              self.height / 2 + (self.extra_small * (row - 2) * 1.2)])
            row += 1
        while row <= 8:
            self.lines.append(["EMPTY SAVE", self.extra_small, self.width / 2,
                              self.height / 2 + (self.extra_small * (row - 2) * 1.2), (70, 70, 70)])
            row += 1
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.extra_small * (row - 1.5) * 1.2)])
        self.renderer.render_menu("LOAD YOUR GAME", self.lines)
