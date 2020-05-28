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

current_room = 6

top_left_x = 0
top_left_y = 100

ROOM_WIDTH = 23
ROOM_HEIGHT  = 16
TILE_SIZE = 30

player_y, player_x = 8, 9
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

player_direction = "up"
player_frame = 0
player_image = PLAYER[player_direction][player_frame]
player_offset_x, player_offset_y = 0, 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

plank, navigation_system, gunpowder, oxygen_tank = False, False, False, False

original_room = [0, 0, 0]
help_menu = False
speech_bubble = True
speech_text = 53

#MAP#

MAP_WIDTH = 4
MAP_HEIGHT = 3
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [["Room 0 - where unused objects are kept"]]

GAME_MAP += [
    #["Room name"]
    ["Base of Mountain"], #room 1
    ["Jungle"], #room 2
    ["Jungle"], #room 3
    ["Raccoon Workshop"], #room 4
    ["Raccoon Treehouse"], #room 5
    ["Raccoon House"], #room 6
    ["Jungle"], #room 7
    ["Beach"], #room 8
    ["Jungle"], #room 9
    ["Jungle"], #room 10
    ["Jungle meets beach"], #room 11
    ["Beach"], #room 12
    ]

#OBJECTS#

objects = {
    #Object number : [Image, Shadow, Description]
    0: [image('grass'), None, None],
    1: [image('transparent'), None, None], #dirt
    2: [image('sand'), None, None],
    3: [image('jungle_sand'), None, None],
    4: [image('jungle_sand_stones'), None, "Stones"],
    5: [image('wall'), None, "Wooden walls"],
    6: [image('wall_1'), None, "Wooden walls"],
    7: [image('longwall'), None, "Wooden walls"],
    8: [image('stones'), None, "Stones"],
    9: [image('shortstones'), None, "Stones"],
    10: [image('longstones'), None, "Stones"],
    11: [image('rocks'), None, "Rocks"],
    12: [image('tree'), None, "A tree with blue leaves"],
    13: [image('row_of_trees'), None, "A tree with blue leaves"],
    14: [image('treehouse'), None, "A treehouse, \
with a staircase made from wooden planks"],
    15: [image('palm_tree'), None, "A palm tree"],
    16: [image('sticky_plant'), None, "A sticky plant"],
    17: [image('mountain'), None, "The base of a mountain"],
    18: [image('sea'), None, "The sea"],
    19: [image('raccoon'), None, "A friendly raccoon"],
    20: [image('raccoon_2'), None, "A raccoon skilled at crafting"],
    21: [image('baby_raccoon'), None, "A baby raccoon"],
    22: [image('fireplace'), None, "A charcoal fireplace"],
    23: [image('table'), None, "A crafting table"],
    24: [image('spaceship_broken'), None, "The remains of my spaceship"],
    25: [image('spaceship'), None, "The spaceship"],
    26: [image('destroyed_treehouse'), None, "A destroyed tree house"],
    27: [image('iron_ore'), None, "Something shiny"],
    28: [image('charcoal'), None, "Some charcoal", "charcoal"],
    29: [image('stick'), None, "A strong and sturdy stick", "stick"],
    30: [image('stick'), None, "A strong and sturdy stick", "stick"],
    31: [image('iron_ore'), None, "A piece of iron ore", "iron ore"],
    32: [image('rocks'), None, "A large piece of stone", "large stone"],
    33: [image('pickaxe_stone'), None, "A long piece of stone",
         "long stone"],
    34: [image('pickaxe'), None, "A pickaxe", "pickaxe"],
    35: [image('axe'), None, "An axe", "axe"],
    36: [image('seashell'), None, "A seashell", "a seashell"],
    37: [image('oxygen_tank'), None, "An oxygen tank, with a hole on \
its side", "a leaking oxygen tank"],
    38: [image('oxygen_tank'), None, "A sealed oxygen tank",
         "sealed oxygen tank"],
    39: [image('sulfur'), None, "Sulfur", "sulfur"],
    40: [image('gunpowder'), None, "Gunpowder", "gunpowder"],
    41: [image('sticky'), None, "Sticky goo", "sticky goo"],
    42: [image('letter'), None, "A letter I wrote to myself",
         "letter to self"],
    43: [image('manual'), None, "The manual to fix the spaceship",
         "a manual to fix the spaceship"],
    44: [image('log'), None, "A piece of log", "a log"],
    45: [image('planks'), None, "A piece of wooden plank", "wooden plank"],
    46: [image('spoilt_machine'), None, "Navigation system. It is missing a \
piece of iron", "spoilt system"],
    47: [image('machine'), None, "Navigation system", "navigation system"],
    48: [image('mixture_1'), None, "Mixture of sulfur and seashell.\
Needs charcoal to make gunpowder",
         "a mixture"],
    49: [image('mixture_2'), None, "Mixture of sulfur and charcoal.\
Needs seashell to make gunpowder",
         "a mixture"],
    50: [image('mixture_3'), None, "Mixture of charcoal and seashell.\
Needs sulfur to make gunpowder",
         "a mixture"],
    51: [image('help'), None, None],
    52: [image('speech'), None, None],
    53: [image('speech_1'), None, None], # raccoon 1
    54: [image('speech_2'), None, None], # baby raccoon
    55: [image('speech_3'), None, None], # baby raccoon
    56: [image('speech_4'), None, None], # raccoon 2
    250: [image('transparent'), None,"Not much to see here"],
    251: [image('transparent'), None, "The mountain"],
    252: [image('transparent'), None, "The sea"],
    253: [image('transparent'), None, "Not much to see here"],
    254: [image('transparent'), None, "A tree with blue leaves"]
    }

