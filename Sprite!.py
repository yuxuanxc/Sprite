import pygame
import os

pygame.init()
pygame.display.set_caption("Sprite!")

#VARIABLES#
WIDTH = 690
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))

current_path = os.path.dirname('Sprite!.py')
image_path = os.path.join(current_path, 'images')

def image(image):
    return pygame.image.load(os.path.join(image_path, image + '.png'))

top_left_x = 100
top_left_y = 150

TILE_SIZE = 30

player_y, player_x = 2, 5
game_over = False

PLAYER = {
    "left": [image('astronaut_left'), image('astronaut_left_1'),
        image('astronaut_left_2'), image('astronaut_left_3'),
        image('astronaut_left_4')
        ],
    "right": [image('astronaut_right'), image('astronaut_right_1'),
        image('astronaut_right_2'), image('astronaut_right_3'),
        image('astronaut_right_4')
        ],
    "up": [image('astronaut_back'), image('astronaut_back_1'),
        image('astronaut_back_2'), image('astronaut_back_3'),
        image('astronaut_back_4')
        ],
    "down": [image('astronaut_front'), image('astronaut_front_1'),
        image('astronaut_front_2'), image('astronaut_front_3'),
        image('astronaut_front_4')
        ]
}

player_direction = "down"
player_frame = 0
player_image = PLAYER[player_direction][player_frame]
player_offset_x, player_offset_y = 0, 0

#DISPLAY#
def draw_image(image, y, x):
    screen.blit(
        image,
        (top_left_x + (x * TILE_SIZE),
         top_left_y + (y * TILE_SIZE) - image.get_height())
        )

def draw_player():
    player_image = PLAYER[player_direction][player_frame]
    draw_image(player_image, player_y + player_offset_y, player_x + player_offset_x)
    
def draw():
    if game_over:
        return

    pygame.draw.rect(screen, (0,0,0), (0, 0, 690, 100))
    pygame.draw.rect(screen, (0, 0, 0), (0, 100, 690, 450))
    pygame.draw.rect(screen, (0,0,0), (0, 550, 690, 100))

    for y in range(HEIGHT):
        if (player_y == y):
            draw_player()
    
#mainloop#
clock = pygame.time.Clock()
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
           
    clock.tick(11) 
    pygame.time.delay(40)

    keys = pygame.key.get_pressed()    
    draw()
    
    if game_over: break
        
    if player_frame > 0:
        player_frame += 1
        #time.sleep(0.05)
        if player_frame == 5:
            player_frame = 0
            player_offset_x = 0
            player_offset_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # save player's current position
    old_player_x = player_x
    old_player_y = player_y
    
    # move if key is pressed
    if player_frame == 0:
        if keys[pygame.K_RIGHT]:
            from_player_x = player_x
            from_player_y = player_y
            player_x += 1
            player_direction = "right"
            player_frame = 1
        elif keys[pygame.K_LEFT]: #elif stops player making diagonal movements
            from_player_x = player_x
            from_player_y = player_y
            player_x -= 1
            player_direction = "left"
            player_frame = 1
        elif keys[pygame.K_UP]:
            from_player_x = player_x
            from_player_y = player_y
            player_y -= 1
            player_direction = "up"
            player_frame = 1
        elif keys[pygame.K_DOWN]:
            from_player_x = player_x
            from_player_y = player_y
            player_y += 1
            player_direction = "down"
            player_frame = 1

    if player_direction == "right" and player_frame > 0:
        player_offset_x = -1 + (0.25 * player_frame)
    if player_direction == "left" and player_frame > 0:
        player_offset_x = 1 - (0.25 * player_frame)
    if player_direction == "up" and player_frame > 0:
        player_offset_y = 1 - (0.25 * player_frame)
    if player_direction == "down" and player_frame > 0:
        player_offset_y = -1 + (0.25 * player_frame)

    pygame.display.update()

pygame.quit()

