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

        self.renderer = renderer
        self.width = self.renderer.width
        self.height = self.renderer.height
        self.big = int(self.height / 10)
        self.small = int(self.height / 20)
        self.lines = []

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
        self.lines.append([text1, self.small, self.width /
                          2, self.height / 2 - self.small])
        self.lines.append([text1, self.small, self.width / 2 - 2,
                          self.height / 2 - self.small - 2, (255, 150, 50)])
        self.lines.append(["CONTINUE ( press ENTER )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 1.2)])
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 2.4)])
        self.renderer.render_menu(f"LEVEL {level} COMPLETED!", self.lines)