items_player_may_carry = list(range(28, 51))
items_player_may_stand_on = items_player_may_carry + list(range(0, 4))

#SCENERY#

scenery = {
    #room number: [[object number, y position, x position]...]
    1: [[12, 4, 7], [12, 4, 10], [12, 4, 13], [12, 4, 16], [12, 5, 19],
        [12, 15, 7], [12, 15, 10], [12, 15, 13], [12, 15, 16], [12, 14, 19],
        [17, 15, 0], [251, 5, 6], [251, 6, 6], [251, 7, 6], [251, 8, 6],
        [251, 9, 6], [251, 10, 6], [251, 12, 6], [251, 13, 6], [251, 14, 6]],
    2: [[13, 4, 0], [13, 15, 0]],
    3: [[12, 15, 0], [12, 15, 3], [12, 15, 6], [12, 15, 13],
        [12, 15, 16], [12, 15, 19], [13, 4, 0]],
    4: [[5, 6, 9], [5, 7, 9], [5, 12, 9], [5, 6, 18], [5, 7, 18],
        [5, 8, 18], [5, 9, 18], [5, 10, 18], [5, 11, 18], [5, 12, 18],
        [6, 11, 9], [7, 6, 9], [7, 13, 9], [12, 14, 19], [12, 12, 19],
        [12, 10, 19], [12, 8, 19], [12, 6, 19],[13, 4, 0], [13, 15, 0],
        [20, 8, 16], [23, 8, 14], [254, 5, 21]],
    5: [[9, 6, 5], [9, 6, 8], [9, 6, 11], [9, 6, 14], [9, 7, 2],
        [9, 7, 17], [9, 7, 19],[12, 5, 4], [12, 5, 16], [12, 6, 1],
        [12, 6, 18], [12, 8, 0], [12, 10, 0], [12, 12, 0], [12, 14, 0],
        [12, 15, 3], [12, 15, 6], [12, 15, 13], [12, 15, 16], [12, 15, 19],
        [14, 7, 6], [21, 8, 5], [254, 9, 0], [254, 11, 0],
        [254, 13, 0], [254, 15, 0]],
    6: [[5, 5, 11], [5, 6, 11], [5, 11, 11], [5, 12, 11], [5, 5, 20],
        [5, 6, 20], [5, 7, 20], [5, 8, 20], [5, 9, 20], [5, 10, 20],
        [5, 11, 20], [5, 12, 20], [6, 10, 11], [7, 4, 11], [7, 13, 11],
        [8, 2, 22], [8, 3, 22], [8, 4, 22], [8, 5, 22], [8, 6, 22],
        [8, 7, 22], [8, 8, 22], [8, 9, 22], [8, 10, 22], [8, 11, 22],
        [8, 12, 22], [8, 13, 22], [8, 14, 22], [9, 6, 0], [9, 10, 0],
        [8, 2, 3], [8, 3, 3], [8, 4, 3], [8, 5, 3], [8, 11, 3],
        [8, 12, 3], [8, 13, 3], [8, 14, 3], [10, 1, 3], [10, 15, 3],
        [19, 6, 9], [22, 4, 6], [52, 15, 1], [53, 15, 2]],
    7: [[12, 4, 0], [12, 4, 3], [12, 4, 6], [12, 4, 13], [12, 4, 16],
        [12, 4, 19], [12, 15, 0], [12, 15, 3], [12, 15, 6], [12, 15, 13],
        [12, 15, 16], [12, 15, 19], [12, 6, 0], [12, 8, 0], [12, 10, 0],
        [12, 12, 0], [12, 14, 0], [12, 6, 19], [12, 8, 19], [12, 10, 19],
        [12, 12, 19], [12, 14, 19], [254, 3, 8], [254, 1, 14],
        [254, 2, 14], [254, 3, 14], [254, 5, 3], [254, 7, 3],
        [254, 9, 3], [254, 13, 3], [254, 5, 19], [254, 7, 19],
        [254, 9, 19], [254, 11, 19], [254, 13, 19], [254, 1, 8],
        [254, 2, 8]],
    8: [[15, 7, 0], [15, 7, 5], [15, 7, 9], [15, 11, 0], [15, 15, 0],
        [18, 15, 16], [252, 0, 16], [252, 1, 16], [252, 2, 16], [252, 3, 16],
        [252, 4, 16], [252, 5, 16], [252, 6, 16], [252, 7, 16], [252, 8, 16],
        [252, 9, 16], [252, 10, 16], [252, 11, 16], [252, 12, 16], [252, 13, 16],
        [252, 14, 16], [253, 8, 0], [253, 9, 0], [253, 10, 0], [253, 12, 0],
        [253, 13, 0], [253, 14, 0], [253, 16, 0]],
    9: [[12, 3, 0], [12, 5, 0], [12, 7, 0], [12, 9, 0], [12, 11, 0],
        [12, 13, 0], [12, 3, 19], [12, 5, 19], [12, 7, 19], [13, 15, 0],
        [254, 6, 3],[254, 8, 3], [254, 10, 3], [254, 12, 3], [254, 14, 3],
        [254, 1, 19], [254, 2, 19], [254, 4, 19], [254, 6, 19]],
    10: [[13, 4, 0], [13, 15, 0], [16, 5, 5]],
    11: [[4, 15, 0], [3, 15, 16], [12, 15, 1], [12, 15, 4], [12, 4, 0],
         [12, 4, 3], [12, 4, 6], [12, 4, 13], [12, 4, 16], [253, 4, 19],
         [253, 4, 20], [253, 4, 21], [253, 4, 22]],
    12: [[10, 15, 0], [18, 15, 16], [24, 5, 3], [252, 0, 16],
         [252, 1, 16], [252, 2, 16], [252, 3, 16], [252, 4, 16],
         [252, 5, 16], [252, 6, 16], [252, 7, 16], [252, 8, 16],
         [252, 9, 16], [252, 10, 16], [252, 11, 16], [252, 12, 16],
         [252, 13, 16], [252, 14, 16], [250, 3, 3], [250, 3, 4],
         [250, 3, 5], [250, 3, 6], [250, 4, 3], [250, 4, 4], [250, 4, 5],
         [250, 4, 6]]
    }

