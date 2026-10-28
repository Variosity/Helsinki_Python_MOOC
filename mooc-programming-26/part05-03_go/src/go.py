def who_won(game_board: list):
    one = 0
    two = 0
    for row in game_board:
        for piece in row:
            if piece == 1:
                one += 1
            elif piece == 2:
                two += 1
    if one > two:
        return 1
    elif two > one:
        return 2
    else:
        return 0


if __name__ == "__main__":
    pass