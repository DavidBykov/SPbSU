from random import shuffle


def shuffle_field(field):
    for i in range(3):
        field[i * 2][1] = 1
        field[i * 2][3] = 1

    random_shuffle = [0, 0, 0, 0, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
    shuffle(random_shuffle)

    for i in range(5):
        for j in range(5):
            if field[i][j] != 1:
                field[i][j] = random_shuffle.pop()