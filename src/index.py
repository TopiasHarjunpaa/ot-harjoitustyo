from services.game_service import GameService


def main():
    game = GameService()
    game.start()


if __name__ == "__main__":
    main()
