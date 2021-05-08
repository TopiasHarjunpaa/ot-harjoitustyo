class LoadGameView:
    """A class to represent load game view of UI.

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
        self.extra_small = int(self.height / 25)
        self.lines = []

    def show(self, saves: list):
        """Prepares all information to show for the renderer object.

        Information is forwarded inside list of lines.
        Following information will be rendered:
        1. Game and view name
        2. List of available saves and their keys (8 rows, empty rows are greyed)
        4. Back to main menu key

        Args:
            saves (list): List of save objects.
        """

        row = 1
        for save in saves:
            txt = f"{save.nickname} - {save.progress}% - CREATED: {save.created_at} ( press {row} )"
            self.lines.append([txt, self.extra_small, self.width / 2,
                               self.height / 2 + (self.extra_small * (row - 2) * 1.2)])
            row += 1

        while row <= 8:
            self.lines.append(["EMPTY SAVE",
                               self.extra_small,
                               self.width / 2,
                               self.height / 2 +
                               (self.extra_small * (row - 2) * 1.2),
                               (70, 70, 70)])
            row += 1

        self.lines.append(["BACK TO MAIN MENU ( press ESC )",
                           self.small, self.width / 2,
                           self.height / 2 + (self.extra_small * (row - 1.5) * 1.2)])
        self.renderer.render_menu("LOAD YOUR GAME", self.lines)
