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

current_room = 1

top_left_x = 0
top_left_y = 100

ROOM_WIDTH = 23
ROOM_HEIGHT  = 16
TILE_SIZE = 30

player_y, player_x = 7, 17
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

#MAP#

GAME_MAP = [["Room 0 - where unused objects are kept", 0, 0, False, False]]

GAME_MAP  += [
    #["Room name", Top exit?, Right exit?]
    ["Raccoon House", False, False] #room 1
    ]

#OBJECTS#

objects = {
    0: [image('grass')],
    1: [image('wall')],
    2: [image('wall1')],
    3: [image('longwall')],
    4: [image('stones')],
    5: [image('shortstones')],
    6: [image('longstones')],
    7: [image('raccoon')]
    }

items_player_may_stand_on = [0]

#SCENERY#

scenery = {
    #room number: [[object number, y position, x position]...]
    1: [[1, 5, 11], [1, 6, 11],
        [2, 10, 11], [1, 11, 11], [1, 12, 11], [1, 5, 20], [1, 6, 20],
        [1, 7, 20], [1, 8, 20], [1, 9, 20], [1, 10, 20], [1, 11, 20],
        [1, 12, 20], [3, 4, 11], [3, 13, 11], [5, 6, 0], [5, 10, 0],
        [4, 2, 3], [4, 3, 3], [4, 4, 3], [4, 5, 3], [4, 11, 3],
        [4, 12, 3], [4, 13, 3], [4, 14, 3], [6, 1, 3], [6, 15, 3],
        [4, 2, 22], [4, 3, 22], [4, 4, 22], [4, 5, 22],[4, 6, 22],
        [4, 7, 22], [4, 8, 22], [4, 9, 22], [4, 10, 22], [4, 11, 22],
        [4, 12, 22], [4, 13, 22], [4, 14, 22], [7, 6, 9]]
    }

#MAKE MAP#

def generate_map():
    global room_map, top_left_x, top_left_y
    room_data = GAME_MAP[current_room]
    
    floor_type = 0

    room_map = [[floor_type] * ROOM_WIDTH]
    
    for y in range(ROOM_HEIGHT):
        room_map.append([floor_type] * ROOM_WIDTH)

    if current_room in scenery:
        for this_scenery in scenery[current_room]: 
            scenery_number = this_scenery[0]
            scenery_y = this_scenery[1]
            scenery_x = this_scenery[2]
            room_map[scenery_y][scenery_x] = scenery_number

            image_here = objects[scenery_number][0]
            image_width = image_here.get_width()
            image_width_in_tiles = int(image_width / TILE_SIZE)

            for tile_number in range(1, image_width_in_tiles):
                room_map[scenery_y][scenery_x + tile_number] = 255    
    
#DISPLAY#
def draw_image(image, y, x):
    screen.blit(
        image,
        (int(top_left_x + (x * TILE_SIZE)),
         int(top_left_y + (y * TILE_SIZE) - image.get_height()))
        )

def draw_player():
    player_image = PLAYER[player_direction][player_frame]
    draw_image(player_image, player_y + player_offset_y,
               player_x + player_offset_x)
    
def draw():
    if game_over:
        return

    pygame.draw.rect(screen, (0, 128, 0), (0, 100, 690, 450))

    screen.set_clip((0, 100, 690, 450))

    floor_type = 0

    for y in range(ROOM_HEIGHT):
        for x in range(ROOM_WIDTH):
            draw_image(objects[floor_type][0], y, x)

    for y in range(ROOM_HEIGHT):
        for x in range(ROOM_WIDTH):
            item_here = room_map[y][x]
            # Player cannot walk on 255: it marks spaces used by wide objects.
            if item_here not in items_player_may_stand_on + [255]:
                image = objects[item_here][0]
                draw_image(image, y, x)
        
        if (player_y == y):
            draw_player()

    screen.set_clip(None)
    
#mainloop#
clock = pygame.time.Clock()
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
           
    clock.tick(16) 

    generate_map()
    draw()
    
    if player_frame > 0:
        player_frame += 1
        #time.sleep(0.05)
        if player_frame == 5:
            player_frame = 0
            player_offset_x = 0
            player_offset_y = 0
    
    # save player's current position
    old_player_x = player_x
    old_player_y = player_y

    keys = pygame.key.get_pressed()
    
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

    if room_map[player_y][player_x] not in items_player_may_stand_on:
        player_x = old_player_x
        player_y = old_player_y
        player_frame = 0
    
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
