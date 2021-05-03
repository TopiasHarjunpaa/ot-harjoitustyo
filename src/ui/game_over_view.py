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

        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

    def show(self, information, progress, level):
        """Prepares all information to show for the renderer object.

        Information is forwarded inside list of lines.

        Args:
            information (dict): Dictionary type progress information from save object.
            progress (int): Progress percentage during previous game event before death.
            level (int): Level number.
        """

        current_record = information[f"level{level}"]
        text1 = f"YOU REACHED {progress}% OF THE LEVEL {level}"
        self.lines.append([text1, self.small, self.width /
                          2, self.height / 2 - self.small])
        self.lines.append([text1, self.small, self.width / 2 - 2,
                          self.height / 2 - self.small - 2, (255, 150, 50)])
        if progress > current_record:
            text2 = f"OLD RECORD WAS {current_record}%"
        else:
            text2 = f"YOUR RECORD IS {current_record}%"
        self.lines.append([text2, self.small, self.width / 2, self.height / 2])
        self.lines.append([text2, self.small, self.width /
                          2 - 2, self.height / 2 - 2, (255, 150, 50)])
        self.lines.append(["TRY AGAIN ( press ENTER )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 2.4)])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 3.6)])
        self.renderer.render_menu("GAME OVER", self.lines)
