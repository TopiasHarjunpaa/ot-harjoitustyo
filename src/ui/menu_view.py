class MenuView:
    def __init__(self, renderer):
        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.extra_small = int(self.height / 30)
        self.lines = []

    def show(self, records):
        # TODO: Clean up this.
        self.lines.append(["TOP3 RECORDS:", self.extra_small,
                          self.width / 2, self.height / 2 - (self.extra_small * 2.4)])
        rank1 = f"{records[0].nickname} - SCORE: {records[0].progress}%"
        rank2 = f"{records[1].nickname} - SCORE: {records[1].progress}%"
        rank3 = f"{records[2].nickname} - SCORE: {records[2].progress}%"
        self.lines.append([rank1, self.extra_small, self.width / 2,
                          self.height / 2 - (self.extra_small * 1.2), (255, 215, 0)])
        self.lines.append(
            [rank2, self.extra_small, self.width / 2, self.height / 2, (192, 192, 192)])
        self.lines.append([rank3, self.extra_small, self.width / 2,
                          self.height / 2 + (self.extra_small * 1.2), (205, 127, 50)])

        self.lines.append(["NEW GAME ( press N )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 2.4)])
        self.lines.append(["LOAD GAME ( press L )", self.small, self.width /
                          2, self.height / 2 + (self.small * 3.6)])
        self.lines.append(["EXIT ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 4.8)])
        self.renderer.render_menu("MAIN MENU", self.lines)
