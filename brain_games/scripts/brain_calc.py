#!/usr/bin/env python


from brain_games.engine import run_game
from brain_games.games import calc_game


def main():
    run_game(calc_game)


if __name__ == '__main__':
    main()
