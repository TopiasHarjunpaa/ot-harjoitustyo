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

        self._renderer = renderer
        self._width = self._renderer.width
        self._height = self._renderer.height
        self.small = int(self._height / 20)
        self._extra_small = int(self._height / 30)
        self._lines = []

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

        self._lines.append(["TOP3 RECORDS:", self._extra_small,
                            self._width / 2, self._height / 2 - (self._extra_small * 2.4)])

        self._lines.append([records[0], self._extra_small, self._width / 2,
                            self._height / 2 - (self._extra_small * 1.2), (255, 215, 0)])
        self._lines.append([records[1], self._extra_small,
                            self._width / 2, self._height / 2, (192, 192, 192)])
        self._lines.append([records[2], self._extra_small, self._width / 2,
                            self._height / 2 + (self._extra_small * 1.2), (205, 127, 50)])

        self._lines.append(["NEW GAME ( press N )", self.small,
                            self._width / 2, self._height / 2 + (self.small * 2.4)])
        self._lines.append(["LOAD GAME ( press L )", self.small, self._width /
                            2, self._height / 2 + (self.small * 3.6)])
        self._lines.append(["GAME SETUP ( press S )", self.small, self._width /
                            2, self._height / 2 + (self.small * 4.8)])
        self._lines.append(["EXIT ( press ESC )", self.small,
                            self._width / 2, self._height / 2 + (self.small * 6)])
        self._renderer.render_menu("MAIN MENU", self._lines)
