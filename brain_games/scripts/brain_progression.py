#!/usr/bin/env python


from brain_games.engine import run_game
from brain_games.games import progression_game


def main():
    run_game(progression_game)


if __name__ == '__main__':
    main()