#PROPS#

props = {
    #object number: [room, y, x]
    27: [1, 11, 6], # Iron ore rock
    28: [6, 4, 6], # Charcoal
    29: [6, 4, 5], # Stick
    30: [6, 3, 5], # Stick
    31: [0, 0, 0], # Iron ore
    32: [9, 10, 4], # Large stone for axe
    33: [2, 11, 2], # Long stone for pickaxe
    34: [0, 0, 0], # Pickaxe
    35: [0, 0, 0], # Axe
    36: [8, 10, 8], # Seashell
    37: [8, 8, 9], # Unsealed oxygen tank
    38: [0, 0, 0], # Oxygen tank
    39: [4, 7, 12], # Sulfur
    40: [0, 0, 0], # Gunpowder
    41: [10, 5, 5], # Sticky goo under sticky plant
    42: [0, 0, 0], # Letter to self
    43: [12, 5, 3], # Manual under broken spaceship
    44: [0, 0, 0], # Log
    45: [0, 0, 0], # Plank
    46: [12, 14, 14], # Navigation system missing a piece of iron
    47: [0, 0, 0], # Navigation system
    48: [0, 0, 0], # Sulfur + Seashell mixture
    49: [0, 0, 0], # Sulfur + Charcoal mixture
    50: [0, 0, 0], # Charcoal + Seashell mixture
    }

