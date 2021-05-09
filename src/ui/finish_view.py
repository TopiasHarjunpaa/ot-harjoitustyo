class FinishView:
    """A class to represent finish view of UI.

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
        self._lines = []

    def show(self, information, level):
        """Prepares all information to show for the renderer object.

        Information is forwarded inside list of lines.
        Following information will be rendered:
        1. Game and view name
        2. Previus and current records of the level
        3. Continue key
        4. Back to main menu key

        Args:
            information (dict): Dictionary type progress information from save object.
            level (int): Level number.
        """

        current_record = information[f"level{level}"]
        text1 = f"YOUR PREVIOUS RECORD WAS {current_record}%"
        self._lines.append([text1, self._small, self._width /
                            2, self._height / 2 - self._small])
        self._lines.append([text1, self._small, self._width / 2 - 2,
                            self._height / 2 - self._small - 2, (255, 150, 50)])
        self._lines.append(["CONTINUE ( press ENTER )", self._small,
                            self._width / 2, self._height / 2 + (self._small * 1.2)])
        self._lines.append(["BACK TO MAIN MENU ( press ESC )", self._small,
                            self._width / 2, self._height / 2 + (self._small * 2.4)])
        self._renderer.render_menu(f"LEVEL {level} COMPLETED!", self._lines)
