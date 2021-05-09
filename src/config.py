import os
from dotenv import load_dotenv

NUMBER_OF_LEVELS = 4
TITLE = "The Possible Game"
FPS = 60

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

LEVEL_PATHS = []
for i in range(NUMBER_OF_LEVELS + 1):
    LEVEL_FILENAME = os.getenv(f"LEVEL{i}_FILENAME") or f"level_{i}.csv"
    LEVEL_FILE_PATH = os.path.join(dirname, "assets", "maps", LEVEL_FILENAME)
    LEVEL_PATHS.append(LEVEL_FILE_PATH)

FONT_FILENAME = os.getenv("FONT_FILENAME") or "fontstyle.ttf"
FONT_PATH = os.path.join(dirname, "assets", "fonts", FONT_FILENAME)

MENU_BG_FILENAME = os.getenv("MENU_BG_FILENAME") or "menu_background.png"
MENU_BG_PATH = os.path.join(dirname, "assets", "images", MENU_BG_FILENAME)

LEVEL_BG_PATHS = []
for i in range(1, NUMBER_OF_LEVELS + 1):
    LEVEL_BG_FILENAME = os.getenv(
        f"LEVEL{i}_BG_FILENAME") or f"level{i}_background.jpg"
    LEVEL_BG_FILE_PATH = os.path.join(
        dirname, "assets", "images", LEVEL_BG_FILENAME)
    LEVEL_BG_PATHS.append(LEVEL_BG_FILE_PATH)

PLAYLIST = []
MENU_MUSIC_FILENAME = os.getenv("MENU_MUSIC_FILENAME") or "menu.ogg"
MENU_MUSIC_PATH = os.path.join(dirname, "assets", "audio", MENU_MUSIC_FILENAME)
PLAYLIST.append(MENU_MUSIC_PATH)
for i in range(1, 5):
    LEVEL_MUSIC_FILENAME = os.getenv(
        f"LEVEL{i}_MUSIC_FILENAME") or f"level{i}.ogg"
    MUSIC_PATH = os.path.join(dirname, "assets", "audio", LEVEL_MUSIC_FILENAME)
    PLAYLIST.append(MUSIC_PATH)

BACK_FILENAME = os.getenv("BACK_SOUND_FILENAME") or "back.wav"
BACK = os.path.join(dirname, "assets", "audio", BACK_FILENAME)
DIE_FILENAME = os.getenv("DIE_SOUND_FILENAME") or "die.wav"
DIE = os.path.join(dirname, "assets", "audio", DIE_FILENAME)
JUMP_FILENAME = os.getenv("JUMP_SOUND_FILENAME") or "jump.wav"
JUMP = os.path.join(dirname, "assets", "audio", JUMP_FILENAME)
KEY_FILENAME = os.getenv("KEY_SOUND_FILENAME") or "key.wav"
KEY = os.path.join(dirname, "assets", "audio", KEY_FILENAME)
FORWARD_FILENAME = os.getenv("FORWARD_SOUND_FILENAME") or "forward.wav"
FORWARD = os.path.join(dirname, "assets", "audio", FORWARD_FILENAME)
