class StartView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self, information):
        # TODO: Clean up the logic.
        nickname = information["nickname"]
        progress = information["progress"]
        number_of_levels = information["number_of_levels"]
        self.lines.append([f"GAME: {nickname} - TOTAL PROGRESS: {progress}",
                          self.small, self.width / 2, self.height / 2 - self.small / 2])
        self.lines.append([f"GAME: {nickname} - TOTAL PROGRESS: {progress}",
                          self.small, self.width / 2 - 2, self.height / 2 - self.small / 2 - 2, (255, 150, 50)])
        level = 1
        while level <= number_of_levels:
            percent = information[f"level{level}"]
            unlocked = information[f"unlocked{level}"]
            if unlocked:
                self.lines.append([f"LEVEL {level} - PROGRESS: {percent} ( press {level} )", self.small,
                                   self.width / 2, self.height / 2 + (self.small * level * 1.2)])
            else:
                self.lines.append([f"LEVEL {level} - PROGRESS: {percent} ( press {level} )", self.small,
                                   self.width / 2, self.height / 2 + (self.small * level * 1.2), (70, 70, 70)])
            level += 1
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * (level * 1.2 + 0.5))])
        self.renderer.render_menu("CHOOSE LEVEL", self.lines)
