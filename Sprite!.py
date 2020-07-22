import pygame
import os
import random
import pickle

pygame.init()
pygame.display.set_caption("Sprite!")

#VARIABLES#
WIDTH = 690
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))

current_path = os.path.dirname('Sprite!.py')
image_path = os.path.join(current_path, 'images')
sound_path = os.path.join(current_path, 'sounds')
path = os.getcwd() + "\\save\\"

def image(image):
    return pygame.image.load(
        os.path.join(image_path, image + '.png')).convert_alpha()

def sound(sound):
    soundObj = pygame.mixer.Sound(os.path.join(sound_path, sound + '.wav'))
    soundObj.play()

top_left_x = 0
top_left_y = 100

ROOM_WIDTH = 23
ROOM_HEIGHT  = 16
TILE_SIZE = 30

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

PLAYER_SHADOW = {
    "left": [image('astronaut_left_shadow'), image('astronaut_left_1_shadow'),
        image('astronaut_left_2_shadow'), image('astronaut_left_3_shadow'),
        image('astronaut_left_4_shadow')
        ],
    "right": [image('astronaut_right_shadow'), image('astronaut_right_1_shadow'),
        image('astronaut_right_2_shadow'),
        image('astronaut_right_3_shadow'), image('astronaut_right_4_shadow')
        ],
    "up": [image('astronaut_back_shadow'), image('astronaut_back_1_shadow'),
        image('astronaut_back_2_shadow'), image('astronaut_back_3_shadow'),
        image('astronaut_back_4_shadow')
        ],
    "down": [image('astronaut_front_shadow'), image('astronaut_front_1_shadow'),
        image('astronaut_front_2_shadow'), image('astronaut_front_3_shadow'),
        image('astronaut_front_4_shadow')
        ]
}

PLAYER_DOG = {
    "left": [image('astronaut_left_dog'), image('astronaut_left_dog_1'),
        image('astronaut_left_dog_2'), image('astronaut_left_dog_3'),
        image('astronaut_left_dog_4')
        ],
    "right": [image('astronaut_right_dog'), image('astronaut_right_dog_1'),
        image('astronaut_right_dog_2'), image('astronaut_right_dog_3'),
        image('astronaut_right_dog_4')
        ],
    "up": [image('astronaut_back_dog'), image('astronaut_back_dog_1'),
        image('astronaut_back_dog_2'), image('astronaut_back_dog_3'),
        image('astronaut_back_dog_4')
        ],
    "down": [image('astronaut_front'), image('astronaut_front_1'),
        image('astronaut_front_2'), image('astronaut_front_3'),
        image('astronaut_front_4')
        ]
}

PLAYER_DOG_SHADOW = {
    "left": [image('astronaut_left_dog_s'), image('astronaut_left_dog_1_s'),
        image('astronaut_left_dog_2_s'), image('astronaut_left_dog_3_s'),
        image('astronaut_left_dog_4_s')
        ],
    "right": [image('astronaut_right_dog_s'), image('astronaut_right_dog_1_s'),
        image('astronaut_right_dog_2_s'),
        image('astronaut_right_dog_3_s'), image('astronaut_right_dog_4_s')
        ],
    "up": [image('astronaut_back_shadow'), image('astronaut_back_1_shadow'),
        image('astronaut_back_2_shadow'), image('astronaut_back_3_shadow'),
        image('astronaut_back_4_shadow')
        ],
    "down": [image('astronaut_front_shadow'), image('astronaut_front_1_shadow'),
        image('astronaut_front_2_shadow'), image('astronaut_front_3_shadow'),
        image('astronaut_front_4_shadow')
        ]
}

