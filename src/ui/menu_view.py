class MenuView:
    """A class to represent menu view of UI.

    Attributes:
        renderer: Renderer object.
    """

    def __init__(self, renderer):
        """Constructs all the necessary attributes for finish view.

        Args:
            renderer (Renderer): Renderer object which renders the display.
        """

        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.extra_small = int(self.height / 30)
        self.lines = []

    def show(self, records):
        """Prepares all information to show for the renderer object.

        Information is forwarded inside list of lines.

        Note: Currently TOP3 RECORDS lines are using list of save objects.
        This list is not ideal for this purposes and requires some ugly filtering here.
        Better solution could be to create another method at information service to
        recieve own list for TOP3 RECORDS.

        Args:
            records (list): List of save objects.
        """

        self.lines.append(["TOP3 RECORDS:", self.extra_small,
                          self.width / 2, self.height / 2 - (self.extra_small * 2.4)])

        rank1 = "EMPTY"
        rank2 = "EMPTY"
        rank3 = "EMPTY"
        if len(records) >= 1:
            rank1 = f"{records[0].nickname} - SCORE: {records[0].progress}%"
        if len(records) >= 2:
            rank2 = f"{records[1].nickname} - SCORE: {records[1].progress}%"
        if len(records) >= 3:
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
        self.lines.append(["GAME SETUP ( press S )", self.small, self.width /
                          2, self.height / 2 + (self.small * 4.8)])
        self.lines.append(["EXIT ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 6)])
        self.renderer.render_menu("MAIN MENU", self.lines)
