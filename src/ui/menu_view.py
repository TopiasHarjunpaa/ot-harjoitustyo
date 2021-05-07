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
        Following information will be rendered:
        1. Game and view name
        2. TOP3 records (text colors: gold, silver, bronze)
        3. New game view key
        4. Load game view key
        5. Exit key

        Args:
            records (list): List of save objects.
        """

        self.lines.append(["TOP3 RECORDS:", self.extra_small,
                          self.width / 2, self.height / 2 - (self.extra_small * 2.4)])

        self.lines.append([records[0], self.extra_small, self.width / 2,
                          self.height / 2 - (self.extra_small * 1.2), (255, 215, 0)])
        self.lines.append([records[1], self.extra_small,
                          self.width / 2, self.height / 2, (192, 192, 192)])
        self.lines.append([records[2], self.extra_small, self.width / 2,
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
