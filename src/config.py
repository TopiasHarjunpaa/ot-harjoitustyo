import os
from dotenv import load_dotenv

NUMBER_OF_LEVELS = 4
TITLE = "The Possible Game"
BACKGROUND = (0, 0, 0)
FPS = 60

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

MAP_PATHS = []
for i in range(NUMBER_OF_LEVELS + 1):
    MAP_FILENAME = f"level_{i}.csv"
    MAP_FILE_PATH = os.path.join(dirname, "assets", "maps", MAP_FILENAME)
    MAP_PATHS.append(MAP_FILE_PATH)

FONT_FILENAME = "fontstyle.ttf"
FONT_PATH = os.path.join(dirname, "assets", "fonts", FONT_FILENAME)

BG_FILENAME = "test_background.png"
BG_PATH = os.path.join(dirname, "assets", "images", BG_FILENAME)

MENU_MUSIC_FILENAME = "menu.ogg"
MENU_MUSIC = os.path.join(dirname, "assets", "audio", MENU_MUSIC_FILENAME)
PLAYLIST = []
PLAYLIST.append(MENU_MUSIC)
for i in range(1,5):
    MUSIC_PATH = os.path.join(dirname, "assets", "audio", f"level{i}.ogg")
    PLAYLIST.append(MUSIC_PATH)

BACK = os.path.join(dirname, "assets", "audio", "back.wav")
DIE = os.path.join(dirname, "assets", "audio", "die.wav")
JUMP = os.path.join(dirname, "assets", "audio", "jump.wav")
KEY = os.path.join(dirname, "assets", "audio", "key.wav")
FORWARD = os.path.join(dirname, "assets", "audio", "forward.wav")
