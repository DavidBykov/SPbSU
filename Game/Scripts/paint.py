def paint(field, scene, sprites, selected, pressed_fields, pressed_space):

    for i in range(5):
        for j in range(5):
            scene.blit(sprites[field[i][j]], (64 * (j + 1), 64 * (i + 1)))

    if pressed_space:
        scene.blit(sprites[field[pressed_fields[0]][pressed_fields[1]] + 4], (64 * (pressed_fields[1] + 1), 64 * (pressed_fields[0] + 1)))

    scene.blit(sprites[5], (64 * (selected[1] + 1), 64 * (selected[0] + 1)))