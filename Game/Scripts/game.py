import pygame
from check_end_game import check_end_game
from paint import paint
from shuffle_field import shuffle_field

# pygame initialization
pygame.init()

# display and mouse settings
scene = pygame.display.set_mode((448, 448))
pygame.display.set_caption("Game")
pygame.mouse.set_visible(False)

# load background
background = pygame.image.load('Sprites/background.png')
scene.blit(background, (0, 0))

# load backgound music
pygame.mixer.music.load('Music/background.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# load sprites
# 0 - empty, 1 - wall, 2 - red_box, 3 - green_box, 4 - blue_box, 5 - red_box pressed, 6 - green_box pressed, 7 - blue_box pressed
sprites = [
    pygame.image.load('Sprites/empty.png'),
    pygame.image.load('Sprites/wall.png'),
    pygame.image.load('Sprites/box1.png'),
    pygame.image.load('Sprites/box2.png'),
    pygame.image.load('Sprites/box3.png'),
    pygame.image.load('Sprites/selected.png'),
    pygame.image.load('Sprites/box1_pressed.png'),
    pygame.image.load('Sprites/box2_pressed.png'),
    pygame.image.load('Sprites/box3_pressed.png')
]

# create and shuffle field
field = [[0] * 5 for _ in range(5)]
shuffle_field(field)

# game variables
end_game = False
selected_fields = [0, 0]
pressed_space = False
pressed_fields = [0, 0]

# main loop
while True:
    # FPS
    pygame.time.Clock().tick(60)

    if not end_game:

        # exit_click tracking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # click tracking
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_fields[1] = (selected_fields[1] - 1) % 5

                elif event.key == pygame.K_RIGHT:
                    selected_fields[1] = (selected_fields[1] + 1) % 5

                elif event.key == pygame.K_UP:
                    selected_fields[0] = (selected_fields[0] - 1) % 5

                elif event.key == pygame.K_DOWN:
                    selected_fields[0] = (selected_fields[0] + 1) % 5

                # mobility check
                elif event.key == pygame.K_SPACE:
                    if field[selected_fields[0]][selected_fields[1]] != 0 and \
                            field[selected_fields[0]][selected_fields[1]] != 1:
                        pressed_fields = selected_fields.copy()
                        pressed_space = not pressed_space

                    elif field[selected_fields[0]][selected_fields[1]] == 0 and pressed_space:
                        # distance check
                        if abs(selected_fields[0] - pressed_fields[0]) + abs(
                                selected_fields[1] - pressed_fields[1]) == 1:
                            field[selected_fields[0]][selected_fields[1]], field[pressed_fields[0]][pressed_fields[1]] = \
                                field[pressed_fields[0]][pressed_fields[1]], field[selected_fields[0]][
                                    selected_fields[1]]
                            pressed_space = not pressed_space

        # drawing scene
        scene.blit(background, (0, 0))
        paint(field, scene, sprites, selected_fields, pressed_fields, pressed_space)

    else:
        # exit check
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                exit()

        # end_game text
        font = pygame.font.Font(None, 36)
        text_end_game = font.render("You win.", 1, (0, 0, 0), (255, 255, 255))
        place_for_text = text_end_game.get_rect(center=(224, 150))
        text_end_game_2 = font.render("Press any button.", 1, (0, 0, 0), (255, 255, 255))
        place_for_text2 = text_end_game_2.get_rect(center=(224, 180))
        scene.blit(text_end_game, place_for_text)
        scene.blit(text_end_game_2, place_for_text2)

    if check_end_game(field):
        end_game = True

    pygame.display.update()