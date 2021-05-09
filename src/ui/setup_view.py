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

        self._renderer = renderer
        self._width = self._renderer.width
        self._height = self._renderer.height
        self._small = int(self._height / 20)
        self._extra_small = int(self._height / 30)
        self._lines = []

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
            self._lines.append(["MUSIC ON", self._small,
                                self._width / 2, self._height / 2 - (self._small * 0.6)])
        else:
            self._lines.append(["MUSIC OFF", self._small, self._width / 2,
                                self._height / 2 - (self._small * 0.6), (70, 70, 70)])
        if audio_info[1]:
            self._lines.append(["SOUND FX ON", self._small, self._width /
                                2, self._height / 2 + (self._small * 1.8)])
        else:
            self._lines.append(["SOUND FX OFF", self._small, self._width /
                                2, self._height / 2 + (self._small * 1.8), (70, 70, 70)])

        self._lines.append(["( press 1 to change )", self._extra_small,
                            self._width / 2, self._height / 2 + (self._small * 0.2)])
        self._lines.append(["( press 2 to change )", self._extra_small,
                            self._width / 2, self._height / 2 + (self._small * 2.6)])
        self._lines.append(["EXIT ( press ESC )", self._small,
                            self._width / 2, self._height / 2 + (self._small * 4.4)])
        self._renderer.render_menu("GAME SETUP", self._lines)
