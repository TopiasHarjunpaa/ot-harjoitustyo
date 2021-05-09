class NewGameView:
    """A class to represent new game view of UI.

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
        self._big = int(self._height / 10)
        self.small = int(self._height / 20)
        self._lines = []

    def show(self, nickname, color=(255, 255, 255)):
        """Prepares all information to show for the renderer object.

        New game view allows player to create new save object with personal nickname.
        Continue text will be rendered as grey color until player has typed all 4 required
        letters for nickname.

        Information is forwarded inside list of lines.
        Following information will be rendered:
        1. Game and view name
        2. Nickname status
        3. Continue key
        4. Back to main menu key

        Args:
            nickname (str): Nickname of the save
            color (tuple, optional): Color of the continue text. Defaults to (255, 255, 255).
        """
        self._lines.append(["ENTER YOUR NICKNAME", self.small,
                            self._width / 2, self._height / 2])
        self._lines.append([nickname, self._big, self._width / 2,
                            self._height / 2 + (self.small * 2.4)])
        self._lines.append(["CONTINUE ( press ENTER )", self.small,
                            self._width / 2, self._height / 2 + (self.small * 4.8), color])
        self._lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                            self._width / 2, self._height / 2 + (self.small * 6)])
        self._renderer.render_menu("CREATE NEW GAME", self._lines)
