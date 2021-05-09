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

        self._renderer = renderer
        self._width = self._renderer.width
        self._height = self._renderer.height
        self._small = int(self._height / 20)
        self._extra_small = int(self._height / 25)
        self._lines = []

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
            self._lines.append([txt, self._extra_small, self._width / 2,
                               self._height / 2 + (self._extra_small * (row - 2) * 1.2)])
            row += 1

        while row <= 8:
            self._lines.append(["EMPTY SAVE",
                               self._extra_small,
                               self._width / 2,
                               self._height / 2 +
                               (self._extra_small * (row - 2) * 1.2),
                               (70, 70, 70)])
            row += 1

        self._lines.append(["BACK TO MAIN MENU ( press ESC )",
                           self._small, self._width / 2,
                           self._height / 2 + (self._extra_small * (row - 1.5) * 1.2)])
        self._renderer.render_menu("LOAD YOUR GAME", self._lines)
