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

        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self, nickname, color=(255, 255, 255)):
        """Prepares all information to show for the renderer object.

        New game view allows player to create new save object with personal nickname.
        Continue text will be rendered as grey color until player has typed all 4 required
        letters for nickname.

        Information is forwarded inside list of lines.

        Args:
            nickname (str): Nickname of the save
            color (tuple, optional): Color of the continue text. Defaults to (255, 255, 255).
        """
        self.lines.append(["ENTER YOUR NICKNAME", self.small,
                          self.width / 2, self.height / 2])
        self.lines.append([nickname, self.big, self.width / 2,
                          self.height / 2 + (self.small * 2.4)])
        self.lines.append(["CONTINUE ( press ENTER )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 4.8), color])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 6)])
        self.renderer.render_menu("CREATE NEW GAME", self.lines)