in_my_pockets = [42, 45, 47, 40, 38]
selected_item = 0
item_carrying = in_my_pockets[selected_item]

RECIPES = [
    [29, 33, 34], # Stick + long stone = pickaxe
    [30, 33, 34], # Stick + long stone = pickaxe
    [29, 32, 35], # Stick + large stone = axe
    [30, 32, 35], # Stick + large stone = axe
    [31, 46, 47], # Iron ore + spoilt navigation system = navigation system
    [37, 41, 38], # Unsealed oxygen tank + sticky goo = oxygen tank
    [39, 36, 48], # Sulfur + Seashell = Mixture 1
    [48, 28, 40], # Mixture 1 + Charcoal = Gunpowder
    [39, 28, 49], # Sulfur + charcoal = Mixture 2
    [49, 36, 40], # Mixture 2 + Seashell = Gunpowder
    [28, 36, 50], # Charcoal + Seashell = Mixture 3
    [50, 39, 40] # Mixture 3 + Sulfur = Gunpowder
    ]

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
        show_text("Now carrying " + objects[item_player_is_on][3], 0)
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
    pygame.draw.rect(screen, BLACK, (0, 550, 690, 100))

    if len(in_my_pockets) == 0:
        return

    start_display = (selected_item // 14) * 14
    list_to_show = in_my_pockets[start_display : start_display + 14]
    selected_marker = selected_item % 14

    for item_counter in range(len(list_to_show)):
        item_number = list_to_show[item_counter]
        image = objects[item_number][0]
        screen.blit(image, (25 + (46 * item_counter), 560))

    box_left = (selected_marker * 46) - 3
    pygame.draw.rect(screen, WHITE, (22 + box_left, 555, 40, 40), 3)
    item_highlighted = in_my_pockets[selected_item]
    description = objects[item_highlighted][2]

    myfont = pygame.font.SysFont('Verdana', 20)
    textsurface = myfont.render(description, False, WHITE)

    screen.blit(textsurface,(20, 600))

def drop_object(old_y, old_x):
    global room_map, props
    if room_map[old_y][old_x] in [0, 1, 2, 3]:
        props[item_carrying][0] = current_room
        props[item_carrying][1] = old_y
        props[item_carrying][2] = old_x
        room_map[old_y][old_x] = item_carrying
        show_text("You have dropped " + objects[item_carrying][3], 0)
        sound('drop')
        remove_object(item_carrying)
        pygame.time.delay(300)
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
    global speech_bubble, speech_text
    
    item_player_is_on = get_item_under_player()
    left_tile_of_item = find_object_start_x()
    
    if item_player_is_on in [0, 1, 2, 3]:
        return

    if item_player_is_on in [19, 20, 21]: # dialogue with raccoons
        speech_bubble = True
        if item_player_is_on == 19: # raccoon 1
            speech_text = 53
        elif item_player_is_on == 20: # raccoon 2
            speech_text = 56
        elif item_player_is_on == 21: # baby raccoon
            speech_text = 54
        scenery[current_room].append([52, 15, 1]) # speech bubble
        scenery[current_room].append([speech_text, 15, 2])
        pygame.time.delay(500)
    
    description = "You see: " + objects[item_player_is_on][2]
    for prop_number, details in props.items():
        if (details[0] == current_room):
            if (details[1] == player_y
                and details[2] == left_tile_of_item
                and room_map[details[1]][details[2]] != prop_number):
                add_object(prop_number)
                description = "You found " + objects[prop_number][3]
                sound('combine')
    show_text(description, 0)
    pygame.time.delay(300)

#USE OBJECTS#

def use_object():
    global room_map, props, item_carrying, selected_item, in_my_pockets
    global plank, navigation_system, gunpowder, oxygen_tank, game_over

    use_message = "You fiddle around with it but don't get anywhere."
    standard_responses = {
        28: "Hot!"
        }

    item_player_is_on = get_item_under_player()
    for this_item in [item_player_is_on, item_carrying]:
        if this_item in standard_responses:
            use_message = standard_responses[this_item]

    if item_carrying == 34 and item_player_is_on == 27: # use pickaxe
        use_message = "You found a piece of iron ore!"
        add_object(31)
        sound('combine')
        props[item_player_is_on][0] = 0
        scenery[1].append([11, 11, 6])

    if item_carrying == 35: # use axe
        if item_player_is_on in [12, 13]:
            use_message = "You chopped off a piece of log"
            add_object(44)
            sound('combine')
        elif item_player_is_on == 14:
            use_message = "You chopped off a piece of plank"
            add_object(45)
            sound('combine')
            scenery[5].remove([14, 7, 6])
            scenery[5].append([26, 7, 6])

    if item_carrying == 44 and item_player_is_on == 23: # use crafting table
        use_message = "You crafted planks from the log"
        add_object(45)
        remove_object(44)
        sound('combine')

    if item_player_is_on in [24, 250]: # broken spaceship
        if item_carrying == 45: # fix plank
            use_message = "You fix the plank to the spaceship"
            plank = True
            remove_object(45)
        elif item_carrying == 47: # fix navigation system
            use_message = "You fix the navigation system to the spaceship"
            navigation_system = True
            remove_object(47)
        elif item_carrying == 40: # add gunpowder
            use_message = "You add gunpowder into the rocket booster"
            gunpowder = True
            remove_object(40)
        elif item_carrying == 38: # fix oxygen tank
            use_message = "You fix the oxygen tank to the spaceship"
            oxygen_tank = True
            remove_object(38)
        if plank == True and navigation_system == True and \
           gunpowder == True and oxygen_tank == True:
            scenery[12].remove([24, 5, 3])
            scenery[12].append([25, 5, 3])
        sound('combine')

    for recipe in RECIPES:
        ingredient1 = recipe[0]
        ingredient2 = recipe[1]
        combination = recipe[2]
        if (item_carrying == ingredient1
            and item_player_is_on == ingredient2) \
            or (item_carrying == ingredient2
                and item_player_is_on == ingredient1):
            use_message = "You combine " + objects[ingredient1][3] \
                          + " and " + objects[ingredient2][3] \
                          + " to make " + objects[combination][3]
            if item_player_is_on in props.keys():
                props[item_player_is_on][0] = 0
                room_map[player_y][player_x] = get_floor_type()
            in_my_pockets.remove(item_carrying)
            add_object(combination)
            sound('combine')

    show_text(use_message, 0)
    pygame.time.delay(500)

#MAKE MAP#

def get_floor_type():
    if current_room in [8, 12]:
        return 2 # Sand
    else:
        return 0 # Grass

def generate_map():
    global room_map, top_left_x, top_left_y
    floor_type = get_floor_type()
    
    room_data = GAME_MAP[current_room]
    
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

    for prop_number, prop_info in props.items():
        prop_room = prop_info[0]
        prop_y = prop_info[1]
        prop_x = prop_info[2]
        if (prop_room == current_room and
            room_map[prop_y][prop_x] in [0, 1, 2, 3]): # Check for floor types
            room_map[prop_y][prop_x] = prop_number
            image_here = objects[prop_number][0]
            image_width = image_here.get_width()
            image_width_in_tiles = int(image_width / TILE_SIZE)
            for tile_number in range(1, image_width_in_tiles):
                room_map[prop_y][prop_x + tile_number] = 255

#GAME LOOP#
                
def start_room():
    show_text("You are here: " + GAME_MAP[current_room][0], 0)

def game_loop():
    global player_x, player_y, current_room
    global from_player_x, from_player_y
    global player_image, player_image_shadow 
    global selected_item, item_carrying
    global player_offset_x, player_offset_y
    global player_frame, player_direction
    global speech_bubble, speech_text
    
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

    if player_x == ROOM_WIDTH: #goes through door on the right
        current_room += 1
        generate_map()
        player_x = 0
        player_y = int(ROOM_HEIGHT / 2)
        player_frame = 0
        start_room()
        return

    if player_x == -1: #goes through door on the left
        current_room -= 1
        generate_map()
        player_x = ROOM_WIDTH - 1
        player_y = int(ROOM_HEIGHT / 2)
        player_frame = 0
        start_room()
        return

    if player_y == ROOM_HEIGHT: #goes through door at the bottom
        current_room += MAP_WIDTH
        generate_map()
        player_y = 0
        player_x = int(ROOM_WIDTH / 2)
        player_frame = 0
        start_room()
        return
    
    if player_y == -1: #goes through door at the top
        current_room -= MAP_WIDTH
        generate_map()
        player_y = ROOM_HEIGHT - 1
        player_x = int(ROOM_WIDTH / 2)
        start_room()
        return

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

    if keys[pygame.K_h] and [51, 13, 0] not in scenery[current_room]:
        show_help()

    if keys[pygame.K_RETURN]:
        if help_menu == True:
            remove_help()

        if speech_bubble:
            scenery[current_room].remove([speech_text, 15, 2])
            scenery[current_room].remove([52, 15, 1]) # remove speech bubble
            speech_bubble = False 

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
    myfont = pygame.font.SysFont('Verdana', 20)
    textsurface = myfont.render(text_to_show, False, (0, 255, 0))

    pygame.draw.rect(screen, (0, 0, 0), (0, text_lines[line_number], 800, 35))
    screen.blit(textsurface,(20, text_lines[line_number]))

def show_help():
    global help_menu, original_room
    original_room = scenery[current_room].copy()
    help_menu = True
    scenery[current_room].append([51, 13, 0])
    print(original_room)
    pygame.time.delay(500)

def remove_help():
    global help_menu, original_room
    scenery[current_room] = original_room
    help_menu = False
    print(scenery[current_room])
    
#mainloop#
    
clock = pygame.time.Clock()
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
           
    clock.tick(40)
    
    generate_map()
    draw()
    display_inventory()
    game_loop()
    
    pygame.display.update()

pygame.quit()
