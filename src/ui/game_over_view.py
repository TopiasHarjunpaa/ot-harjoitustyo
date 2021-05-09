class GameOverView:
    """A class to represent game over view of UI.

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

    def show(self, information, progress, level):
        """Prepares all information to show for the renderer object.

        Information is forwarded inside list of lines.
        Following information will be rendered:
        1. Game and view name
        2. Previus and current records of the level
        3. Try again key
        4. Back to main menu key

        Args:
            information (dict): Dictionary type progress information from save object.
            progress (int): Progress percentage during previous game event before death.
            level (int): Level number.
        """

        current_record = information[f"level{level}"]
        text1 = f"YOU REACHED {progress}% OF THE LEVEL {level}"

        self._lines.append([text1, self._small, self._width /
                            2, self._height / 2 - self._small])
        self._lines.append([text1, self._small, self._width / 2 - 2,
                            self._height / 2 - self._small - 2, (255, 150, 50)])

        if progress > current_record:
            text2 = f"OLD RECORD WAS {current_record}%"
        else:
            text2 = f"YOUR RECORD IS {current_record}%"

        self._lines.append(
            [text2, self._small, self._width / 2, self._height / 2])
        self._lines.append([text2, self._small, self._width /
                            2 - 2, self._height / 2 - 2, (255, 150, 50)])
        self._lines.append(["TRY AGAIN ( press ENTER )", self._small,
                            self._width / 2, self._height / 2 + (self._small * 2.4)])
        self._lines.append(["BACK TO MAIN MENU ( press ESC )", self._small,
                            self._width / 2, self._height / 2 + (self._small * 3.6)])
        self._renderer.render_menu("GAME OVER", self._lines)
