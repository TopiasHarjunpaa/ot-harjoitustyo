class LoadGameView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.extra_small = int(self.height / 30)
        self.lines = []

    def show(self, saves: list):
        # TODO: If less than 9 saves. Fill with blank saves.
        for i in range(len(saves)):
            text = f"{saves[i].nickname} ( press {i + 1})"
            self.lines.append(
                [text, self.extra_small, self.width / 2, self.height / 2 + (self.extra_small * i * 1.2)])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.extra_small * len(saves) * 1.2 + self.small)])
        self.renderer.render_menu("LOAD YOUR GAME", self.lines)
