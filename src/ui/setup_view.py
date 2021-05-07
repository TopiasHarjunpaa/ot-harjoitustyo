class SetupView:
    """A class to represent setup view of UI.

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
        self.extra_small = int(self.height / 30)
        self.lines = []

    def show(self, audio_info):
        """Prepares all information to show for the renderer object.

        Check music and sound fx status from audio_info (on / off).
        Update status text and color (on = white text and off = grey text)

        Information is forwarded inside list of lines.
        Following information will be rendered:
        1. Game and view name
        2. Music and fx status keys
        4. Back to main menu key

        """

        if audio_info[0]:
            self.lines.append(["MUSIC ON", self.small,
                               self.width / 2, self.height / 2 - (self.small * 0.6)])
        else:
            self.lines.append(["MUSIC OFF", self.small,
                               self.width / 2, self.height / 2 - (self.small * 0.6), (70, 70, 70)])
        if audio_info[1]:
            self.lines.append(["SOUND FX ON", self.small, self.width /
                               2, self.height / 2 + (self.small * 1.8)])
        else:
            self.lines.append(["SOUND FX OFF", self.small, self.width /
                               2, self.height / 2 + (self.small * 1.8), (70, 70, 70)])

        self.lines.append(["( press 1 to change )", self.extra_small,
                          self.width / 2, self.height / 2 + (self.small * 0.2)])
        self.lines.append(["( press 2 to change )", self.extra_small,
                          self.width / 2, self.height / 2 + (self.small * 2.6)])
        self.lines.append(["EXIT ( press ESC )", self.small,
                          self.width / 2, self.height / 2 + (self.small * 4.4)])
        self.renderer.render_menu("GAME SETUP", self.lines)