PLAYER_FISH = {
    "left": [image('astronaut_fishing'), image('astronaut_left_1'),
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

player_image_shadow = PLAYER_SHADOW["up"][0]

PILLARS = {
    5: [image('wall_70')],
    80: [image('ice_wall_70')],
    150: [image('wall_70')]
    }

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#MAP#

MAP_WIDTH = 4
MAP_HEIGHT = 6
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [["Room 0 - where unused objects are kept"]]

GAME_MAP += [
    #["Room name"] 
    
    #planet 1
    ["Raccoon Treehouse"], #room 1
    ["Raccoon House"], #room 2
    ["Beach"], #room 3
    ["Empty"], #room 4
    ["Jungle"], #room 5
    ["Jungle meets beach"], #room 6
    ["Beach"], #room 7
    ["Empty"], #room 8
    ["Base of Mountain"], #room 9
    ["Raccoon Workshop"], #room 10
    ["Empty"], #room 11
    ["Empty"], #room 12
    
    #planet 2
    ["Student's House"], #room 13
    ["Road"], #room 14
    ["Fisherman's House"], #room 15
    ["Abandoned research centre"], #room 16
    ["Penguin Town Hall"], #room 17
    ["Road"], #room 18
    ["Scientist's house"], #room 19
    ["Abandoned research centre"], #room 20
    ["Spaceship Landing Area"], #room 21
    ["Road"], #room 22
    ["Road"], #room 23
    ["Road with a dead end"], #room 24

    #planet 3
    ["River"], #room 25
    ["Village"], #room 26
    ["The Maze"], #room 27
    ["Empty"], #room 28
    ["River"], #room 29
    ["Village"], #room 30
    ["Village"], #room 31
    ["Empty"], #room 32
    ["Spaceship Landing Area"], #room 33
    ["Village"], #room 34
    ["Village"], #room 35

    #earth
    ["Earth"] #room 36
    ]

#OBJECTS#

objects = {
    #Object number : [Image, Shadow, Description]

    #planet 1
    0: [image('grass'), None, None],
    1: [image('transparent'), None, None], #dirt
    2: [image('sand'), None, None],
    3: [image('jungle_sand'), None, None],
    4: [image('jungle_sand_2'), None, "Stones"],
    5: [image('wall'), None, "Wooden walls"],
    6: [image('wall_1'), None, "Wooden walls"],
    7: [image('longwall'), None, "Wooden walls"],
    8: [image('stones'), None, "Stones"],
    9: [image('shortstones'), None, "Stones"],
    10: [image('longstones'), None, "Stones"],
    11: [image('rocks'), None, "Rocks"],
    12: [image('tree'), image('tree_shadow'), "A tree with blue leaves"],
    13: [image('row_of_trees'), None, "A tree with blue leaves"],
    14: [image('treehouse'), image('treehouse_shadow'), "A treehouse, \
with a staircase made from wooden planks"],
    15: [image('palm_tree'), image('palm_tree_shadow'), "A palm tree"],
    16: [image('sticky_plant'), image('sticky_plant_shadow'), "A sticky plant"],
    17: [image('mountain'), None, "The base of a mountain"],
    18: [image('sea'), None, "The sea"],
    19: [image('raccoon'), image('raccoon_shadow'), "A friendly raccoon"],
    20: [image('raccoon_2'), image('raccoon_2_shadow'), "A raccoon skilled at crafting"],
    21: [image('baby_raccoon'), image('baby_raccoon_shadow'), "A baby raccoon"],
    22: [image('fireplace'), None, "A charcoal fireplace"],
    23: [image('table'), image('table_shadow'), "A crafting table"],
    24: [image('spaceship_broken'), None, "The remains of my spaceship"],
    25: [image('spaceship'), image('spaceship_shadow'), "The spaceship"],
    26: [image('destroyed_treehouse'), image('treehouse_shadow'), "A destroyed tree house"],
    27: [image('iron_ore'), None, "Something shiny"],
    28: [image('charcoal'), None, "Some charcoal", "charcoal"],
    29: [image('stick'), None, "A strong and sturdy stick", "a stick"],
    30: [image('stick'), None, "A strong and sturdy stick", "a stick"],
    31: [image('iron_ore'), None, "A piece of iron ore", "iron ore"],
    32: [image('rocks'), None, "A large piece of stone", "a large stone"],
    33: [image('pickaxe_stone'), None, "A long piece of stone",
         "long stone"],
    34: [image('pickaxe'), None, "A pickaxe", "pickaxe"],
    35: [image('axe'), None, "An axe", "an axe"],
    36: [image('seashell'), None, "A seashell", "a seashell"],
    37: [image('oxygen_tank'), None, "An oxygen tank, with a hole on \
its side", "leaking O2 tank"],
    38: [image('oxygen_tank'), None, "A sealed oxygen tank",
         "oxygen tank"], 
    39: [image('sulfur'), None, "Sulfur", "sulfur"],
    40: [image('gunpowder'), None, "Gunpowder", "gunpowder"], 
    41: [image('sticky'), None, "Sticky goo", "sticky goo"],
    43: [image('manual'), None, "The spaceship manual",
         "a manual to fix the spaceship"],
    44: [image('log'), None, "A piece of log", "a log"], 
    45: [image('planks'), None, "A piece of wooden plank", "wooden plank"],
    46: [image('spoilt_machine'), None, "Navigation system. It is missing a \
piece of magnet.", "spoilt system"],
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
    51: [image('manual_page1'), None, None],
    52: [image('manual_page2'), None, None],
    53: [image('speech_1'), None, None], # raccoon 1
    54: [image('speech_2'), None, None], # baby raccoon
    55: [image('speech_3'), None, None], # baby raccoon
    56: [image('speech_4'), None, None], # raccoon 2

    #planet 2
    57: [image('road_tile'), None, None],
    58: [image('concrete'), None, None],
    59: [image('ice_bricks'), None, "Bricks from ice"],
    60: [image('ice_bricks_long'), None, "Bricks from ice"],
    61: [image('ice_bricks_short'), None, "Bricks from ice"],
    62: [image('sea_with_ice_1'), None, None],
    63: [image('sea_with_ice_2'), None, None],
    64: [image('sea_with_ice_3'), None, None],
    65: [image('sea_with_ice_4'), None, None],
    66: [image('sea_with_ice_5'), None, None],
    67: [image('sea_with_ice_6'), None, None],
    68: [image('sea_with_ice_7'), None, None],
    69: [image('sea_with_ice_8'), None, None],
    70: [image('sea_with_ice_9'), None, None],
    71: [image('sea_with_ice_10'), None, None],
    72: [image('sea_with_ice_11'), None, None],
    73: [image('penguin_1'), image('penguin_1_shadow'), "The fisherman"],
    74: [image('penguin_2'), image('penguin_1_shadow'), "The scientist"],
    75: [image('penguin_3'), image('penguin_3_shadow'), "The student"],
    76: [image('penguin_mayor'), image('penguin_mayor_shadow'), "The Penguin Mayor"],
    77: [image('spaceship'), image('spaceship_shadow'), "Your spaceship. It needs fuel."],
    78: [image('crowd_1'), None, "A crowd of penguins"],
    79: [image('crowd_2'), None, "A crowd of penguins"],
    80: [image('ice_wall'), None, "Wall made of ice"],
    81: [image('ice_wall_long'), None, "Wall made of ice"],
    82: [image('fence'), image('fence_shadow'), "A fence"],
    83: [image('desk'), image('bed_shadow'), "A desk"],
    84: [image('pile_of_snow'), None, "Pile of snow"],
    85: [image('gate_unlocked_1'), None, "An open gate"],
    86: [image('gate_unlocked_2'), None, "An open gate"],
    87: [image('gate_locked'), image('gate_locked_shadow'), "A gate with a padlock"],
    88: [image('ice_wall_short'), None, "Wall made of ice"],
    89: [image('computer'), None, "Row of computers displaying strange \
images"],
    90: [image('door_closed'), None, "A door which is locked"],
    91: [image('door_open_1'), None, "An open door"],
    92: [image('door_open_2'), None, "An open door"],
    93: [image('steam_machine'), image('steam_machine_shadow'),
         "A machine which is left running"],
    94: [image('gate_left'), None, "A gate"],
    95: [image('gate_right'), None, "A gate"],
    96: [image('fishing_rod'), None, "A collection of fishing rods"],
    97: [image('whiteboard'), None, "A whiteboard filled with calculations"],
    98: [image('shelf_1'), image('shelf_shadow'), "A shelf with assorted items"],
    99: [image('shelf_2'), image('shelf_shadow'), "A shelf with assorted items"],
    100: [image('chair'), None, "A chair"],
    101: [image('chair_2'), None, "A chair"],
    102: [image('science_table'), None, "A table full of burning hot \
science equipment"],
    103: [image('science_table_2'), None, "Home experiments. The \
equipment is hot!"],
    104: [image('fishtank'), image('bed_shadow'), "A fish tank"],
    105: [image('bed_1'), image('bed_shadow'), "A bed"],
    106: [image('bed_2'), image('bed_shadow'), "A bed"],
    107: [image('bed_3'), image('bed_shadow'), "A bed"],
    108: [image('chair_3'), image('chair_3_shadow'), "A chair"],
    109: [image('chair_4'), None, "A chair"],
    110: [image('chair_5'), None, "A chair"],
    111: [image('table_2'), None, "A table"],
    112: [image('plant_pot'), image('plant_pot_shadow'), "A potted plant"],
    113: [image('cupboard'), image('cupboard_shadow'), "Cupboards"],
    114: [image('shelf_3'), image('cupboard_shadow'), "Some cupboards and shelves"],
    115: [image('table_3'), None, "A table with matches and fishing hooks"],
    116: [image('chair_6'), None, "A chair"],
    117: [image('research_table_1'), None, "A table full of books and \
research papers"],
    118: [image('research_table_2'), None, "A table full of books and \
research papers"],
    119: [image('trapdoor'), None, "A trapdoor"],
    120: [image('spaceship'), image('spaceship_shadow'), "Your spaceship. It is ready to \
take off."],
    121: [image('access_card'), None, "An access card", "an access card"],
    122: [image('key'), None, "An old and rusty key", "a key"],
    123: [image('shovel'), None, "A shovel", "a shovel"],
    124: [image('fuel'), None, "A fuel tank", "a fuel tank"],
    125: [image('choose_culprit'), None, None],
    126: [image('speech_5'), None, None], # Self
    127: [image('speech_6'), None, None], # Mayor
    128: [image('speech_7'), None, None],
    129: [image('speech_8'), None, None],
    130: [image('speech_9'), None, None], # Not convinced
    131: [image('speech_10'), None, None], # Convinced
    132: [image('speech_fisherman'), None, None],
    133: [image('speech_scientist'), None, None],
    134: [image('speech_student'), None, None],
    135: [image('hazard'), None, None],

    #planet 3
    136: [image('floor_tile'), None, None], 
    137: [image('tree_room7'), None, "A tree"], 
    138: [image('tree_room8'), None, "A tree"], 
    139: [image('rock_2'), None, "A rock"], 
    140: [image('rock_2_long'), None, "A rock"], 
    141: [image('spaceship'), image('spaceship_shadow'), "Your spaceship"], 
    142: [image('spaceship_dog'), image('spaceship_dog_shadow'),
          "Scout's spaceship! It needs to be attached to mine."], 
    143: [image('cat_jailer_1'), image('cat_shadow'), "A cat"], 
    144: [image('cat_jailer_2'), image('cat_shadow'), "A cat"], 
    145: [image('cat_river'), image('cat_shadow'), "A cat"], 
    146: [image('river'), None, "The river bank"], 
    147: [image('tree_room1'), None, "A tree"], 
    148: [image('tree_room4'), None, "A tree"], 
    149: [image('tree_2'), image('tree_2_shadow'), "A tree"], 
    150: [image('wall'), None, "Wooden walls"], 
    151: [image('longwall'), None, "Wooden walls"], 
    152: [image('wooden_door'), None, "The door is locked and Scout is \
inside!"], 
    153: [image('tree_room2_1'), None, "A tree"], 
    154: [image('tree_room2_2'), None, "A tree"], 
    155: [image('maze_fence'), None, "A fence"], 
    156: [image('tree_room5'), None, "A tree"], 
    157: [image('tree_room6_1'), None, "A tree"], 
    158: [image('tree_room6_2'), None, "A tree"], 
    159: [image('tree_room6_3'), None, "A tree"], 
    160: [image('tree_room6_4'), None, "A tree"], 
    161: [image('twine'), None, "A bunch of twines"], 
    162: [image('tree_room6_5'), None, "A tree"], 
    163: [image('tree_room6_6'), None, "A tree"], 
    164: [image('tree_room9_1'), None, "A tree"], 
    165: [image('tree_room9_2'), None, "A tree"], 
    166: [image('fence_2'), None, "A locked fence"], 
    167: [image('cats_unfriendly'), None, "A cat"], 
    168: [image('house'), image('house_shadow'), "The villagers' house"], 
    169: [image('spaceships'), image('spaceships_shadow'),
          "You and Scout's spaceship"], 
    170: [image('fence_2_open'), None, "An open fence"], 
    171: [image('fishing_rod_2'), None, "A fishing rod", "fishing rod"], 
    172: [image('string'), None, "A piece of string", "string"], 
    173: [image('stick'), None, "A stick", "the stick"], 
    174: [image('shears'), None, "A pair of shears", "the shears"], 
    175: [image('fish'), None, "A fish", "the fish"], 
    176: [image('key_2'), None, "A rusty key", "the key"], 
    177: [image('scout'), image('scout_shadow'), "Scout", "Scout"], 
    178: [image('scout_in_spaceship'), None, "Scout in his spaceship",
         "Scout's spaceship"], 
    179: [image('speech'), None, None], 
    180: [image('speech_cat1'), None, None], 
    181: [image('speech_cat2'), None, None], 
    182: [image('speech_fish'), None, None], 
    183: [image('speech_fish2'), None, None], 
    184: [image('speech_jailer'), None, None], 
    185: [image('speech_jailer2'), None, None], 
    186: [image('river_crop'), None, "The river bank"], 
    187: [image('tree_room2_2_crop'), None, "A tree"], 
    188: [image('tree_room6_2_crop'), None, "A tree"], 

    #earth
    189: [image('earth_grass'), None, None],
    190: [image('spaceship_earth'), image('spaceships_shadow'), "You and Scout's spaceship"],
    191: [image('scout'), image('scout_shadow'), "Scout", "Scout"],

    #extra
    192: [image('shelf_4'), image('shelf_4_shadow'), "A bookshelf"],
    193: [image('bed_4'), image('shelf_4_shadow'), "A bed"],
    194: [image('chair_7'), image('chair_7_shadow'), "Table and chairs"],
    195: [image('shelf_5'), image('shelf_4_shadow'), "A shelf with crafting materials"],
    196: [image('barrels'), image('barrels_shadow'), "Barrels"],
    197: [image('raccoon_tile'), None, ""],
    198: [image('speech_mountain'), None, None],
    199: [image('speech_help'), None, None],

    #general
    200: [image('speech'), None, None],
    201: [image('letter'), None, "A letter I wrote to myself",
         "letter to self"],
    202: [image('help'), None, None],
    203: [image('letter_1'), None, None],
    204: [image('wall_of_achievements'), None, None],
    205: [image('achievement_1'), None, None],
    206: [image('achievement_1_2'), None, None],
    207: [image('achievement_2'), None, None],
    208: [image('achievement_1_2_3'), None, None],
    209: [image('achievement_1_3'), None, None],
    210: [image('achievement_2_3'), None, None],
    211: [image('achievement_3'), None, None],

    #space images
    212: [image('space_1to2'), None, "Space"],
    213: [image('space_2to3'), None, "Space"],
    214: [image('space_3'), None, "Space"],

    #transparent images
    238: [image('transparent'), None, ""],
    
    239: [image('transparent'), None,"Not much to see here"],
    240: [image('transparent'), None, "The mountain"],
    241: [image('transparent'), None, "The sea"],
    242: [image('transparent'), None, "Not much to see here"],
    243: [image('transparent'), None, "A tree with blue leaves"],
    244: [image('transparent'), None, "A fence"],
    245: [image('transparent'), None, "An open door"],
    246: [image('transparent'), None, "A machine which is left running"],
    247: [image('transparent'), None, "A table full of books and \
research papers"],
    248: [image('transparent'), None, "Wall made of ice"],
    249: [image('transparent'), None, "A crowd of penguins"],
    250: [image('transparent'), None, "An open gate"],

    251: [image('transparent'), None, "The villagers' house"],
    252: [image('transparent'), None, "A locked fence"],
    253: [image('transparent'), None, "The river bank"],
    254: [image('transparent'), None, "A tree"]
    }

walls = [5, 80, 150]
items_player_may_carry = list(range(28, 51)) + list(range(121, 125)) + \
                         list(range(171, 179)) + [201]
items_player_may_stand_on = items_player_may_carry + \
                            [0, 2, 3, 57, 58, 136, 189, 197]

#SCENERY#

scenery = {
    #room number: [[object number, y position, x position]...]
    
    #planet 1
    1: [[9, 6, 5], [9, 6, 8], [9, 6, 11], [9, 6, 14], [9, 7, 2],
        [9, 7, 17], [9, 7, 19],[12, 5, 4], [12, 5, 16], [12, 6, 1],
        [12, 6, 18], [12, 8, 0], [12, 10, 0], [12, 12, 0], [12, 14, 0],
        [12, 15, 3], [12, 15, 6], [12, 15, 13], [12, 15, 16], [12, 15, 19],
        [14, 7, 6], [21, 8, 5], [243, 9, 0], [243, 11, 0],
        [243, 13, 0], [243, 15, 0]],
    2: [[5, 6, 11], [5, 11, 11], [5, 5, 20], [5, 6, 20], [5, 7, 20],
        [5, 8, 20], [5, 9, 20], [5, 10, 20], [5, 11, 20], [5, 5, 11],
        [5, 5, 12], [5, 5, 13], [5, 5, 14], [5, 5, 15], [5, 5, 16],
        [5, 5, 17], [5, 5, 18], [5, 5, 19], [5, 5, 20], [5, 12, 11],
        [5, 12, 12], [5, 12, 13], [5, 12, 14], [5, 12, 15], [5, 12, 16],
        [5, 12, 17], [5, 12, 18], [5, 12, 19], [5, 12, 20], [6, 10, 11],
        [8, 2, 22], [8, 3, 22], [8, 4, 22], [8, 5, 22], [8, 6, 22],
        [8, 7, 22], [8, 8, 22], [8, 9, 22], [8, 10, 22], [8, 11, 22],
        [8, 12, 22], [8, 13, 22], [8, 14, 22], [9, 6, 0], [9, 10, 0],
        [8, 2, 3], [8, 3, 3], [8, 4, 3], [8, 5, 3], [8, 11, 3],
        [8, 12, 3], [8, 13, 3], [8, 14, 3], [10, 1, 3], [10, 15, 3],
        [19, 6, 9], [22, 4, 6], [200, 15, 0], [53, 15, 2],
        [192, 6, 13], [193, 9, 18], [194, 6, 16], [197, 6, 12], [197, 7, 12],
        [197, 7, 13], [197, 7, 14], [197, 7, 15], [197, 6, 15], [197, 6, 19],
        [197, 7, 16], [197, 7, 17], [197, 7, 18], [197, 7, 19], [197, 8, 12],
        [197, 8, 17], [197, 8, 18], [197, 8, 19], [197, 9, 12], [197, 9, 17], 
        [197, 10, 12], [197, 10, 13], [197, 10, 14], [197, 10, 15], [197, 10, 16], 
        [197, 10, 17], [197, 10, 18], [197, 10, 19], [197, 11, 12], [197, 11, 13], 
        [197, 11, 14], [197, 11, 15], [197, 11, 16], [197, 11, 17], [197, 11, 18], 
        [197, 11, 19], [197, 9, 13], [197, 9, 14], [197, 9, 15], [197, 9, 16],
        [197, 8, 13], [197, 8, 14], [197, 8, 15], [197, 8, 16]],
    3: [[15, 7, 0], [15, 7, 5], [15, 7, 9], [15, 11, 0], [15, 15, 0],
        [18, 15, 16], [241, 0, 16], [241, 1, 16], [241, 2, 16], [241, 3, 16],
        [241, 4, 16], [241, 5, 16], [241, 6, 16], [241, 7, 16], [241, 8, 16],
        [241, 9, 16], [241, 10, 16], [241, 11, 16], [241, 12, 16], [241, 13, 16],
        [241, 14, 16], [242, 8, 0], [242, 9, 0], [242, 10, 0], [242, 12, 0],
        [242, 13, 0], [242, 14, 0], [242, 16, 0]],
    5: [[12, 3, 0], [12, 5, 0], [12, 7, 0], [12, 9, 0], [12, 11, 0],
        [12, 13, 0], [12, 3, 19], [12, 5, 19], [12, 7, 19], [13, 15, 0],
        [243, 6, 3],[243, 8, 3], [243, 10, 3], [243, 12, 3], [243, 14, 3],
        [243, 1, 19], [243, 2, 19], [243, 4, 19], [243, 6, 19], [243, 0, 3],
        [243, 1, 3], [243, 2, 3], [243, 4, 3], [243, 0, 19], [16, 8, 20]],
    6: [[4, 15, 13], [3, 15, 16], [12, 15, 0], [12, 15, 3], [12, 15, 6], 
        [12, 4, 0], [12, 4, 3], [12, 4, 6], [12, 4, 9], [12, 4, 12],
        [12, 4, 15], [12, 4, 18], [242, 4, 22]],
    7: [[10, 15, 0], [18, 15, 16], [24, 5, 3], [241, 0, 16],
        [241, 1, 16], [241, 2, 16], [241, 3, 16], [241, 4, 16],
        [241, 5, 16], [241, 6, 16], [241, 7, 16], [241, 8, 16],
        [241, 9, 16], [241, 10, 16], [241, 11, 16], [241, 12, 16],
        [241, 13, 16], [241, 14, 16], [239, 3, 3], [239, 3, 4],
        [239, 3, 5], [239, 3, 6], [239, 4, 3], [239, 4, 4], [239, 4, 5],
        [239, 4, 6]],
    9: [[12, 4, 7], [12, 4, 10], [12, 4, 13], [12, 4, 16], [12, 5, 19],
        [12, 15, 7], [12, 15, 10], [12, 15, 13], [12, 15, 16], [12, 14, 19],
        [17, 15, 0], [240, 5, 6], [240, 6, 6], [240, 7, 6], [240, 8, 6],
        [240, 9, 6], [240, 10, 6], [240, 12, 6], [240, 13, 6], [240, 14, 6]],
    10: [[5, 7, 13], [5, 11, 13], [5, 12, 13], [5, 7, 21], [5, 8, 21],
         [5, 9, 21], [5, 10, 21], [5, 11, 21], [5, 12, 21], [5, 12, 14],
         [5, 12, 15], [5, 12, 16], [5, 12, 17], [5, 12, 18], [5, 12, 19],
         [5, 12, 20], [6, 10, 13], [7, 6, 13], [13, 15, 0], [12, 4, 0],
         [12, 4, 3], [12, 4, 6], [12, 4, 13], [12, 4, 16], [12, 4, 19],
         [20, 8, 19], [23, 8, 17], [243, 5, 13], [242, 13, 13],
         [242, 14, 13], [243, 3, 9], [243, 2, 9], [243, 1, 9], [243, 3, 13],
         [243, 2, 13], [243, 1, 13], [195, 7, 14], [196, 7, 19]],

    #planet 2
    13: [[80, 4, 0], [80, 5, 0], [80, 6, 0], [80, 7, 0], [80, 8, 0],
         [80, 9, 0], [80, 10, 0], [80, 11, 0], [80, 12, 0], [80, 13, 0],
         [80, 14, 0], [80, 4, 22], [80, 5, 22], [80, 11, 22], [80, 12, 22],
         [80, 13, 22], [80, 14, 22], [80, 15, 0], [80, 15, 1], [80, 15, 2],
         [80, 15, 3], [80, 15, 4], [80, 15, 5], [80, 15, 6], [80, 15, 7],
         [80, 15, 8], [80, 15, 9], [80, 15, 10], [80, 15, 11], [80, 15, 12],
         [80, 15, 13], [80, 15, 14], [80, 15, 15], [80, 15, 16], [80, 15, 17],
         [80, 15, 18], [80, 15, 19], [80, 15, 20], [80, 15, 21], [80, 15, 22],
         [81, 3, 0], [105, 11, 2], [104, 5, 19], [98, 5, 1], [99, 5, 7],
         [98, 5, 13], [100, 8, 10], [102, 8, 11], [101, 8, 15], [100, 11, 10],
         [103, 11, 11], [101, 11, 15]],
    14: [[59, 10, 8], [59, 11, 8], [59, 12, 8], [59, 13, 8], [59, 14, 8],
         [59, 15, 8], [59, 10, 14], [59, 11, 14], [59, 12, 14], [59, 13, 14],
         [59, 14, 14], [59, 15, 14], [60, 3, 0], [61, 9, 0], [61, 9, 14],
         [62, 15, 0], [63, 15, 15], [70, 2, 0]],
    15: [[80, 4, 22], [80, 5, 22], [80, 6, 22], [80, 7, 22], [80, 8, 22],
         [80, 9, 22], [80, 10, 22], [80, 11, 22], [80, 12, 22], [80, 13, 22],
         [80, 14, 22], [80, 4, 0], [80, 5, 0], [80, 6, 0], [80, 12, 0],
         [80, 13, 0], [80, 14, 0], [80, 15, 0], [80, 15, 1], [80, 15, 2],
         [80, 15, 3], [80, 15, 4], [80, 15, 5], [80, 15, 6], [80, 15, 7],
         [80, 15, 8], [80, 15, 9], [80, 15, 10], [80, 15, 11], [80, 15, 12],
         [80, 15, 13], [80, 15, 14], [80, 15, 15], [80, 15, 16], [80, 15, 17],
         [80, 15, 18], [80, 15, 19], [80, 15, 20], [80, 15, 21], [80, 15, 22],
         [81, 3, 0], [107, 11, 16],[116, 6, 15], [115, 6, 16], [114, 5, 1],
         [96, 4, 9]],
    16: [[80, 4, 0], [80, 5, 0], [80, 6, 0], [80, 7, 0], [80, 8, 0],
         [80, 9, 0], [80, 10, 0], [80, 11, 0], [80, 12, 0], [80, 13, 0],
         [80, 14, 0], [80, 4, 22], [80, 5, 22], [80, 6, 22], [80, 7, 22],
         [80, 8, 22], [80, 9, 22], [80, 10, 22], [80, 11, 22],
         [80, 12, 22], [80, 13, 22], [80, 14, 22], [80, 15, 0], [80, 15, 1],
         [80, 15, 2], [80, 15, 3], [80, 15, 4], [80, 15, 5], [80, 15, 6],
         [80, 15, 7], [80, 15, 8], [80, 15, 14], [80, 15, 15], [80, 15, 16],
         [80, 15, 17], [80, 15, 18], [80, 15, 19], [80, 15, 20], [80, 15, 21],
         [80, 15, 22], [81, 3, 0], [91, 15, 9], [92, 15, 13], [117, 13, 2] ,
         [93, 8, 15], [97, 3, 4], [246, 4, 15], [246, 5, 15], [246, 6, 15],
         [246, 7, 15], [247, 6, 2], [247, 6, 3], [247, 6, 4], [247, 7, 2],
         [247, 7, 3], [247, 7, 4], [247, 8, 2], [247, 8, 3], [247, 8, 4],
         [247, 9, 2], [247, 9, 3], [247, 9, 4], [247, 10, 2], [247, 10, 3],
         [247, 10, 4], [247, 11, 2], [247, 11, 3], [247, 11, 4], [247, 12, 2],
         [247, 12, 3], [247, 12, 4], [119, 13, 5]],
    17: [[80, 4, 0], [80, 5, 0], [80, 6, 0], [80, 7, 0], [80, 8, 0],
         [80, 9, 0], [80, 10, 0], [80, 11, 0], [80, 12, 0], [80, 13, 0],
         [80, 14, 0], [80, 15, 0], [80, 15, 1], [80, 15, 2], [80, 15, 3],
         [80, 15, 4], [80, 15, 5], [80, 15, 6], [80, 15, 7], [80, 15, 8],
         [80, 15, 9], [80, 15, 13], [80, 15, 14], [80, 15, 15], [80, 15, 16],
         [80, 15, 17], [80, 15, 18], [80, 15, 19], [80, 15, 20], [80, 15, 21],
         [80, 15, 22], [248, 14, 9], [248, 13, 9], [248, 14, 13], [248, 13, 13], 
         [81, 3, 0], [80, 4, 22], [80, 5, 22], [80, 11, 22], [80, 12, 22],
         [80, 13, 22], [80, 14, 22], [73, 6, 3], [74, 6, 5], [75, 6, 7],
         [76, 7, 11], [78, 12, 1], [79, 12, 13], [82, 6, 2], [248, 10, 1],
         [248, 10, 2], [248, 10, 3], [248, 10, 4], [248, 10, 5],
         [248, 10, 6], [248, 10, 7], [248, 10, 8], [248, 10, 9],
         [248, 11, 9], [248, 12, 9], [248, 13, 9], [248, 11, 13],
         [248, 10, 13], [248, 10, 14], [248, 10, 15], [248, 10, 16],
         [248, 10, 17], [248, 10, 18], [248, 10, 19], [248, 10, 20],
         [243, 5, 2], [243, 4, 2], [243, 5, 8], [243, 4, 8]],
    18: [[59, 1, 8], [59, 2, 8], [59, 3, 8], [59, 4, 8], [59, 1, 14],
         [59, 2, 14], [59, 3, 14], [59, 4, 14], [59, 12, 8], [59, 13, 8],
         [59, 14, 8], [59, 15, 8], [59, 12, 14], [59, 13, 14], [59, 14, 14],
         [59, 15, 14], [61, 5, 0], [61, 11, 0], [61, 5, 14], [61, 11, 14],
         [64, 4, 0], [65, 4, 15], [66, 15, 0], [67, 15, 15]],
    19: [[80, 4, 22], [80, 5, 22], [80, 6, 22], [80, 7, 22], [80, 8, 22],
         [80, 9, 22], [80, 10, 22], [80, 11, 22], [80, 12, 22], [80, 13, 22],
         [80, 14, 22], [80, 15, 0], [80, 15, 1], [80, 15, 2], [80, 15, 3],
         [80, 15, 4], [80, 15, 5], [80, 15, 6], [80, 15, 7], [80, 15, 8],
         [80, 15, 9], [80, 15, 10], [80, 15, 11], [80, 15, 12], [80, 15, 13],
         [80, 15, 14], [80, 15, 15], [80, 15, 16], [80, 15, 17], [80, 15, 18],
         [80, 15, 19], [80, 15, 20], [80, 15, 21], [80, 15, 22], [80, 4, 0],
         [80, 5, 0], [80, 6, 0], [80, 12, 0], [80, 13, 0], [80, 14, 0],
         [81, 3, 0], [113, 6, 1], [113, 6, 14], [112, 5, 9], [112, 5, 13],
         [83, 5, 10], [108, 6, 11], [109, 11, 3], [110, 11, 7], [111, 11, 4],
         [106, 11, 17], [119, 13, 15]],
    20: [[80, 4, 0], [80, 5, 0], [80, 6, 0], [80, 7, 0], [80, 8, 0],
         [80, 9, 0], [80, 10, 0], [80, 11, 0], [80, 12, 0], [80, 13, 0],
         [80, 14, 0], [80, 4, 22], [80, 5, 22], [80, 6, 22], [80, 7, 22],
         [80, 8, 22], [80, 9, 22], [80, 10, 22], [80, 11, 22],
         [80, 12, 22], [80, 13, 22], [80, 14, 22], [80, 15, 0],
         [80, 15, 1], [80, 15, 2], [80, 15, 3], [80, 15, 4], [80, 15, 5],
         [80, 15, 6], [80, 15, 7], [80, 15, 8], [80, 15, 14],
         [80, 15, 15], [80, 15, 16], [80, 15, 17], [80, 15, 18],
         [80, 15, 19], [80, 15, 20], [80, 15, 21], [80, 15, 22],
         [88, 3, 0], [88, 3, 14], [89, 4, 2], [89, 4, 4], [89, 4, 6],
         [89, 4, 15], [89, 4, 17], [89, 4, 19], [90, 3, 9], [117, 13, 2],
         [118, 13, 18], [247, 6, 2], [247, 6, 3], [247, 6, 4], [247, 7, 2],
         [247, 7, 3], [247, 7, 4], [247, 8, 2], [247, 8, 3], [247, 8, 4],
         [247, 9, 2], [247, 9, 3], [247, 9, 4], [247, 10, 2], [247, 10, 3],
         [247, 10, 4], [247, 11, 2], [247, 11, 3], [247, 11, 4],
         [247, 12, 2], [247, 12, 3], [247, 12, 4], [247, 6, 18],
         [247, 6, 19], [247, 6, 20], [247, 7, 18], [247, 7, 19],
         [247, 7, 20], [247, 8, 18], [247, 8, 19], [247, 8, 20],
         [247, 9, 18], [247, 9, 19], [247, 9, 20], [247, 10, 18],
         [247, 10, 19], [247, 10, 20], [247, 11, 18], [247, 11, 19],
         [247, 11, 20], [247, 12, 18], [247, 12, 19], [247, 12, 20], [119, 13, 5]],
    21: [[77, 10, 5], [94, 5, 0], [95, 5, 14], [59, 6, 0], [59, 7, 0],
         [59, 8, 0], [59, 9, 0], [59, 10, 0], [59, 11, 0], [59, 12, 0], 
         [59, 13, 0], [59, 14, 0], [60, 15, 0], [59, 6, 22], [59, 7, 22], 
         [59, 8, 22], [59, 9, 22], [59, 10, 22], [59, 11, 22], [59, 12, 22],
         [59, 13, 22], [59, 14, 22], [200, 15, 0], [126, 15, 2], [244, 1, 8],
         [244, 2, 8], [244, 3, 8], [244, 1, 14], [244, 2, 14], [244, 3, 14],
         [244, 0, 8]],
    22: [[59, 1, 8], [59, 2, 8], [59, 3, 8], [59, 4, 8], [59, 5, 8],
         [59, 6, 8], [59, 7, 8], [59, 8, 8], [59, 9, 8], [59, 10, 8],
         [59, 11, 8], [59, 12, 8], [59, 1, 14], [59, 2, 14], [59, 3, 14],
         [59, 4, 14], [59, 5, 14], [59, 6, 14], [60, 13, 0],
         [61, 7, 14], [68, 6, 15], [69, 15, 0]],
    23: [[60, 7, 0], [60, 13, 0], [71, 15, 0], [72, 6, 0]],
    24: [[59, 8, 22], [59, 9, 22], [59, 10, 22], [59, 11, 22], [59, 12, 22],
         [60, 13, 0], [71, 15, 0], [84, 7, 0], [246, 1, 9], [246, 2, 9],
         [246, 3, 9], [246, 4, 9], [246, 5, 9], [246, 6, 0], [246, 1, 13],
         [246, 2, 13], [246, 3, 13], [246, 4, 13], [246, 5, 13]],

    #planet 3
    25: [[145, 6, 9], [146, 15, 0], [147, 3, 8], [253, 4, 7], [253, 5, 7],
         [253, 6, 7], [253, 7, 7], [253, 8, 7], [253, 9, 7], [253, 10, 7], 
         [253, 11, 7], [253, 12, 7], [253, 13, 7], [253, 14, 7],  [158, 15, 14]],
    26: [[150, 3, 13], [150, 4, 13], [150, 5, 13], [150, 6, 13], [150, 7, 13],
         [150, 8, 13], [150, 9, 13], [150, 10, 13], [150, 10, 14], [150, 10, 15],
         [150, 10, 18], [150, 10, 19], [150, 10, 20], [150, 10, 21],
         [150, 10, 22], [151, 3, 14], [153, 3, 0], [154, 15, 0], [152, 10, 16],
         [143, 11, 15], [144, 11, 18], [254, 11, 21], [254, 12, 21],
         [254, 13, 21], [254, 14, 21]],
    27: [[155, 15, 0], [155, 15, 1], [155, 15, 2], [155, 15, 3], [155, 15, 4], 
         [155, 15, 5], [155, 15, 6], [155, 15, 7], [155, 15, 8], [155, 15, 9],
         [155, 15, 13], [155, 15, 14], [155, 15, 15], [155, 15, 16], [155, 15, 17],
         [155, 15, 18], [155, 15, 19], [155, 15, 20], [155, 15, 21], [155, 15, 22],
         [155, 14, 0], [155, 14, 2], [155, 14, 9], [155, 14, 17], [155, 14, 22],
         [155, 13, 0], [155, 13, 2], [155, 13, 3], [155, 13, 4], [155, 13, 5],
         [155, 13, 6], [155, 13, 7], [155, 13, 9], [155, 13, 14], [155, 13, 15],
         [155, 13, 17], [155, 13, 19], [155, 13, 20], [155, 13, 22], [155, 12, 0], 
         [155, 12, 7], [155, 12, 9], [155, 12, 10], [155, 12, 11], [155, 12, 12], 
         [155, 12, 15], [155, 12, 17], [155, 12, 20], [155, 12, 22], [155, 11, 0], 
         [155, 11, 7], [155, 11, 12], [155, 11, 13], [155, 11, 15], [155, 11, 17], 
         [155, 11, 18], [155, 11, 20], [155, 11, 22], [155, 10, 0], [155, 10, 1], 
         [155, 10, 3], [155, 10, 4], [155, 10, 5], [155, 10, 6], [155, 10, 7], 
         [155, 10, 10], [155, 10, 11], [155, 10, 12], [155, 10, 15], [155, 10, 20], 
         [155, 10, 22], [155, 9, 3], [155, 9, 10], [155, 9, 14], [155, 9, 15], 
         [155, 9, 17], [155, 9, 18], [155, 9, 19], [155, 9, 20], [155, 9, 22], 
         [155, 8, 3], [155, 8, 5], [155, 8, 6], [155, 8, 7], [155, 8, 8], 
         [155, 8, 9], [155, 8, 10], [155, 8, 12], [155, 8, 13], [155, 8, 14], 
         [155, 8, 17], [155, 8, 22], [155, 7, 3], [155, 7, 20], [155, 7, 21], 
         [155, 7, 22], [155, 6, 3], [155, 6, 4], [155, 6, 5], [155, 6, 6], 
         [155, 6, 7], [155, 6, 8], [155, 6, 10], [155, 6, 11], [155, 6, 12], 
         [155, 6, 13], [155, 6, 14], [155, 6, 15], [155, 6, 16], [155, 6, 17], 
         [155, 6, 20], [155, 6, 22],  [155, 5, 0],  [155, 5, 1], [155, 5, 3], 
         [155, 5, 11], [155, 5, 20], [155, 5, 22], [155, 4, 0], [155, 4, 3], 
         [155, 4, 4], [155, 4, 5], [155, 4, 6], [155, 4, 7], [155, 4, 8], 
         [155, 4, 9], [155, 4, 10], [155, 4, 11], [155, 4, 12], [155, 4, 14], 
         [155, 4, 16], [155, 4, 17], [155, 4, 19], [155, 4, 20], [155, 4, 22],
         [155, 3, 0], [155, 3, 14], [155, 3, 22], [155, 2, 0], [155, 2, 1],
         [155, 2, 2], [155, 2, 3], [155, 2, 4], [155, 2, 5], [155, 2, 6],
         [155, 2, 7], [155, 2, 8], [155, 2, 9], [155, 2, 10], [155, 2, 11], 
         [155, 2, 12], [155, 2, 13], [155, 2, 14], [155, 2, 15], [155, 2, 16], 
         [155, 2, 17], [155, 2, 18], [155, 2, 19],  [155, 2, 20], [155, 2, 21],
         [155, 2, 22], [166, 9, 0], [252, 6, 0], [252, 7, 0], [252, 8, 0]],
    29: [[146, 15, 0], [148, 15, 8], [163, 5, 14], [254, 1, 14], [254, 2, 14],
         [254, 3, 14], [254, 4, 14], [253, 1, 7], [253, 2, 7],
         [253, 3, 7], [253, 4, 7], [253, 5, 7], [253, 6, 7], [253, 7, 7],
         [253, 8, 7], [253, 9, 7], [253, 10, 7], [253, 11, 7], [253, 12, 7],
         [253, 13, 7], [253, 14, 7]],
    30: [[137, 5, 0], [156, 15, 0]],
    31: [[157, 15, 0], [158, 15, 14], [159, 5, 0], [160, 5, 14], [161, 5, 9],
         [139, 6, 22], [139, 7, 22], [139, 8, 22], [139, 9, 22], [139, 10, 22],
         [139, 11, 22], [139, 12, 22], [139, 13, 22], [139, 14, 22]],
    33: [[137, 5, 0], [140, 15, 0], [141, 10, 6],
         [139, 6, 0], [139, 7, 0], [139, 8, 0], [139, 9, 0], [139, 10, 0],
         [139, 11, 0], [139, 12, 0], [139, 13, 0], [139, 14, 0]],
    34: [[138, 5, 0], [140, 15, 0], [142, 10, 10]],
    35: [[164, 5, 0], [165, 5, 14], [140, 15, 0], [139, 6, 22], [139, 7, 22],
         [139, 8, 22], [139, 9, 22], [139, 10, 22], [139, 11, 22], [139, 12, 22],
         [139, 13, 22], [139, 14, 22], [167, 12, 17], [168, 11, 15],
         [251, 6, 15], [251, 7, 15], [252, 8, 15], [252, 9, 15], [252, 10, 15],
         [254, 0, 8], [254, 1, 8], [254, 2, 8], [254, 3, 8], [254, 4, 8],
         [254, 0, 14], [254, 1, 14], [254, 2, 14], [254, 3, 14], [254, 4, 14]],

    #earth
    36: [[190, 9, 9], [191, 10, 10], [238, 10, 8], [238, 11, 9]]
    }

#PROPS#

props = {
    #object number: [room, y, x]

    #planet1
    27: [9, 11, 6], # Iron ore rock
    28: [2, 4, 6], # Charcoal
    29: [2, 4, 5], # Stick
    30: [2, 3, 5], # Stick
    31: [0, 0, 0], # Iron ore
    32: [5, 10, 4], # Large stone for axe
    33: [10, 11, 2], # Long stone for pickaxe
    34: [0, 0, 0], # Pickaxe
    35: [0, 0, 0], # Axe
    36: [3, 10, 8], # Seashell
    37: [3, 8, 9], # Unsealed oxygen tank
    38: [0, 0, 0], # Oxygen tank
    39: [10, 7, 16], # Sulfur
    40: [0, 0, 0], # Gunpowder
    41: [5, 8, 20], # Sticky goo under sticky plant
    43: [7, 5, 3], # Manual under broken spaceship
    44: [0, 0, 0], # Log
    45: [0, 0, 0], # Plank
    46: [7, 14, 14], # Navigation system missing a piece of magnet
    47: [0, 0, 0], # Navigation system
    48: [0, 0, 0], # Sulfur + Seashell mixture
    49: [0, 0, 0], # Sulfur + Charcoal mixture
    50: [0, 0, 0], # Charcoal + Seashell mixture

    #planet 2
    121: [20, 5, 2], # Access card
    122: [19, 5, 13], # Key
    123: [15, 5, 1], # Shovel
    124: [13, 5, 7], # Fuel tank

    #planet 3
    171: [0, 0, 0], # Fishing rod
    172: [25, 6, 8], # String
    173: [30, 14, 5], # Stick
    174: [0, 0, 0], # Shears
    175: [0, 0, 0], # Fish
    176: [27, 9, 4], # Key
    177: [26, 6, 17], # Scout
    178: [0, 0, 0], # Scout and his spaceship
    
    201: [0, 0, 0], # Letter to self
    }

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
    [50, 39, 40], # Mixture 3 + Sulfur = Gunpowder
    [172, 173, 171] # Planet 3 Fishing rod
    ]

#GAME PROGRESS#
new_game = True

if os.path.exists('save\\new_game.dat'):
    new_game = pickle.load(open(path + "new_game.dat", "rb"))

if new_game:
    current_room = 2
    player_y, player_x = 8, 9 # Start at 8,9
    player_direction = "up"
    achievement = 204
    speech_text = 53
    in_my_pockets = [201, 38, 40, 45, 47]
    game_progress = [True, True, False, False, False, False, False,
                     False, False, False, False, False, False, False]
    planet1_progress = [False, False, False, False,
                        False, False, False, False, False]
    planet2_progress = [False, False, False, True, False]
    planet3_progress = [False, False, True, False, False, False, False,
                        False]
    
else:  
    current_room = pickle.load(open(path + "current_room.dat", "rb"))
    player_y = pickle.load(open(path + "player_y.dat", "rb"))
    player_x = pickle.load(open(path + "player_x.dat", "rb"))
    player_direction = pickle.load(open(path + "player_direction.dat", "rb"))
    achievement = pickle.load(open(path + "achievement.dat", "rb"))
    speech_text = pickle.load(open(path + "speech_text.dat", "rb"))
    in_my_pockets = pickle.load(open(path + "in_my_pockets.dat", "rb"))
    game_progress = pickle.load(open(path + "game_progress.dat", "rb"))
    planet1_progress = pickle.load(open(path + "planet1_progress.dat", "rb"))
    planet2_progress = pickle.load(open(path + "planet2_progress.dat", "rb"))
    planet3_progress = pickle.load(open(path + "planet3_progress.dat", "rb"))
    props = pickle.load(open(path + "props.dat", "rb"))
    scenery = pickle.load(open(path + "scenery.dat", "rb"))

player_frame = 0
player_offset_x, player_offset_y = 0, 0
player_image = PLAYER[player_direction][player_frame]

#USE OBJECTS#

def use_object():
    global room_map, item_carrying, selected_item, in_my_pockets
    global speech_text, game_progress
    global planet1_progress, planet2_progress, planet3_progress

    use_message = "You fiddle with it but nothing happens."
    standard_responses = {
        28: "Hot!",
        43: "You read the manual.",
        201: "You read the letter you wrote to yourself."
        }

    item_player_is_on = get_item_under_player()
    for this_item in [item_player_is_on, item_carrying]:
        if this_item in standard_responses:
            use_message = standard_responses[this_item]

    if game_progress[0] == True:
        use_message = "Please press Enter to continue."

    #planet 1
    if item_carrying == 34 and item_player_is_on == 27: # use pickaxe
        use_message = "You found a piece of iron ore!"
        add_object(31)
        sound('combine')
        props[item_player_is_on][0] = 0
        scenery[current_room].append([240, 11, 6])

    elif item_carrying == 35 and item_player_is_on in [12, 13, 14, 243]: # use axe
        if item_player_is_on in [12, 13, 243]:
            use_message = "You chopped off a piece of log"
            add_object(44)
            sound('combine')
        elif item_player_is_on == 14:
            use_message = "You chopped off a piece of plank"
            add_object(45)
            sound('combine')
            scenery[current_room].remove([14, 7, 6])
            scenery[current_room].append([26, 7, 6])
            game_progress[5] = True

    elif item_carrying == 44 and item_player_is_on == 23: # use crafting table
        use_message = "You crafted planks from the log"
        add_object(45)
        remove_object(44)
        sound('combine')

    elif item_player_is_on in [24, 242] and item_carrying in [38, 40, 45, 47]: # broken spaceship
        if item_carrying == 45: # fix plank
            use_message = "You fix the plank to the spaceship"
            planet1_progress[0] = True
            remove_object(45)
        elif item_carrying == 47: # fix navigation system
            use_message = "You fix the navigation system to the spaceship"
            planet1_progress[1] = True
            remove_object(47)
        elif item_carrying == 40: # add gunpowder
            use_message = "You add gunpowder into the rocket booster"
            planet1_progress[2] = True
            remove_object(40)
        elif item_carrying == 38: # fix oxygen tank
            use_message = "You fix the oxygen tank to the spaceship"
            planet1_progress[3] = True
            remove_object(38)
        if planet1_progress[0] and planet1_progress[1] and \
           planet1_progress[2] and planet1_progress[3]:
            scenery[current_room].remove([24, 5, 3])
            scenery[current_room].append([25, 5, 3])
            game_progress[6] = True
            if game_progress[5]:
                use_message = "You've fixed the spaceship and you can \
leave! The raccoons"
                show_text("seem upset about the treehouse and did not \
give you a souvenir.", 1)
            else:
                use_message = "You've fixed the spaceship and you can \
leave the planet!"
                show_text("The raccoons gave you a souvenir! Press [A] \
to view it.", 1)

        sound('combine')

    elif item_player_is_on == 25: # Fixed spaceship
        use_message = "You're travelling through space!"
        show_text("", 1)
        planet_1_to_2()

    elif item_player_is_on == 43 or item_carrying == 43: #read manual
        if not game_progress[0]:
            scenery[current_room].append([51, 15, 0])
            planet1_progress[5] = True
            game_progress[0] = True

    #planet 2
    elif item_player_is_on == 90 and item_carrying == 121:
        use_message = "You used the access card to unlock the door!"
        scenery[current_room].remove([90, 3, 9])
        scenery[current_room].append([91, 3, 9])
        scenery[current_room].append([92, 3, 13])
        scenery[current_room].append([245, 1, 9])
        scenery[current_room].append([245, 2, 9])
        scenery[current_room].append([245, 1, 13])
        scenery[current_room].append([245, 2, 13])
        sound('combine')
        planet2_progress[2] = True

    elif item_player_is_on == 87 and item_carrying == 122:
        use_message = "You used the key to unlock the gate!"
        scenery[current_room].remove([87, 6, 0])
        scenery[current_room].append([85, 6, 0])
        scenery[current_room].append([86, 6, 13])
        sound('combine')

    elif item_player_is_on == 84 and item_carrying == 123:
        use_message = "You shovel the snow away to reveal a hidden gate"
        scenery[current_room].remove([84, 7, 0])
        scenery[current_room].append([59, 7, 9])
        scenery[current_room].append([59, 7, 13])
        scenery[current_room].append([61, 7, 0])
        scenery[current_room].append([61, 7, 14])
        scenery[current_room].append([87, 6, 0])
        sound('combine')

    elif item_player_is_on == 77 and item_carrying == 124:
        use_message = "You add fuel to your spaceship"
        scenery[current_room].remove([77, 10, 5])
        scenery[current_room].append([120, 10, 5])
        remove_object(124)
        game_progress[8] = True
        sound('combine')

    elif item_player_is_on == 120: # Fixed spaceship
        use_message = "You're travelling through space!"
        show_text("", 1)
        planet_2_to_3()

    #planet 3
    elif item_player_is_on == 161 and item_carrying == 174:
        scenery[current_room].remove([159, 5, 0])
        scenery[current_room].remove([160, 5, 14])
        scenery[current_room].remove([161, 5, 9])
        scenery[current_room].append([162, 5, 0])
        scenery[current_room].append([163, 5, 14])
        use_message = "You cut away the twines to reveal a hidden path"
        sound('combine')

    elif item_player_is_on == 253 and item_carrying == 171:
        if planet3_progress[6]:
            use_message = "You can't fish right now!" 
            return
        else:
            planet3_progress[7] = True
            number = random.choice(range(1, 10))
            limit = random.choice(range(4, 7))
            count = 0
            if number == 1 or count > limit:
                use_message = "You caught a fish!"
                add_object(175)
                sound('combine')
            else:
                use_message = "No fishes took the bait."
                count += 1

    elif item_player_is_on == 252 or item_player_is_on == 166:
        if item_carrying == 176:
            scenery[current_room].remove([166, 9, 0])
            scenery[current_room].remove([252, 6, 0])
            scenery[current_room].remove([252, 7, 0])
            scenery[current_room].remove([252, 8, 0])
            scenery[current_room].append([170, 6, 0])
            use_message = "You unlocked the fence!"
            sound('combine')

    elif item_player_is_on == 145 and item_carrying == 175: # river cat
        use_message = "You gave a fish to the cat."
        remove_object(175)
        planet3_progress[0] = True

    elif item_player_is_on in [143, 144] and item_carrying == 175: # jailer cat
        use_message = "You gave a fish to the jailer cats."
        remove_object(175)
        planet3_progress[1] = True

    elif item_player_is_on == 167 and item_carrying == 175: # unfriendly cat
        if planet3_progress[2]:
            planet3_progress[2] = False
            planet3_progress[3] = True
        elif planet3_progress[3]:
            planet3_progress[3] = False
            planet3_progress[4] = True
        use_message = "You gave a fish to the cats."
        show_text("", 1)
        remove_object(175)

    elif item_player_is_on == 142 and planet3_progress[6]:
        use_message = "You placed Scout in his spaceship"
        scenery[current_room].remove([142, 10, 10])
        remove_object(177)
        add_object(178)
        planet3_progress[6] = False
        sound('combine')

    elif item_player_is_on == 141 and item_carrying == 178:
        use_message = "You attached Scout's spaceship to your own"
        scenery[current_room].remove([141, 10, 6])
        scenery[current_room].append([169, 10, 6])     
        remove_object(178)
        sound('combine')

    elif item_player_is_on == 169: # Fixed spaceship
        use_message = "You're travelling back to Earth!"
        show_text("", 1)
        game_progress[9] = True
        planet_3_to_earth()

    elif item_player_is_on == 201 or item_carrying == 201:
        if not game_progress[0]:
            scenery[current_room].append([203, 15, 0])
            game_progress[2] = True
            game_progress[0] = True
            
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

def get_floor_type():
    if current_room in [1, 2, 5, 6, 9, 10]:
        return 0 # Grass
    elif current_room in [3, 7]:
        return 2 # Sand
    elif current_room in [13, 15, 16, 17, 19, 20]:
        return 58 # Concrete
    elif current_room in [14, 18, 21, 22, 23, 24]:
        return 57 # Ice path
    elif current_room in [25, 26, 27, 29, 30, 31, 33, 34, 35]:
        return 136 # Yellow floor tile
    elif current_room == 36:
        return 189 # Earth grass

def can_drop(old_y, old_x):
    if item_carrying == 177:
        return False
    elif room_map[old_y][old_x] in [0, 1, 2, 57, 58, 136]:
        if current_room == 6 and old_x > 17:
            return False
        else:
            return True
    else:
        return False

def speak():
    global speech_text, game_progress
    global planet1_progress, planet2_progress, planet3_progress
    
    item_player_is_on = get_item_under_player()

    #planet 1
    if item_player_is_on in [19, 20, 21]: # dialogue with raccoons
        if not game_progress[0]:
            if item_player_is_on == 19: # raccoon 1
                speech_text = 53
                planet1_progress[8] = True
            elif item_player_is_on == 20: # raccoon 2
                speech_text = 56
                planet1_progress[7] = True
            elif item_player_is_on == 21: # baby raccoon
                speech_text = 54
                planet1_progress[4] = True
            scenery[current_room].append([200, 15, 0]) # speech bubble
            scenery[current_room].append([speech_text, 15, 2])
            game_progress[1] = True
            game_progress[0] = True

    #planet 2
    if item_player_is_on in [73, 74, 75]: # dialogue with penguins
        if not game_progress[1] and not planet2_progress[2]:
            if item_player_is_on == 73:  # fisherman
                speech_text = 132
            elif item_player_is_on == 74: # scientist
                speech_text = 133
            elif item_player_is_on == 75: # student
                speech_text = 134
            scenery[current_room].append([200, 15, 0]) # speech bubble
            scenery[current_room].append([speech_text, 15, 2])
            game_progress[1] = True
            game_progress[0] = True

    if item_player_is_on == 76: # dialogue with mayor
        if not game_progress[1]:
            if not planet2_progress[2]:
                speech_text = 127
                planet2_progress[0] = True
                scenery[current_room].append([200, 15, 0]) # speech bubble
                scenery[current_room].append([speech_text, 15, 2])
                game_progress[1] = True
                game_progress[0] = True
            else:
                if planet2_progress[3]:
                    scenery[current_room].append([125, 15, 0])
                    game_progress[0] = True
                    planet2_progress[4] = True
                else:
                    show_text("You have used up your only chance to \
identify the culprit", 0)

    # planet 3
    if item_player_is_on == 167: # unfriendly cats
        if not game_progress[0] and not planet3_progress[5]:
            if planet3_progress[2]:
                show_text("The cats stare at you but don't say anything.", 1)
                return
            elif planet3_progress[3]:
                speech_text = 182
            elif planet3_progress[4]:
                speech_text = 183
                add_object(174)
                sound('combine')
                planet3_progress[5] = True
            scenery[current_room].append([200, 15, 0]) # speech bubble
            scenery[current_room].append([speech_text, 15, 2])
            game_progress[1] = True
            game_progress[0] = True

    if item_player_is_on == 145: # river cat
        if not game_progress[0]:
            if planet3_progress[0]:
                speech_text = 181
            else:
                speech_text = 180
            scenery[current_room].append([200, 15, 0]) # speech bubble
            scenery[current_room].append([speech_text, 15, 2])
            scenery[current_room].append([186, 14, 0])
            scenery[current_room].append([188, 14, 14])
            game_progress[1] = True
            game_progress[0] = True

    if item_player_is_on in [143, 144]: # jailers
        if not game_progress[0]:
            if planet3_progress[1]: 
                speech_text = 185
            else:
                speech_text = 184
            scenery[current_room].append([200, 15, 0]) # speech bubble
            scenery[current_room].append([speech_text, 15, 2])
            scenery[current_room].append([187, 14, 0])
            game_progress[1] = True
            game_progress[0] = True

#HANDLE OBJECTS#

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
        if item_player_is_on == 177:
            planet3_progress[6] = True
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

    start_display = (selected_item // 11) * 11
    list_to_show = in_my_pockets[start_display : start_display + 11]
    selected_marker = selected_item % 11

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
    global room_map
    
    if can_drop(old_y, old_x):
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
    pygame.time.delay(500)

def examine_object():
    global speech_text
    
    item_player_is_on = get_item_under_player()
    left_tile_of_item = find_object_start_x()
    
    if item_player_is_on in [0, 1, 2, 3, 57, 58, 136]:
        return
    
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
    show_text("", 1)
    pygame.time.delay(500)

#MAKE MAP#

def generate_map():
    global room_map, top_left_x, top_left_y, hazard_map
    
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
            can_drop(prop_y, prop_x)): # Check for floor types
            room_map[prop_y][prop_x] = prop_number
            image_here = objects[prop_number][0]
            image_width = image_here.get_width()
            image_width_in_tiles = int(image_width / TILE_SIZE)
            for tile_number in range(1, image_width_in_tiles):
                room_map[prop_y][prop_x + tile_number] = 255

    hazard_map = []
    for y in range(ROOM_HEIGHT):
        hazard_map.append([0] * ROOM_WIDTH)

def close_text_boxes():
    global speech_text, game_progress
    global planet1_progress, planet2_progress
        
    if planet1_progress[4]:
        planet1_progress[4] = False
        scenery[current_room].remove([speech_text, 15, 2])
        speech_text = 55
        scenery[current_room].append([speech_text, 15, 2])
        pygame.time.delay(200)
        return

    elif planet1_progress[5]:
        scenery[current_room].remove([51, 15, 0])
        planet1_progress[5] = False
        scenery[current_room].append([52, 15, 0])
        planet1_progress[6] = True
        pygame.time.delay(200)
        return

    elif planet1_progress[6]:
        scenery[current_room].remove([52, 15, 0])
        planet1_progress[6] = False

    elif planet1_progress[7]:
        planet1_progress[7] = False
        scenery[current_room].remove([speech_text, 15, 2])
        speech_text = 198
        scenery[current_room].append([speech_text, 15, 2])
        pygame.time.delay(200)
        return

    elif planet1_progress[8]:
        planet1_progress[8] = False
        scenery[current_room].remove([speech_text, 15, 2])
        speech_text = 199
        scenery[current_room].append([speech_text, 15, 2])
        pygame.time.delay(200)
        return
        
    elif planet2_progress[0]:
        scenery[current_room].remove([speech_text, 15, 2])
        speech_text = 128
        scenery[current_room].append([speech_text, 15, 2])
        planet2_progress[0] = False
        planet2_progress[1] = True
        pygame.time.delay(200)
        return

    elif planet2_progress[1]:
        scenery[current_room].remove([speech_text, 15, 2])
        speech_text = 129
        scenery[current_room].append([speech_text, 15, 2])
        planet2_progress[1] = False
        pygame.time.delay(200)
        return

    elif planet2_progress[4]:
        scenery[current_room].remove([125, 15, 0])
        planet2_progress[4] = False
 
    elif game_progress[1]:
        if speech_text == 53:
            scenery[current_room].remove([speech_text, 15, 2])
            scenery[current_room].append([199, 15, 2])
            speech_text = 199

        else:
            scenery[current_room].remove([speech_text, 15, 2])    
            scenery[current_room].remove([200, 15, 0]) # remove speech bubble

            if current_room == 25:
                scenery[current_room].remove([186, 14, 0])
                scenery[current_room].remove([188, 14, 14])

            if current_room == 26:
                scenery[current_room].remove([187, 14, 0])
        
            game_progress[1] = False

    elif game_progress[2]:
        scenery[current_room].remove([203, 15, 0])
        show_text("", 0)
        game_progress[2] = False

    elif game_progress[3]:
        scenery[current_room].remove([202, 15, 0])
        show_text("", 0)
        game_progress[3] = False
        
    elif game_progress[4]:
        scenery[current_room].remove([achievement, 15, 0])
        show_text("", 0)
        game_progress[4] = False

    elif game_progress[10]: #Planet 1 to 2
        scenery[current_room].remove([212, 15, 0])
        show_text("You have arrived on a new planet!", 0)
        show_text("", 1)
        game_progress[10] = False
        game_progress[1] = True
        game_progress[0] = True
        save_progress()
        pygame.time.delay(200)
        return

    elif game_progress[11]: #Planet 2 to 3
        scenery[current_room].remove([213, 15, 0])
        show_text("You have arrived on a new planet!", 0)
        show_text("", 1)
        game_progress[11] = False
        save_progress()

    elif game_progress[12]: #Planet 3 to Earth
        scenery[current_room].remove([214, 15, 0])
        show_text("Well done! You have arrived on Earth!", 0)
        show_text("Press [A] to view your wall of achievements!", 1)
        game_progress[12] = False
        save_progress()

    game_progress[0] = False
    
    pygame.time.delay(200)

#GAME LOOP#
                
def start_room():
    show_text("You are here: " + GAME_MAP[current_room][0], 0)
    show_text("", 1)
    hazard_start()

def game_loop():
    global player_x, player_y, current_room
    global from_player_x, from_player_y
    global player_image, player_image_shadow 
    global selected_item, item_carrying
    global player_offset_x, player_offset_y
    global player_frame, player_direction
    global achievement, scenery, speech_text
    global game_progress, planet2_progress, new_game
    
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
        if game_progress[0]:
            close_text_boxes()
        pygame.time.set_timer(25, 0)
        current_room += 1
        generate_map()
        player_x = 0
        player_y = int(ROOM_HEIGHT / 2)
        player_frame = 0
        start_room()
        return

    if player_x == -1: #goes through door on the left
        if game_progress[0]:
            close_text_boxes()
        pygame.time.set_timer(25, 0)
        current_room -= 1
        generate_map()
        player_x = ROOM_WIDTH - 1
        player_y = int(ROOM_HEIGHT / 2)
        player_frame = 0
        start_room()
        return

    if player_y == ROOM_HEIGHT: #goes through door at the bottom
        if game_progress[0]:
            close_text_boxes()
        pygame.time.set_timer(25, 0)
        current_room += MAP_WIDTH
        generate_map()
        player_y = 0
        player_x = int(ROOM_WIDTH / 2)
        player_frame = 0
        start_room()
        return
    
    if player_y == -1: #goes through door at the top
        if game_progress[0]:
            close_text_boxes()
        pygame.time.set_timer(25, 0)
        current_room -= MAP_WIDTH
        generate_map()
        player_y = ROOM_HEIGHT - 1
        player_x = int(ROOM_WIDTH / 2)
        start_room()
        return

    if keys[pygame.K_w] and len(in_my_pockets) > 0:
        selected_item += 1
        if selected_item > len(in_my_pockets) - 1:
            selected_item = 0
        item_carrying = in_my_pockets[selected_item]
        display_inventory()
        pygame.time.delay(300)

    if keys[pygame.K_q] and len(in_my_pockets) > 0:
        selected_item -= 1
        if selected_item < 0:
            selected_item = len(in_my_pockets) - 1
        item_carrying = in_my_pockets[selected_item]
        display_inventory()
        pygame.time.delay(300)

    if not game_progress[13]:
        if keys[pygame.K_g]:
            pick_up_object()
            
        if keys[pygame.K_d] and item_carrying:
            drop_object(old_player_y, old_player_x)

        if keys[pygame.K_SPACE]:
            examine_object()
            speak()

        if keys[pygame.K_u]:
            use_object()
            pygame.time.delay(300)

    if keys[pygame.K_h]:
        if game_progress[0]:
            show_text("Please press Enter to continue.", 0)
        else:
            scenery[current_room].append([202, 15, 0])
            game_progress[3] = True
            game_progress[0] = True
            show_text("Help Menu", 0)
                
    if keys[pygame.K_a]:
        if game_progress[0]:
            show_text("Please press Enter to continue.", 0)
            show_text("", 1)
        else:
            if game_progress[6]:
                if game_progress[5] == False:
                    achievement = 205
            if game_progress[8]:
                if game_progress[7]:
                    if game_progress[5]:
                        achievement = 206
                    else:
                        achievement = 206
            if game_progress[9]:
                if game_progress[7]:
                    if game_progress[5]:
                        achievement = 210
                    else:
                        achievement = 208                        
                else:
                    if game_progress[5]:
                        achievement = 211
                    else:
                        achievement = 209
            scenery[current_room].append([achievement, 15, 0])
            game_progress[4] = True
            game_progress[0] = True

    if keys[pygame.K_1] or keys[pygame.K_2] or keys[pygame.K_3]:
        if planet2_progress[4]:   
            if keys[pygame.K_2]:
                speech_text = 131
                game_progress[7] = True
            else:
                speech_text = 130
            scenery[current_room].remove([125, 15, 0])
            scenery[current_room].append([200, 15, 0]) #speech bubble
            scenery[current_room].append([speech_text, 15, 2])
            game_progress[1] = True
            game_progress[0] = True
            planet2_progress[3] = False
            planet2_progress[4] = False
            game_progress[8] = True   

    if keys[pygame.K_RETURN]:
        close_text_boxes()

    if keys[pygame.K_s]:
        save_progress()
        show_text("Game progress saved.", 0)

    if keys[pygame.K_r]:
        new_game = True
        pickle.dump(new_game, open(path + "new_game.dat", "wb"))
        end_the_game("Game restarting")

    #TELEPORTER
    if keys[pygame.K_x]:
        current_room = int(input("Enter room number:"))
        player_x = 10
        player_y = 10
        generate_map()
        start_room()

    if game_progress[10]:
        player_x = 6
        player_y = 11
    elif game_progress[11]:
        player_x = 7
        player_y = 11
    elif game_progress[12]:
        player_x = 9
        player_y = 10
        player_direction = "down"
    elif room_map[player_y][player_x] not in items_player_may_stand_on \
         or hazard_map[player_y][player_x] != 0:
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

def draw_shadow(image, y, x):
    screen.blit(
        image,
        (int(top_left_x + (x * TILE_SIZE)),
         int(top_left_y + (y * TILE_SIZE)))
        )

def draw_player():
    if planet3_progress[6]:
        player_image = PLAYER_DOG[player_direction][player_frame]
        player_image_shadow = PLAYER_DOG_SHADOW[player_direction][player_frame]
    elif planet3_progress[7]:
        player_image = PLAYER_FISH[player_direction][player_frame]
        player_image_shadow = PLAYER_SHADOW[player_direction][player_frame]
    else:
        player_image = PLAYER[player_direction][player_frame]
        player_image_shadow = PLAYER_SHADOW[player_direction][player_frame]

    draw_image(player_image, player_y + player_offset_y,
               player_x + player_offset_x)
    draw_shadow(player_image_shadow, player_y + player_offset_y,
        player_x + player_offset_x)

    planet3_progress[7] = False
    
def draw():
    
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

                if y == player_y + 1 and \
                   room_map[player_y + 1][player_x] in walls:
                    wall = room_map[player_y + 1][player_x]
                    if x == player_x:
                        image = PILLARS[wall][0]
                    if x < 21 and x == player_x + 1 and \
                       room_map[player_y + 1][player_x + 1] == wall and \
                       room_map[player_y + 1][player_x + 2] == wall:
                        image = PILLARS[wall][0]
                    if x > 2 and x == player_x - 1 and \
                       room_map[player_y + 1][player_x - 1] == wall and \
                       room_map[player_y + 1][player_x - 2] == wall:
                        image = PILLARS[wall][0]
                
                draw_image(image, y, x)

                if objects[item_here][1] is not None:
                    shadow_image = objects[item_here][1]
                    draw_shadow(shadow_image, y, x)

            hazard_here = hazard_map[y][x]
            if hazard_here != 0:
                draw_image(objects[hazard_here][0], y, x)
        
        if (player_y == y):
            draw_player()

    screen.set_clip(None)

def show_text(text_to_show, line_number):
    text_lines = [15, 50]
    myfont = pygame.font.SysFont('Verdana', 20)
    textsurface = myfont.render(text_to_show, False, (0, 255, 0))

    pygame.draw.rect(screen, (0, 0, 0), (0, text_lines[line_number], 690, 35))
    screen.blit(textsurface,(20, text_lines[line_number]))

def planet_1_to_2():
    global current_room, game_progress
    global in_my_pockets, selected_item, speech_text
    
    current_room = 21
    selected_item = 0
    in_my_pockets = [201, 124]
    scenery[current_room].append([212, 15, 0])
    show_text("Press Enter to continue your journey~", 1)
    speech_text = 126
    game_progress[10] = True
    game_progress[0] = True

def planet_2_to_3():
    global current_room, game_progress
    global in_my_pockets, selected_item, speech_text
    
    current_room = 33
    selected_item = 0
    in_my_pockets = [201, 178]
    scenery[current_room].append([213, 15, 0])
    show_text("Press Enter to continue your journey~", 1)
    game_progress[11] = True
    game_progress[0] = True

def planet_3_to_earth():
    global current_room, game_progress
    global in_my_pockets, selected_item
    
    current_room = 36
    selected_item = 0
    in_my_pockets = [201]
    scenery[current_room].append([214, 15, 0])
    show_text("Press Enter to continue your journey~", 1)
    game_progress[12] = True
    game_progress[0] = True
    game_progress[13] = True

def save_progress():
    new_game = False
    pickle.dump(current_room, open(path + "current_room.dat", "wb"))
    pickle.dump(player_y, open(path + "player_y.dat", "wb"))
    pickle.dump(player_x, open(path + "player_x.dat", "wb"))
    pickle.dump(player_direction, open(path + "player_direction.dat", "wb"))
    pickle.dump(achievement, open(path + "achievement.dat", "wb"))
    pickle.dump(speech_text, open(path + "speech_text.dat", "wb"))
    pickle.dump(in_my_pockets, open(path + "in_my_pockets.dat", "wb"))
    pickle.dump(game_progress, open(path + "game_progress.dat", "wb"))
    pickle.dump(planet1_progress, open(path + "planet1_progress.dat", "wb"))
    pickle.dump(planet2_progress, open(path + "planet2_progress.dat", "wb"))
    pickle.dump(planet3_progress, open(path + "planet3_progress.dat", "wb"))
    pickle.dump(props, open(path + "props.dat", "wb"))
    pickle.dump(scenery, open(path + "scenery.dat", "wb"))
    pickle.dump(new_game, open(path + "new_game.dat", "wb"))

#health bar#

health = 100

def draw_health():
    myfont = pygame.font.SysFont('Verdana', 20)
    textsurface = myfont.render("Health", False, (0, 255, 0))

    screen.blit(textsurface,(570, 570))
    
    pygame.draw.rect(screen, (255, 255, 255), (565, 595, 110, 30))
    pygame.draw.rect(screen, BLACK, (570, 600, 100, 20))
    
    if health > 0:
        pygame.draw.rect(screen, (0, 200, 0), (570, 600, health, 20))

def replenish_health():
    global health
    
    if health < 96:
        health += 5
        
def end_the_game(reason):
    global run

    show_text(reason, 1)
    run = False
    
#hazards#

hazard_data = {
    # room number : [[y, x, direction, bounce addition, object]]
    9: [[10, 17, 3, 2, 11], [9, 20, 1, 2, 11], [12, 14, 3, 2, 11],
        [8, 11, 1, 2, 11]],
    20: [[5, 13, 2, 2, 135], [7, 17, 2, 2, 135], [10, 8, 2, 2, 135],
         [14, 13, 2, 2, 135]], 
    }

def deplete_health(penalty):
    global health, run
    
    if not run:
        return
    
    health = health - penalty
    draw_health()
    if health < 1:
        end_the_game("You ran out of health!")
        
def hazard_start():
    global current_room_hazards_list, hazard_map
    if current_room in hazard_data.keys():
        current_room_hazards_list = hazard_data[current_room]
        for hazard in current_room_hazards_list:
            hazard_y = hazard[0]
            hazard_x = hazard[1]
            hazard_map[hazard_y][hazard_x] = hazard[4]
        pygame.time.set_timer(25, 40)

def hazard_move():
    global current_room_hazards_list, hazard_data, hazard_map
    global old_player_x, old_player_y

    if not run:
        return
    
    for hazard in current_room_hazards_list:
        hazard_y = hazard[0]
        hazard_x = hazard[1]
        hazard_direction = hazard[2]

        old_hazard_x = hazard_x
        old_hazard_y = hazard_y
        hazard_map[old_hazard_y][old_hazard_x] = 0

        if hazard_direction == 1: #up
            hazard_y -= 1
        if hazard_direction == 2: #right
            hazard_x += 1
        if hazard_direction == 3: #down
            hazard_y += 1
        if hazard_direction == 4: #left
            hazard_x -= 1

        hazard_should_bounce = False

        if (hazard_y == player_y and hazard_x == player_x) or \
           (hazard_y == from_player_y and hazard_x == from_player_x
            and player_frame > 0):
            deplete_health(10)
            sound('ouch')
            hazard_should_bounce = True

        if hazard_x == ROOM_WIDTH:
            hazard_should_bounce = True
            hazard_x = ROOM_WIDTH - 1
        if hazard_x == -1:
            hazard_should_bounce = True
            hazard_x = 0
        if hazard_y == ROOM_HEIGHT:
            hazard_should_bounce = True
            hazard_y = ROOM_HEIGHT - 1
        if hazard_y == -1:
            hazard_should_bounce = True
            hazard_y = 0

        if room_map[hazard_y][hazard_x] not in items_player_may_stand_on \
           or hazard_map[hazard_y][hazard_x] != 0:
            hazard_should_bounce = True

        if hazard_should_bounce:
            hazard_y = old_hazard_y
            hazard_x = old_hazard_x
            hazard_direction += hazard[3]
            if hazard_direction > 4:
                hazard_direction -= 4
            if hazard_direction < 1:
                hazard_direction += 4
            hazard[2] = hazard_direction
    
        hazard_map[hazard_y][hazard_x] = hazard[4]
        hazard[0] = hazard_y
        hazard[1] = hazard_x
            
#mainloop#
    
clock = pygame.time.Clock()
pygame.time.set_timer(26, 5000) #replenish health
    
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(20)
    
    generate_map()
    display_inventory()
    game_loop()

    if pygame.event.get(25):
        hazard_move()
    if pygame.event.get(26):
        replenish_health()

    draw()
    draw_health()
    
    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()
