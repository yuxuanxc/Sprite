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
sound_path = os.path.join(current_path, 'sounds')

def image(image):
    return pygame.image.load(os.path.join(image_path, image + '.png'))

def sound(sound):
    soundObj = pygame.mixer.Sound(os.path.join(sound_path, sound + '.wav'))
    soundObj.play()

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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
    7: [image('raccoon')],
    8: [image('fireplace')],
    9: [image('charcoal')],
    10: [image('picture')],
    11: [image('charcoal')]
    }

items_player_may_carry = list(range(9, 12))
items_player_may_stand_on = items_player_may_carry + [0]

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
        [4, 12, 22], [4, 13, 22], [4, 14, 22], [7, 6, 9], [8, 4, 6]]
    }

#PROPS#

props = {
    #object number: [room, y, x]
    9: [1, 4, 6],
    10: [0, 0, 0],
    11: [1, 6, 6]
    }

in_my_pockets = [10]
selected_item = 0
item_carrying = in_my_pockets[selected_item]

def find_object_start_x():
    checker_x = player_x
    while room_map[player_y][checker_x] == 255:
        checker_x -= 1
    return checker_x

def get_item_under_player():
    item_x = find_object_start_x()
    item_player_is_on = room_map[player_y][item_x]
    return item_player_is_on

def pick_up_object():
    global room_map
    item_player_is_on = get_item_under_player()
    if item_player_is_on in items_player_may_carry:
        room_map[player_y][player_x] = get_floor_type()
        add_object(item_player_is_on)
        show_text("Now carrying ", 0)
        sound('pickup')
        pygame.time.delay(300)
    else:
        show_text("You can't carry that!", 0)

def add_object(item):
    global selected_item, item_carrying
    in_my_pockets.append(item)
    item_carrying = item
    selected_item = len(in_my_pockets) - 1
    display_inventory()
    props[item][0] = 0

def display_inventory():
    pygame.draw.rect(screen, (0, 0, 0), (0, 550, 690, 100))

    if len(in_my_pockets) == 0:
        return

    start_display = (selected_item // 16) * 16
    list_to_show = in_my_pockets[start_display : start_display + 16]
    selected_marker = selected_item % 16

    for item_counter in range(len(list_to_show)):
        item_number = list_to_show[item_counter]
        image = objects[item_number][0]
        screen.blit(image, (25 + (46 * item_counter), 560))

    box_left = (selected_marker * 46) - 3
    pygame.draw.rect(screen, WHITE, (22 + box_left, 555, 40, 40), 3)
    item_highlighted = in_my_pockets[selected_item]
    description = 'description'

    myfont = pygame.font.SysFont('Arial', 20)
    textsurface = myfont.render(description, False, WHITE)

    screen.blit(textsurface,(20, 600))

def drop_object(old_y, old_x):
    global room_map, props
    if room_map[old_y][old_x] in [0]:
        props[item_carrying][0] = current_room
        props[item_carrying][1] = old_y
        props[item_carrying][2] = old_x
        room_map[old_y][old_x] = item_carrying
        show_text("You have dropped ", 0)
        sound('drop')
        remove_object(item_carrying)
        pygame.time.delay(300)
        print(props)
    else:
        show_text("You can't drop that here.", 0)
        pygame.time.delay(300)

def remove_object(item):
    global selected_item, in_my_pockets, item_carrying
    in_my_pockets.remove(item)
    selected_item = selected_item - 1
    if selected_item < 0:
        selected_item = 0
    if len(in_my_pockets) == 0:
        item_carrying = False
    else:
        item_carrying = in_my_pockets[selected_item]
    display_inventory()

def examine_object():
    item_player_is_on = get_item_under_player()
    left_tile_of_item = find_object_start_x()
    if item_player_is_on in [0, 2]:
        return
    description = "You see: "
    for prop_number, details in props.items():
        if (details[0] == current_room):
            if (details[1] == player_y
                and details[2] == left_tile_of_item
                and room_map[details[1]][details[2]] != prop_number):
                add_object(prop_number)
                description = "You found "
                sound('combine')
    show_text(description, 0)
    pygame.time.delay(300)

#USE OBJECTS#

def use_object():
    global room_map, props, item_carrying, selected_item, energy
    global in_my_pockets, game_over

    use_message = "You fiddle around with it but don't get anywhere."
    standard_responses = {
        9: "Hot!"
        }

    item_player_is_on = get_item_under_player()
    for this_item in [item_player_is_on, item_carrying]:
        if this_item in standard_responses:
            use_message = standard_responses[this_item]

    show_text(use_message, 0)
    pygame.time.delay(500)

#MAKE MAP#

def get_floor_type():
    return 0

def generate_map():
    global room_map, top_left_x, top_left_y
    room_data = GAME_MAP[current_room]
    
    room_map = [[0] * ROOM_WIDTH]
    
    for y in range(ROOM_HEIGHT):
        room_map.append([0] * ROOM_WIDTH)

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

    for prop_number, prop_info in props.items():
        prop_room = prop_info[0]
        prop_y = prop_info[1]
        prop_x = prop_info[2]
        if (prop_room == current_room and
            room_map[prop_y][prop_x] in [0]):
            room_map[prop_y][prop_x] = prop_number
            image_here = objects[prop_number][0]
            image_width = image_here.get_width()
            image_width_in_tiles = int(image_width / TILE_SIZE)
            for tile_number in range(1, image_width_in_tiles):
                room_map[prop_y][prop_x + tile_number] = 255

#GAME LOOP#
                
def start_room():
    show_text("You are here: " + room_name, 0)

def game_loop():
    global player_x, player_y, current_room
    global from_player_x, from_player_y
    global player_image, player_image_shadow 
    global selected_item, item_carrying, energy 
    global player_offset_x, player_offset_y
    global player_frame, player_direction
    
    if player_frame > 0:
        player_frame += 1
        pygame.time.delay(50)
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

    if keys[pygame.K_g]:
        pick_up_object()

    if keys[pygame.K_TAB] and len(in_my_pockets) > 0:
        selected_item += 1
        if selected_item > len(in_my_pockets) -1:
            selected_item = 0
        item_carrying = in_my_pockets[selected_item]
        display_inventory()
        pygame.time.delay(300)

    if keys[pygame.K_d] and item_carrying:
        drop_object(old_player_y, old_player_x)

    if keys[pygame.K_SPACE]:
        examine_object()

    if keys[pygame.K_u]:
        use_object()

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

    floor_type = get_floor_type()

    for y in range(ROOM_HEIGHT):
        for x in range(ROOM_WIDTH):
            draw_image(objects[floor_type][0], y, x)
            if room_map[y][x] in items_player_may_stand_on:
                draw_image(objects[room_map[y][x]][0], y, x)

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

def show_text(text_to_show, line_number):
    if game_over:
        return

    text_lines = [15, 50]
    myfont = pygame.font.SysFont('Arial', 25)
    textsurface = myfont.render(text_to_show, False, (0, 255, 0))

    pygame.draw.rect(screen, (0, 0, 0), (0, text_lines[line_number], 800, 35))
    screen.blit(textsurface,(20, text_lines[line_number]))
    
#mainloop#
    
clock = pygame.time.Clock()
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
           
    clock.tick(16)
    pygame.time.delay(10)

    generate_map()
    draw()
    display_inventory()
    game_loop()
    
    pygame.display.update()

pygame.quit()
