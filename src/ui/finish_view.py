class FinishView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self, information, level):
        current_record = information[f"level{level}"]
        text1 = f"YOUR PREVIOUS RECORD WAS {current_record}%"
        self.lines.append([text1, self.small, self.width /
                          2, self.height / 2 - self.small])
        self.lines.append([text1, self.small, self.width / 2 - 2,
                          self.height / 2 - self.small - 2, (255, 150, 50)])
        self.lines.append(["CONTINUE ( press ENTER )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 1.2)])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 2.4)])
        self.renderer.render_menu(f"LEVEL {level} COMPLETED!", self.lines)
