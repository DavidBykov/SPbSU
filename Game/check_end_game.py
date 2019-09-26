def check_end_game(field):

    for i in range(5):
        if field[i][0] != 2 or field[i][2] != 3 or field[i][4] != 4:
            return False

    return True