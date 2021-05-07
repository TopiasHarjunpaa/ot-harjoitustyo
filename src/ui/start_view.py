class StartView:
    """A class to represent start view of UI.

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

    def show(self, information):
        """Prepares all information to show for the renderer object.

        Information is forwarded inside list of lines.

        Start view shows list of levels at the game. Only levels which are
        unlocked at the current save will be rendered with white color. Unlocked
        levels will be rendered with grey color. These are determined according
        to the save object information.

        Information is forwarded inside list of lines.
        Following information will be rendered:
        1. Game and view name
        2. Nickname and progress of the save
        3. List of available levels and best progress for each (unavailable levels are greyed)
        4. Back to main menu key

        Args:
             information (dict): Dictionary type progress information from save object.
        """

        nickname = information["nickname"]
        progress = information["progress"]
        number_of_levels = information["number_of_levels"]
        self.lines.append([f"GAME: {nickname} - TOTAL PROGRESS: {progress}%",
                          self.small, self.width / 2, self.height / 2 - self.small / 2])
        self.lines.append([f"GAME: {nickname} - TOTAL PROGRESS: {progress}%",
                          self.small, self.width / 2 - 2, self.height / 2 - self.small / 2 - 2, (255, 150, 50)])
        level = 1
        while level <= number_of_levels:
            percent = information[f"level{level}"]
            unlocked = information[f"unlocked{level}"]
            if unlocked:
                self.lines.append([f"LEVEL {level} - PROGRESS: {percent}% ( press {level} )", self.small,
                                   self.width / 2, self.height / 2 + (self.small * level * 1.2)])
            else:
                self.lines.append([f"LEVEL {level} - PROGRESS: {percent}% ( press {level} )", self.small,
                                   self.width / 2, self.height / 2 + (self.small * level * 1.2), (70, 70, 70)])
            level += 1
        self.lines.append(["BACK TO MAIN MENU ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * (level * 1.2 + 0.5))])
        self.renderer.render_menu("CHOOSE LEVEL", self.lines)
