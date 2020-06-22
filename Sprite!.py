import pygame
import os
import random

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

current_room = 6 # Start at 6
player_y, player_x = 8, 9 # Start at 8,9
player_direction = "up"
player_frame = 0
player_image = PLAYER[player_direction][player_frame]
player_offset_x, player_offset_y = 0, 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class earth():

    #MAP#

    map_width = 4
    map_height = 3
    map_size = map_width * map_height

    game_map = [["Room 0"]]

    game_map += [
        #["Room name"]
        ["Earth"] #room 1
        ]

    objects = {
        #Object number : [Image, Shadow, Description]
        0: [image('earth_grass'), None, None],
        1: [image('spaceship_earth'), None, "You and Scout's spaceship"],
        2: [image('scout'), None, "Scout", "Scout"],
        90: [image('speech'), None, None],

        100: [image('letter'), None, "A letter I wrote to myself",
             "letter to self"],
        101: [image('help'), None, None],
        102: [image('letter_1'), None, None],
        103: [image('wall_of_achievements'), None, None],
        104: [image('achievement_1'), None, None],
        105: [image('achievement_1_2'), None, None],
        106: [image('achievement_2'), None, None],
        107: [image('achievement_1_2_3'), None, None],
        108: [image('achievement_1_3'), None, None],
        109: [image('achievement_2_3'), None, None],
        110: [image('achievement_3'), None, None],

        240: [image('space_1to2'), None, "Space"],
        241: [image('space_2to3'), None, "Space"],
        242: [image('space_3'), None, "Space"],
        254: [image('transparent'), None, ""],
        }

    items_player_may_carry = [100]
    items_player_may_stand_on = items_player_may_carry + [0]

    scenery = {
        #room number: [[object number, y position, x position]...]
        0: [[1, 9, 9], [2, 10, 10], [254, 10, 8], [254, 11, 9]]
        }

    #PROPS#

    props = {
        #object number: [room, y, x]
        }

    RECIPES = [
        ]

    def get_floor_type(self):
        return 0 # Grass

    def close_textboxes(self):
        global speech_bubble, text_on_screen
        
        return
    

class planet1():
    
    plank, navigation_system, gunpowder, oxygen_tank = False, False, False, False

    baby_raccoon_textbox_1, baby_raccoon_textbox_2 = False, False
    manual_page1, manual_page2 = False, False
    speech_text = 53
    
    #MAP#

    map_width = 4
    map_height = 3
    map_size = map_width * map_height

    game_map = [["Room 0 - where unused objects are kept"]]

    game_map += [
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

        # speech
        53: [image('speech_1'), None, None], # raccoon 1
        54: [image('speech_2'), None, None], # baby raccoon
        55: [image('speech_3'), None, None], # baby raccoon
        56: [image('speech_4'), None, None], # raccoon 2
        57: [image('manual_page1'), None, None],
        58: [image('manual_page2'), None, None],

        90: [image('speech'), None, None],

        100: [image('letter'), None, "A letter I wrote to myself",
             "letter to self"],
        101: [image('help'), None, None],
        102: [image('letter_1'), None, None],
        103: [image('wall_of_achievements'), None, None],
        104: [image('achievement_1'), None, None],

        240: [image('space_1to2'), None, "Space"],
        241: [image('space_2to3'), None, "Space"],
        242: [image('space_3'), None, "Space"],
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
            [19, 6, 9], [22, 4, 6], [90, 15, 0], [53, 15, 2]],
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
        43: [12, 5, 3], # Manual under broken spaceship
        44: [0, 0, 0], # Log
        45: [0, 0, 0], # Plank
        46: [12, 14, 14], # Navigation system missing a piece of magnet
        47: [0, 0, 0], # Navigation system
        48: [0, 0, 0], # Sulfur + Seashell mixture
        49: [0, 0, 0], # Sulfur + Charcoal mixture
        50: [0, 0, 0], # Charcoal + Seashell mixture
        100: [0, 0, 0], # Letter to self
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
        [50, 39, 40] # Mixture 3 + Sulfur = Gunpowder
        ]

    #USE OBJECTS#

    def use_object(self):
        global room_map, item_carrying, selected_item, in_my_pockets
        global text_on_screen, speech_bubble, speech_text, letter_1
        global treehouse_destroyed, planet1_completed

        use_message = "You fiddle around with it but don't get anywhere."
        standard_responses = {
            28: "Hot!",
            43: "You read the manual.",
            100: "You read the letter you wrote to yourself."
            }

        item_player_is_on = get_item_under_player()
        for this_item in [item_player_is_on, item_carrying]:
            if this_item in standard_responses:
                use_message = standard_responses[this_item]

        if text_on_screen == True:
            use_message = "Please press Enter to continue."

        if item_carrying == 34 and item_player_is_on == 27: # use pickaxe
            use_message = "You found a piece of iron ore!"
            add_object(31)
            sound('combine')
            self.props[item_player_is_on][0] = 0
            self.scenery[1].append([251, 11, 6])

        elif item_carrying == 35 and item_player_is_on in [12, 13, 14, 254]: # use axe
            if item_player_is_on in [12, 13, 254]:
                use_message = "You chopped off a piece of log"
                add_object(44)
                sound('combine')
            elif item_player_is_on == 14:
                use_message = "You chopped off a piece of plank"
                add_object(45)
                sound('combine')
                self.scenery[5].remove([14, 7, 6])
                self.scenery[5].append([26, 7, 6])
                treehouse_destroyed = True

        elif item_carrying == 44 and item_player_is_on == 23: # use crafting table
            use_message = "You crafted planks from the log"
            add_object(45)
            remove_object(44)
            sound('combine')

        elif item_player_is_on in [24, 250] and item_carrying in [38, 40, 45, 47]: # broken spaceship
            if item_carrying == 45: # fix plank
                use_message = "You fix the plank to the spaceship"
                self.plank = True
                remove_object(45)
            elif item_carrying == 47: # fix navigation system
                use_message = "You fix the navigation system to the spaceship"
                self.navigation_system = True
                remove_object(47)
            elif item_carrying == 40: # add gunpowder
                use_message = "You add gunpowder into the rocket booster"
                self.gunpowder = True
                remove_object(40)
            elif item_carrying == 38: # fix oxygen tank
                use_message = "You fix the oxygen tank to the spaceship"
                self.oxygen_tank = True
                remove_object(38)
            if self.plank == True and self.navigation_system == True and \
            self.gunpowder == True and self.oxygen_tank == True:
                self.scenery[12].remove([24, 5, 3])
                self.scenery[12].append([25, 5, 3])
                planet1_completed = True
                if treehouse_destroyed == False:
                    use_message = "You've fixed the spaceship and you can leave the planet!"
                    show_text("The raccoons gave you a souvenir! Press [A] to view it.", 1)
                elif treehouse_destroyed:
                    use_message = "You've fixed the spaceship and you can leave! The raccoons"
                    show_text("seem upset about the treehouse and did not give you a souvenir.", 1)
            sound('combine')

        elif item_player_is_on == 25: # Fixed spaceship
            use_message = "You're travelling through space!"
            show_text("", 1)
            planet_1_to_2()

        elif item_player_is_on == 43 or item_carrying == 43:
            if self.manual_page1 == False and text_on_screen == False:
                self.scenery[current_room].append([57, 15, 0])
                self.manual_page1 = True
                text_on_screen = True

        elif item_player_is_on == 100 or item_carrying == 100:
            if letter_1 == False and text_on_screen == False:
                self.scenery[current_room].append([102, 15, 0])
                letter_1 = True
                text_on_screen = True
                
        for recipe in self.RECIPES:
            ingredient1 = recipe[0]
            ingredient2 = recipe[1]
            combination = recipe[2]
            if (item_carrying == ingredient1
                and item_player_is_on == ingredient2) \
                or (item_carrying == ingredient2
                    and item_player_is_on == ingredient1):
                use_message = "You combine " + self.objects[ingredient1][3] \
                              + " and " + self.objects[ingredient2][3] \
                              + " to make " + self.objects[combination][3]
                if item_player_is_on in self.props.keys():
                    self.props[item_player_is_on][0] = 0
                    room_map[player_y][player_x] = self.get_floor_type()
                in_my_pockets.remove(item_carrying)
                add_object(combination)
                sound('combine')

        show_text(use_message, 0)
    
    def get_floor_type(self):
        if current_room in [8, 12]:
            return 2 # Sand
        else:
            return 0 # Grass

    def can_drop(self, old_y, old_x):
        if room_map[old_y][old_x] in [0, 1, 2]:
            if current_room == 11 and old_x > 17:
                return False
            else:
                return True
        else:
            return False

    def speak(self):
        global speech_bubble, text_on_screen

        item_player_is_on = get_item_under_player()

        if item_player_is_on in [19, 20, 21]: # dialogue with raccoons
            if speech_bubble == False:
                if item_player_is_on == 19: # raccoon 1
                    self.speech_text = 53
                elif item_player_is_on == 20: # raccoon 2
                    self.speech_text = 56
                elif item_player_is_on == 21: # baby raccoon
                    self.speech_text = 54
                    self.baby_raccoon_textbox_1 = True
                self.scenery[current_room].append([90, 15, 0]) # speech bubble
                self.scenery[current_room].append([self.speech_text, 15, 2])
                speech_bubble = True
                text_on_screen = True

    def close_textboxes(self):
        global speech_bubble, text_on_screen
        
        if self.baby_raccoon_textbox_1:
            self.baby_raccoon_textbox_1 = False
            self.speech_text = 55
            self.scenery[current_room].append([90, 15, 0]) # speech bubble
            self.scenery[current_room].append([self.speech_text, 15, 2])
            self.baby_raccoon_textbox_2 = True

        elif self.baby_raccoon_textbox_2:
            self.scenery[current_room].remove([self.speech_text, 15, 2])
            self.baby_raccoon_textbox_2 = False
            self.scenery[current_room].remove([90, 15, 0]) # remove speech bubble
            speech_bubble = False
            text_on_screen = False
            
        elif self.manual_page1:
            self.scenery[current_room].remove([57, 15, 0])
            self.manual_page1 = False
            self.scenery[current_room].append([58, 15, 0])
            self.manual_page2 = True

        elif self.manual_page2:
            self.scenery[current_room].remove([58, 15, 0])
            self.manual_page2 = False
            text_on_screen = False
                
        pygame.time.delay(500)

class planet2():

    mayor_speech_1, mayor_speech_2, mayor_speech_3 = False, False, False
    speech_text = 91
    
    #MAP#

    map_width = 4
    map_height = 3
    map_size = map_width * map_height

    game_map = [["Room 0 - where unused objects are kept"]]

    game_map += [
        #["Room name"]
        ["Student's House"], #room 1
        ["Road"], #room 2
        ["Fisherman's House"], #room 3
        ["Abandoned research centre"], #room 4
        ["Penguin Town Hall"], #room 5
        ["Road"], #room 6
        ["Scientist's house"], #room 7
        ["Abandoned research centre"], #room 8
        ["Spaceship Landing Area"], #room 9
        ["Road"], #room 10
        ["Road"], #room 11
        ["Road with a dead end"], #room 12
        ]

    objects = {
        #Object number : [Image, Shadow, Description]
        0: [image('road_tile'), None, None],
        1: [image('concrete'), None, None],
        3: [image('ice_bricks'), None, "Bricks from ice"],
        4: [image('ice_bricks_long'), None, "Bricks from ice"],
        5: [image('ice_bricks_short'), None, "Bricks from ice"],
        6: [image('sea_with_ice_1'), None, None],
        7: [image('sea_with_ice_2'), None, None],
        8: [image('sea_with_ice_3'), None, None],
        9: [image('sea_with_ice_4'), None, None],
        10: [image('sea_with_ice_5'), None, None],
        11: [image('sea_with_ice_6'), None, None],
        12: [image('sea_with_ice_7'), None, None],
        13: [image('sea_with_ice_8'), None, None],
        14: [image('sea_with_ice_9'), None, None],
        15: [image('sea_with_ice_10'), None, None],
        16: [image('sea_with_ice_11'), None, None],
        17: [image('penguin_1'), None, "The fisherman"],
        18: [image('penguin_2'), None, "The scientist"],
        19: [image('penguin_3'), None, "The student"],
        20: [image('penguin_mayor'), None, "The Penguin Mayor"],
        21: [image('spaceship'), None, "Your spaceship. It needs fuel."],
        22: [image('crowd_1'), None, "A crowd of penguins"],
        23: [image('crowd_2'), None, "A crowd of penguins"],
        24: [image('ice_wall'), None, "Wall made of ice"],
        25: [image('ice_wall_1'), None, "Wall made of ice"],
        26: [image('ice_wall_long'), None, "Wall made of ice"],
        27: [image('fence'), None, "A fence"],
        28: [image('desk'), None, "A desk"],
        29: [image('pile_of_snow'), None, "Pile of snow"],
        30: [image('gate_unlocked_1'), None, "An open gate"],
        31: [image('gate_unlocked_2'), None, "An open gate"],
        32: [image('gate_locked'), None, "A gate with a padlock"],
        33: [image('ice_wall_short'), None, "Wall made of ice"],
        34: [image('computer'), None, "Row of computers displaying strange \
images"],
        35: [image('door_closed'), None, "A door which is locked"],
        36: [image('door_open_1'), None, "An open door"],
        37: [image('door_open_2'), None, "An open door"],
        38: [image('steam_machine'), None, "A machine which is left running"],
        39: [image('gate_left'), None, "A gate"],
        40: [image('gate_right'), None, "A gate"],
        41: [image('fishing_rod'), None, "A collection of fishing rods"],
        42: [image('whiteboard'), None, "A whiteboard filled with calculations"],
        43: [image('shelf_1'), None, "A shelf with assorted items"],
        44: [image('shelf_2'), None, "A shelf with assorted items"],
        45: [image('chair'), None, "A chair"],
        46: [image('chair_2'), None, "A chair"],
        47: [image('science_table'), None, "A table full of burning hot \
science equipment"],
        48: [image('science_table_2'), None, "Home experiments. The \
equipment is hot!"],
        49: [image('fishtank'), None, "A fish tank"],
        50: [image('bed_1'), None, "A bed"],
        51: [image('bed_2'), None, "A bed"],
        52: [image('bed_3'), None, "A bed"],
        53: [image('chair_3'), None, "A chair"],
        54: [image('chair_4'), None, "A chair"],
        55: [image('chair_5'), None, "A chair"],
        56: [image('table_2'), None, "A table"],
        57: [image('plant_pot'), None, "A potted plant"],
        58: [image('cupboard'), None, "Cupboards"],
        59: [image('shelf_3'), None, "Some cupboards and shelves"],
        60: [image('table_3'), None, "A table with matches and fishing hooks"],
        61: [image('chair_6'), None, "A chair"],
        62: [image('research_table_1'), None, "A table full of books and \
research papers"],
        63: [image('research_table_2'), None, "A table full of books and \
research papers"],
        64: [image('trapdoor'), None, "A trapdoor"],
        65: [image('spaceship'), None, "Your spaceship. It is ready to take off."],

        66: [image('access_card'), None, "An access card", "an access card"],
        67: [image('key'), None, "An old and rusty key", "a key"],
        68: [image('shovel'), None, "A shovel", "a shovel"],
        69: [image('fuel'), None, "A fuel tank", "a fuel tank"],
        
        89: [image('choose_culprit'), None, None],
        90: [image('speech'), None, None],
        91: [image('speech_5'), None, None], # Self
        92: [image('speech_6'), None, None], # Mayor
        93: [image('speech_7'), None, None],
        94: [image('speech_8'), None, None],
        95: [image('speech_9'), None, None], # Not convinced
        96: [image('speech_10'), None, None], # Convinced
        97: [image('speech_fisherman'), None, None],
        98: [image('speech_scientist'), None, None],
        99: [image('speech_student'), None, None],
        100: [image('letter'), None, "A letter I wrote to myself",
             "letter to self"],
        101: [image('help'), None, None],
        102: [image('letter_1'), None, None],
        103: [image('wall_of_achievements'), None, None],
        104: [image('achievement_1'), None, None],
        105: [image('achievement_1_2'), None, None],
        106: [image('achievement_2'), None, None],

        240: [image('space_1to2'), None, "Space"],
        241: [image('space_2to3'), None, "Space"],
        242: [image('space_3'), None, "Space"],

        247: [image('transparent'), None, "A trapdoor"],
        248: [image('transparent'), None, "A fence"],
        249: [image('transparent'), None, "An open door"],
        250: [image('transparent'), None, "A machine which is left running"],
        251: [image('transparent'), None, "A table full of books and \
research papers"],
        252: [image('transparent'), None, "Wall made of ice"],
        253: [image('transparent'), None, "A crowd of penguins"],
        254: [image('transparent'), None, "An open gate"]
        }

    items_player_may_carry = list(range(66, 70))
    items_player_may_stand_on = items_player_may_carry + [0, 1, 64, 247]

    #SCENERY#

    scenery = {
        #room number: [[object number, y position, x position]...]
        1: [[24, 4, 0], [24, 5, 0], [24, 6, 0], [24, 7, 0], [24, 8, 0],
            [24, 9, 0], [24, 10, 0], [24, 11, 0], [24, 12, 0], [24, 13, 0],
            [24, 14, 0], [24, 4, 22], [24, 5, 22], [24, 11, 22], [24, 12, 22],
            [24, 13, 22], [24, 14, 22], [26, 15, 0], [26, 3, 0], [50, 11, 2],
            [49, 5, 19], [43, 5, 1], [44, 5, 7], [43, 5, 13], [45, 8, 10],
            [47, 8, 11], [46, 8, 15], [45, 11, 10], [48, 11, 11], [46, 11, 15]],
        2: [[3, 10, 8], [3, 11, 8], [3, 12, 8], [3, 13, 8], [3, 14, 8],
            [3, 15, 8], [3, 10, 14], [3, 11, 14], [3, 12, 14], [3, 13, 14],
            [3, 14, 14], [3, 15, 14], [4, 3, 0], [5, 9, 0], [5, 9, 14],
            [6, 15, 0], [7, 15, 15], [14, 2, 0]],
        3: [[24, 4, 22], [24, 5, 22], [24, 6, 22], [24, 7, 22], [24, 8, 22],
            [24, 9, 22], [24, 10, 22], [24, 11, 22], [24, 12, 22], [24, 13, 22],
            [24, 14, 22], [26, 15, 0], [26, 3, 0], [24, 4, 0], [24, 5, 0],
            [24, 6, 0], [24, 12, 0], [24, 13, 0], [24, 14, 0], [52, 11, 16],
            [61, 6, 15], [60, 6, 16], [59, 5, 1], [41, 4, 9]],
        4: [[24, 4, 0], [24, 5, 0], [24, 6, 0], [24, 7, 0], [24, 8, 0],
            [24, 9, 0], [24, 10, 0], [24, 11, 0], [24, 12, 0], [24, 13, 0],
            [24, 14, 0], [24, 4, 22], [24, 5, 22], [24, 6, 22], [24, 7, 22],
            [24, 8, 22], [24, 9, 22], [24, 10, 22], [24, 11, 22],
            [24, 12, 22], [24, 13, 22], [24, 14, 22], [26, 3, 0],
            [33, 15, 0], [33, 15, 14], [62, 13, 2] , [38, 8, 15], [42, 3, 4],
            [250, 4, 15], [250, 5, 15], [250, 6, 15], [250, 7, 15],
            [251, 6, 2], [251, 6, 3], [251, 6, 4], [251, 7, 2],
            [251, 7, 3], [251, 7, 4], [251, 8, 2], [251, 8, 3], [251, 8, 4],
            [251, 9, 2], [251, 9, 3], [251, 9, 4], [251, 10, 2], [251, 10, 3],
            [251, 10, 4], [251, 11, 2], [251, 11, 3], [251, 11, 4], [251, 12, 2],
            [251, 12, 3], [251, 12, 4], ],
        5: [[24, 4, 0], [24, 5, 0], [24, 6, 0], [24, 7, 0], [24, 8, 0],
            [24, 9, 0], [24, 10, 0], [24, 11, 0], [24, 12, 0], [24, 13, 0],
            [24, 14, 0], [24, 15, 0], [24, 15, 1], [24, 15, 2], [24, 15, 3],
            [24, 15, 4], [24, 15, 5], [24, 15, 6], [24, 15, 7], [24, 15, 8],
            [24, 15, 9], [24, 15, 13], [24, 15, 14], [24, 15, 15], [24, 15, 16],
            [24, 15, 17], [24, 15, 18], [24, 15, 19], [24, 15, 20], [24, 15, 21],
            [24, 15, 22], [252, 14, 9], [252, 13, 9], [252, 14, 13], [252, 13, 13], 
            [26, 3, 0], [24, 4, 22], [24, 5, 22], [24, 11, 22], [24, 12, 22],
            [24, 13, 22], [24, 14, 22], [17, 6, 3], [18, 6, 5], [19, 6, 7],
            [20, 7, 11], [22, 12, 1], [23, 12, 13], [27, 6, 2], [253, 10, 1],
            [253, 10, 2], [253, 10, 3], [253, 10, 4], [253, 10, 5],
            [253, 10, 6], [253, 10, 7], [253, 10, 8], [253, 10, 9],
            [253, 11, 9], [253, 12, 9], [253, 13, 9], [253, 11, 13],
            [253, 10, 13], [253, 10, 14], [253, 10, 15], [253, 10, 16],
            [253, 10, 17], [253, 10, 18], [253, 10, 19], [253, 10, 20],
            [248, 5, 2], [248, 4, 2], [248, 5, 8], [248, 4, 8]],
        6: [[3, 1, 8], [3, 2, 8], [3, 3, 8], [3, 4, 8], [3, 1, 14],
            [3, 2, 14], [3, 3, 14], [3, 4, 14], [3, 12, 8], [3, 13, 8],
            [3, 14, 8], [3, 15, 8], [3, 12, 14], [3, 13, 14], [3, 14, 14],
            [3, 15, 14], [5, 5, 0], [5, 11, 0], [5, 5, 14], [5, 11, 14],
            [8, 4, 0], [9, 4, 15], [10, 15, 0], [11, 15, 15]],
        7: [[24, 4, 22], [24, 5, 22], [24, 6, 22], [24, 7, 22], [24, 8, 22],
            [24, 9, 22], [24, 10, 22], [24, 11, 22], [24, 12, 22], [24, 13, 22],
            [24, 14, 22], [26, 15, 0], [26, 3, 0], [24, 4, 0], [24, 5, 0],
            [24, 6, 0], [24, 12, 0], [24, 13, 0], [24, 14, 0], [58, 6, 1],
            [58, 6, 14], [57, 5, 9], [57, 5, 13], [28, 5, 10], [53, 6, 11],
            [54, 11, 3], [55, 11, 7], [56, 11, 4], [51, 11, 17], [64, 9, 21],
            [247, 8, 21], [247, 7, 21]],
        8: [[24, 4, 0], [24, 5, 0], [24, 6, 0], [24, 7, 0], [24, 8, 0],
            [24, 9, 0], [24, 10, 0], [24, 11, 0], [24, 12, 0], [24, 13, 0],
            [24, 14, 0], [24, 4, 22], [24, 5, 22], [24, 6, 22], [24, 7, 22],
            [24, 8, 22], [24, 9, 22], [24, 10, 22], [24, 11, 22],
            [24, 12, 22], [24, 13, 22], [24, 14, 22], [33, 3, 0], [33, 3, 14],
            [33, 15, 0], [33, 15, 14], [34, 4, 2], [34, 4, 4], [34, 4, 6],
            [34, 4, 15], [34, 4, 17], [34, 4, 19], [35, 3, 9], [62, 13, 2],
            [63, 13, 18], [251, 6, 2], [251, 6, 3], [251, 6, 4], [251, 7, 2],
            [251, 7, 3], [251, 7, 4], [251, 8, 2], [251, 8, 3], [251, 8, 4],
            [251, 9, 2], [251, 9, 3], [251, 9, 4], [251, 10, 2], [251, 10, 3],
            [251, 10, 4], [251, 11, 2], [251, 11, 3], [251, 11, 4], [251, 12, 2],
            [251, 12, 3], [251, 12, 4], [251, 6, 18], [251, 6, 19], [251, 6, 20],
            [251, 7, 18], [251, 7, 19], [251, 7, 20], [251, 8, 18], [251, 8, 19],
            [251, 8, 20], [251, 9, 18], [251, 9, 19], [251, 9, 20], [251, 10, 18],
            [251, 10, 19], [251, 10, 20], [251, 11, 18], [251, 11, 19], [251, 11, 20],
            [251, 12, 18], [251, 12, 19], [251, 12, 20]],
        9: [[21, 10, 5], [39, 5, 0], [40, 5, 14], [3, 6, 0], [3, 7, 0],
            [3, 8, 0], [3, 9, 0], [3, 10, 0], [3, 11, 0], [3, 12, 0], 
            [3, 13, 0], [3, 14, 0], [4, 15, 0], [3, 6, 22], [3, 7, 22], 
            [3, 8, 22], [3, 9, 22], [3, 10, 22], [3, 11, 22], [3, 12, 22],
            [3, 13, 22], [3, 14, 22], [90, 15, 0], [91, 15, 2], [254, 1, 8],
            [254, 2, 8], [254, 3, 8], [254, 1, 14], [254, 2, 14], [254, 3, 14]],
        10: [[3, 1, 8], [3, 2, 8], [3, 3, 8], [3, 4, 8], [3, 5, 8],
             [3, 6, 8], [3, 7, 8], [3, 8, 8], [3, 9, 8], [3, 10, 8],
             [3, 11, 8], [3, 12, 8], [3, 1, 14], [3, 2, 14], [3, 3, 14],
             [3, 4, 14], [3, 5, 14], [3, 6, 14], [4, 13, 0],
             [5, 7, 14], [12, 6, 15], [13, 15, 0]],
        11: [[4, 7, 0], [4, 13, 0], [15, 15, 0], [16, 6, 0]],
        12: [[3, 8, 22], [3, 9, 22], [3, 10, 22], [3, 11, 22], [3, 12, 22],
             [4, 13, 0], [15, 15, 0], [29, 7, 0], [254, 1, 9], [254, 2, 9],
             [254, 3, 9], [254, 4, 9], [254, 5, 9], [254, 6, 0], [254, 1, 13],
             [254, 2, 13], [254, 3, 13], [254, 4, 13], [254, 5, 13]]
        }

    #PROPS#

    props = {
        #object number: [room, y, x]
        66: [8, 5, 2], #access card
        67: [7, 5, 13], #key
        68: [3, 5, 1], #shovel
        69: [1, 5, 7], #fuel tank
        100: [0, 0, 0] #letter
        }

    RECIPES = [
        ]

    #USE OBJECTS#

    def use_object(self):
        global room_map, item_carrying, selected_item, in_my_pockets, visited_centre
        global text_on_screen, letter_1, speech_bubble

        use_message = "You fiddle around with it but don't get anywhere."
        standard_responses = {
            100: "You read the letter you wrote to yourself."
            }

        item_player_is_on = get_item_under_player()
        for this_item in [item_player_is_on, item_carrying]:
            if this_item in standard_responses:
                use_message = standard_responses[this_item]

        if text_on_screen == True:
            use_message = "Please press Enter to continue."

        if item_player_is_on == 35 and item_carrying == 66:
            use_message = "You used the access card to unlock the door!"
            self.scenery[current_room].remove([35, 3, 9])
            self.scenery[current_room].append([36, 3, 9])
            self.scenery[current_room].append([37, 3, 13])
            self.scenery[current_room].append([249, 1, 9])
            self.scenery[current_room].append([249, 2, 9])
            self.scenery[current_room].append([249, 1, 13])
            self.scenery[current_room].append([249, 2, 13])
            sound('combine')
            visited_centre = True

        elif item_player_is_on == 32 and item_carrying == 67:
            use_message = "You used the key to unlock the gate!"
            self.scenery[current_room].remove([32, 6, 0])
            self.scenery[current_room].append([30, 6, 0])
            self.scenery[current_room].append([31, 6, 13])
            sound('combine')

        elif item_player_is_on == 29 and item_carrying == 68:
            use_message = "You shovel the snow away to reveal a hidden gate"
            self.scenery[current_room].remove([29, 7, 0])
            self.scenery[current_room].append([3, 7, 9])
            self.scenery[current_room].append([3, 7, 13])
            self.scenery[current_room].append([5, 7, 0])
            self.scenery[current_room].append([5, 7, 14])
            self.scenery[current_room].append([32, 6, 0])
            sound('combine')

        elif item_player_is_on == 21 and item_carrying == 69:
            use_message = "You add fuel to your spaceship"
            self.scenery[current_room].remove([21, 10, 5])
            self.scenery[current_room].append([65, 10, 5])
            remove_object(69)
            sound('combine')

        elif item_player_is_on == 65: # Fixed spaceship
            use_message = "You're travelling through space!"
            show_text("", 1)
            planet2_completed = True
            letter_1 = False
            speech_bubble = False
            planet_2_to_3()

        elif item_player_is_on == 100 or item_carrying == 100:
            if letter_1 == False and text_on_screen == False:
                self.scenery[current_room].append([102, 15, 0])
                letter_1 = True
                text_on_screen = True

        show_text(use_message, 0)
    
    def get_floor_type(self):
        if current_room in (1, 3, 4, 5, 7, 8):
            return 1
        else:
            return 0

    def can_drop(self, old_y, old_x):
        return room_map[old_y][old_x] in [0, 1]

    def speak(self):
        global speech_bubble, text_on_screen

        item_player_is_on = get_item_under_player()

        if item_player_is_on in [17, 18, 19]: # dialogue with penguins
            if speech_bubble == False:
                if visited_centre == False:
                    if item_player_is_on == 17:  # fisherman
                        self.speech_text = 97
                    elif item_player_is_on == 18: # scientist
                        self.speech_text = 98
                    elif item_player_is_on == 19: # student
                        self.speech_text = 99
                    self.scenery[current_room].append([90, 15, 0]) # speech bubble
                    self.scenery[current_room].append([self.speech_text, 15, 2])
                    speech_bubble = True
                    text_on_screen = True
                else:
                    return

        if item_player_is_on == 20: # dialogue with mayor
            if speech_bubble == False:
                if visited_centre == False:
                    self.speech_text = 92
                    self.mayor_speech_1 = True
                    self.scenery[current_room].append([90, 15, 0]) # speech bubble
                    self.scenery[current_room].append([self.speech_text, 15, 2])
                    speech_bubble = True
                    text_on_screen = True
                else:
                    if can_guess:
                        planet.speech_text = 89
                        self.scenery[current_room].append([90, 15, 0]) # speech bubble
                        self.scenery[current_room].append([self.speech_text, 15, 2])
                        speech_bubble = True
                        text_on_screen = True
                    else:
                        if item_player_is_on == 20:
                            show_text("You have used up your only chance to \
identify the culprit", 0)


    def close_textboxes(self):
        global speech_bubble, text_on_screen
        
        if self.mayor_speech_1:
            self.scenery[current_room].append([90, 15, 0]) # speech bubble
            self.scenery[current_room].append([93, 15, 2])
            self.mayor_speech_1 = False
            self.mayor_speech_2 = True

        elif self.mayor_speech_2:
            self.scenery[current_room].remove([93, 15, 2])
            self.scenery[current_room].append([94, 15, 2])
            self.mayor_speech_2 = False
            self.mayor_speech_3 = True

        elif self.mayor_speech_3:
            self.scenery[current_room].remove([94, 15, 2])
            self.scenery[current_room].remove([90, 15, 0]) # remove speech bubble
            self.mayor_speech_3 = False
            speech_bubble = False
            text_on_screen = False
                
        pygame.time.delay(500)

class planet3():

    river_cat_fish = False
    jailer_fish = False
    no_fish = True
    one_fish, two_fish = False, False
    #speech_text = 0
    
    #MAP#

    map_width = 3
    map_height = 3
    map_size = map_width * map_height

    game_map = [["Room 0 - where unused objects are kept"]]

    game_map += [
        #["Room name"]
        ["River"], #room 1
        ["Village"], #room 2
        ["The Maze"], #room 3
        ["River"], #room 4
        ["Village"], #room 5
        ["Village"], #room 6
        ["Spaceship Landing Area"], #room 7
        ["Village"], #room 8
        ["Village"], #room 9
        ]

    objects = {
        #Object number : [Image, Shadow, Description]
        0: [image('floor_tile'), None, None],

        3: [image('tree_room7'), None, "A tree"],
        4: [image('tree_room8'), None, "A tree"],
        5: [image('rock_2'), None, "A rock"],
        6: [image('rock_2_long'), None, "A rock"],
        7: [image('spaceship'), None, "Your spaceship"],
        8: [image('spaceship_dog'), None, "Scout's spaceship! \
It needs to be attached to mine."],
        9: [image('cat_jailer_1'), None, "A cat"],
        10: [image('cat_jailer_2'), None, "A cat"],
        11: [image('cat_river'), None, "A cat"],
        12: [image('river'), None, "The river bank"],
        13: [image('tree_room1'), None, "A tree"],
        14: [image('tree_room4'), None, "A tree"],
        15: [image('tree_2'), None, "A tree"],
        16: [image('wall'), None, "Wooden walls"],
        17: [image('longwall'), None, "Wooden walls"],
        18: [image('wooden_door'), None, "The door is locked and Scout is \
inside!"],
        19: [image('tree_room2_1'), None, "A tree"],
        20: [image('tree_room2_2'), None, "A tree"],
        21: [image('maze_fence'), None, "A fence"],
        22: [image('tree_room5'), None, "A tree"],
        23: [image('tree_room6_1'), None, "A tree"],
        24: [image('tree_room6_2'), None, "A tree"],
        25: [image('tree_room6_3'), None, "A tree"],
        26: [image('tree_room6_4'), None, "A tree"],
        27: [image('twine'), None, "A bunch of twines"],
        28: [image('tree_room6_5'), None, "A tree"],
        29: [image('tree_room6_6'), None, "A tree"],
        30: [image('tree_room9_1'), None, "A tree"],
        31: [image('tree_room9_2'), None, "A tree"],
        32: [image('fence_2'), None, "A locked fence"],
        33: [image('cats_unfriendly'), None, "A cat"],
        34: [image('house'), None, "The villagers' house"],
        35: [image('spaceships'), None, "You and Scout's spaceship"],
        
        #props
        50: [image('fishing_rod_2'), None, "A fishing rod", "fishing rod"],
        51: [image('string'), None, "A piece of string", "string"],
        52: [image('stick'), None, "A stick", "the stick"],
        53: [image('shears'), None, "A pair of shears", "the shears"],
        54: [image('fish'), None, "A fish", "the fish"],
        55: [image('key_2'), None, "A rusty key", "the key"],
        56: [image('scout'), None, "Scout", "Scout"],
        57: [image('scout_in_spaceship'), None, "Scout in his spaceship",
             "Scout's spaceship"],

        #speech
        90: [image('speech'), None, None],
        91: [image('speech_cat1'), None, None],
        92: [image('speech_cat2'), None, None],
        93: [image('speech_fish'), None, None],
        94: [image('speech_fish2'), None, None],
        95: [image('speech_jailer'), None, None],
        96: [image('speech_jailer2'), None, None],
        
        100: [image('letter'), None, "A letter I wrote to myself",
             "letter to self"],
        101: [image('help'), None, None],
        102: [image('letter_1'), None, None],
        103: [image('wall_of_achievements'), None, None],
        104: [image('achievement_1'), None, None],
        105: [image('achievement_1_2'), None, None],
        106: [image('achievement_2'), None, None],
        107: [image('achievement_1_2_3'), None, None],
        108: [image('achievement_1_3'), None, None],
        109: [image('achievement_2_3'), None, None],
        110: [image('achievement_3'), None, None],

        120: [image('river_crop'), None, "The river bank"],
        121: [image('tree_room2_2_crop'), None, "A tree"],
        122: [image('tree_room6_2_crop'), None, "A tree"],

        240: [image('space_1to2'), None, "Space"],
        241: [image('space_2to3'), None, "Space"],
        242: [image('space_3'), None, "Space"],

        251: [image('transparent'), None, "The villagers' house"],
        252: [image('transparent'), None, "A locked fence"],
        253: [image('transparent'), None, "The river bank"],
        254: [image('transparent'), None, "A tree"]
        }

    items_player_may_carry = list(range(50,58)) + [100]
    items_player_may_stand_on = items_player_may_carry + [0]

    #SCENERY#

    scenery = {
        #room number: [[object number, y position, x position]...]
        1: [[11, 6, 9], [12, 15, 0], [13, 3, 8], [253, 4, 7], [253, 5, 7],
            [253, 6, 7], [253, 7, 7], [253, 8, 7], [253, 9, 7], [253, 10, 7], 
            [253, 11, 7], [253, 12, 7], [253, 13, 7], [253, 14, 7], [24, 15, 14]],
        2: [[19, 3, 0], [20, 15, 0],
            [16, 4, 13], [16, 5, 13], [16, 6, 13], [16, 7, 13], [16, 8, 13],
            [16, 9, 13], [16, 10, 13], [16, 10, 14], [16, 10, 15], [16, 10, 18],
            [16, 10, 19], [16, 10, 20], [16, 10, 21], [16, 10, 22], [17, 3, 13],
            [18, 10, 16], [9, 11, 15], [10, 11, 18], [254, 11, 21], [254, 12, 21],
            [254, 13, 21], [254, 14, 21]],
        3: [[21, 15, 0], [21, 15, 1], [21, 15, 2], [21, 15, 3], [21, 15, 4], 
            [21, 15, 5], [21, 15, 6], [21, 15, 7], [21, 15, 8], [21, 15, 9],
            [21, 15, 13], [21, 15, 14], [21, 15, 15], [21, 15, 16], [21, 15, 17],
            [21, 15, 18], [21, 15, 19], [21, 15, 20], [21, 15, 21], [21, 15, 22],
            [21, 14, 0], [21, 14, 2], [21, 14, 9], [21, 14, 17], [21, 14, 22],
            [21, 13, 0], [21, 13, 2], [21, 13, 3], [21, 13, 4], [21, 13, 5],
            [21, 13, 6], [21, 13, 7], [21, 13, 9], [21, 13, 14], [21, 13, 15],
            [21, 13, 17], [21, 13, 19], [21, 13, 20], [21, 13, 22], [21, 12, 0], 
            [21, 12, 7], [21, 12, 9], [21, 12, 10], [21, 12, 11], [21, 12, 12], 
            [21, 12, 15], [21, 12, 17], [21, 12, 20], [21, 12, 22], [21, 11, 0], 
            [21, 11, 7], [21, 11, 12], [21, 11, 13], [21, 11, 15], [21, 11, 17], 
            [21, 11, 18], [21, 11, 20], [21, 11, 22], [21, 10, 0], [21, 10, 1], 
            [21, 10, 3], [21, 10, 4], [21, 10, 5], [21, 10, 6], [21, 10, 7], 
            [21, 10, 10], [21, 10, 11], [21, 10, 12], [21, 10, 15], [21, 10, 20], 
            [21, 10, 22], [21, 9, 3], [21, 9, 10], [21, 9, 14], [21, 9, 15], 
            [21, 9, 17], [21, 9, 18], [21, 9, 19], [21, 9, 20], [21, 9, 22], 
            [21, 8, 3], [21, 8, 5], [21, 8, 6], [21, 8, 7], [21, 8, 8], 
            [21, 8, 9], [21, 8, 10], [21, 8, 12], [21, 8, 13], [21, 8, 14], 
            [21, 8, 17], [21, 8, 22], [21, 7, 3], [21, 7, 20], [21, 7, 21], 
            [21, 7, 22], [21, 6, 3], [21, 6, 4], [21, 6, 5], [21, 6, 6], 
            [21, 6, 7], [21, 6, 8], [21, 6, 10], [21, 6, 11], [21, 6, 12], 
            [21, 6, 13], [21, 6, 14], [21, 6, 15], [21, 6, 16], [21, 6, 17], 
            [21, 6, 20], [21, 6, 22],  [21, 5, 0],  [21, 5, 1], [21, 5, 3], 
            [21, 5, 11], [21, 5, 20], [21, 5, 22], [21, 4, 0], [21, 4, 3], 
            [21, 4, 4], [21, 4, 5], [21, 4, 6], [21, 4, 7], [21, 4, 8], 
            [21, 4, 9], [21, 4, 10], [21, 4, 11], [21, 4, 12], [21, 4, 14], 
            [21, 4, 16], [21, 4, 17], [21, 4, 19], [21, 4, 20], [21, 4, 22],
            [21, 3, 0], [21, 3, 14], [21, 3, 22], [21, 2, 0], [21, 2, 1],
            [21, 2, 2], [21, 2, 3], [21, 2, 4], [21, 2, 5], [21, 2, 6],
            [21, 2, 7], [21, 2, 8], [21, 2, 9], [21, 2, 10], [21, 2, 11], 
            [21, 2, 12], [21, 2, 13], [21, 2, 14], [21, 2, 15], [21, 2, 16], 
            [21, 2, 17], [21, 2, 18], [21, 2, 19],  [21, 2, 20], [21, 2, 21],
            [21, 2, 22], [32, 9, 0], [252, 6, 0], [252, 7, 0], [252, 8, 0]],
        4: [[12, 15, 0], [14, 15, 8], [29, 5, 14], [254, 1, 14], [254, 2, 14],
            [254, 3, 14], [254, 4, 14], [253, 1, 7], [253, 2, 7],
            [253, 3, 7], [253, 4, 7], [253, 5, 7], [253, 6, 7], [253, 7, 7],
            [253, 8, 7], [253, 9, 7], [253, 10, 7], [253, 11, 7], [253, 12, 7],
            [253, 13, 7], [253, 14, 7]],
        5: [[3, 5, 0], [22, 15, 0]],
        6: [[23, 15, 0], [24, 15, 14], [25, 5, 0], [26, 5, 14], [27, 5, 9],
            [5, 6, 22], [5, 7, 22], [5, 8, 22], [5, 9, 22], [5, 10, 22],
            [5, 11, 22], [5, 12, 22], [5, 13, 22], [5, 14, 22]],
        7: [[3, 5, 0], [6, 15, 0], [7, 10, 6],
            [5, 6, 0], [5, 7, 0], [5, 8, 0], [5, 9, 0], [5, 10, 0],
            [5, 11, 0], [5, 12, 0], [5, 13, 0], [5, 14, 0]],
        8: [[4, 5, 0], [6, 15, 0], [8, 10, 10]],
        9: [[30, 5, 0], [31, 5, 13], [6, 15, 0], [5, 6, 22], [5, 7, 22],
            [5, 8, 22], [5, 9, 22], [5, 10, 22], [5, 11, 22], [5, 12, 22],
            [5, 13, 22], [5, 14, 22], [33, 12, 17], [34, 11, 15],
            [251, 6, 15], [251, 7, 15], [252, 8, 15], [252, 9, 15], [252, 10, 15]]
        }

    #PROPS#

    props = {
        #object number: [room, y, x]
        50: [0, 0, 0], #fishing rod
        51: [1, 6, 8], #string
        52: [5, 14, 5], #stick
        53: [0, 0, 0], #shears
        54: [0, 0, 0], #fish
        55: [3, 9, 4], #key
        56: [2, 6, 17], #scout
        57: [0, 0, 0] #scout and his spaceship
        }

    RECIPES = [
        [51, 52, 50]
        ]

    #USE OBJECTS#

    def use_object(self):
        global room_map, item_carrying, selected_item, in_my_pockets
        global text_on_screen, letter_1, planet3_completed

        use_message = "You fiddle around with it but don't get anywhere."
        standard_responses = {
            100: "You read the letter you wrote to yourself."
            }

        item_player_is_on = get_item_under_player()
        for this_item in [item_player_is_on, item_carrying]:
            if this_item in standard_responses:
                use_message = standard_responses[this_item]

        if text_on_screen == True:
            use_message = "Please press Enter to continue."

        if item_player_is_on == 27 and item_carrying == 53:
            self.scenery[current_room].remove([25, 5, 0])
            self.scenery[current_room].remove([26, 5, 14])
            self.scenery[current_room].remove([27, 5, 9])
            self.scenery[current_room].append([28, 5, 0])
            self.scenery[current_room].append([29, 5, 14])
            use_message = "You cut away the twines to reveal a hidden path"
            sound('combine')

        elif item_player_is_on == 253 and item_carrying == 50:
            number = random.choice([1, 2, 3, 4])
            if number == 1:
                use_message = "You caught a fish!"
                add_object(54)
                sound('combine')
            else:
                use_message = "No fishes took the bait."

        elif item_player_is_on == 252 or item_player_is_on == 32:
            if item_carrying == 55:
                self.scenery[current_room].remove([32, 9, 0])
                self.scenery[current_room].remove([252, 6, 0])
                self.scenery[current_room].remove([252, 7, 0])
                self.scenery[current_room].remove([252, 8, 0])
                use_message = "You unlocked the fence!"
                sound('combine')

        elif item_player_is_on == 11 and item_carrying == 54: # river cat
            use_message = "You gave a fish to the cat."
            remove_object(54)
            self.river_cat_fish = True

        elif item_player_is_on in [9, 10] and item_carrying == 54: # jailer cat
            use_message = "You gave a fish to the jailer cats."
            remove_object(54)
            self.jailer_fish = True

        elif item_player_is_on == 33 and item_carrying == 54: # unfriendly cat
            if self.one_fish == False:
                self.no_fish = False
                self.one_fish = True
            else:
                self.two_fish = True

            use_message = "You gave a fish to the cats."
            show_text("", 1)
            remove_object(54)

        elif item_player_is_on == 8 and item_carrying == 56:
            use_message = "You placed Scout in his spaceship"
            self.scenery[current_room].remove([8, 10, 10])
            remove_object(56)
            add_object(57)
            sound('combine')

        elif item_player_is_on == 7 and item_carrying == 57:
            use_message = "You attached Scout's spaceship to your own"
            self.scenery[current_room].remove([7, 10, 6])
            self.scenery[current_room].append([35, 10, 6])     
            remove_object(57)
            sound('combine')

        elif item_player_is_on == 35: # Fixed spaceship
            use_message = "You're travelling back to Earth!"
            show_text("", 1)
            planet3_completed = True
            planet_3_to_earth()
        
        elif item_player_is_on == 100 or item_carrying == 100:
            if letter_1 == False and text_on_screen == False:
                self.scenery[current_room].append([102, 15, 0])
                letter_1 = True
                text_on_screen = True
        
        for recipe in self.RECIPES:
            ingredient1 = recipe[0]
            ingredient2 = recipe[1]
            combination = recipe[2]
            if (item_carrying == ingredient1
                and item_player_is_on == ingredient2) \
                or (item_carrying == ingredient2
                    and item_player_is_on == ingredient1):
                use_message = "You combine " + self.objects[ingredient1][3] \
                              + " and " + self.objects[ingredient2][3] \
                              + " to make " + self.objects[combination][3]
                if item_player_is_on in self.props.keys():
                    self.props[item_player_is_on][0] = 0
                    room_map[player_y][player_x] = self.get_floor_type()
                in_my_pockets.remove(item_carrying)
                add_object(combination)
                sound('combine')
                
        show_text(use_message, 0)

    def get_floor_type(self):
        return 0

    def can_drop(self, old_y, old_x):
        return room_map[old_y][old_x] in [0, 1]

    def speak(self):
        global speech_bubble, text_on_screen

        item_player_is_on = get_item_under_player()

        if item_player_is_on == 33: # unfriendly cats
            if speech_bubble == False:
                if self.no_fish:
                    show_text("The cats stare at you but don't say anything.", 1)
                    return
                elif self.two_fish:
                    self.speech_text = 94
                    add_object(53)
                    sound('combine')
                elif self.one_fish:
                    self.speech_text = 93

                self.scenery[current_room].append([90, 15, 0]) # speech bubble
                self.scenery[current_room].append([self.speech_text, 15, 2])
                speech_bubble = True
                text_on_screen = True

        if item_player_is_on == 11: # river cat
            if speech_bubble == False:
                if self.river_cat_fish:
                    self.speech_text = 92
                else:
                    self.speech_text = 91

                self.scenery[current_room].append([90, 15, 0]) # speech bubble
                self.scenery[current_room].append([self.speech_text, 15, 2])
                self.scenery[current_room].append([120, 14, 0])
                self.scenery[current_room].append([122, 14, 14])
                speech_bubble = True
                text_on_screen = True

        if item_player_is_on in [9, 10]: # jailers
            if speech_bubble == False:
                if self.jailer_fish: 
                    self.speech_text = 96
                else:
                    self.speech_text = 95

                self.scenery[current_room].append([90, 15, 0]) # speech bubble
                self.scenery[current_room].append([self.speech_text, 15, 2])
                self.scenery[current_room].append([121, 14, 0])
                speech_bubble = True
                text_on_screen = True
                    

    def close_textboxes(self):
        global speech_bubble, text_on_screen

        if current_room == 1:
            self.scenery[current_room].remove([120, 14, 0])
            self.scenery[current_room].remove([122, 14, 14])
        if current_room == 2:
            self.scenery[current_room].remove([121, 14, 0])
        
        pygame.time.delay(500)


#TEXT ON SCREEN#
text_on_screen = True # Start with True
help_menu = False
speech_bubble = True # Start with True
letter_1 = False
wall_of_achievements = False
achievement = 103

#GAME PROGRESS#
planet = planet1() # Start with planet1()
treehouse_destroyed = False
visited_centre = False
planet1_completed = False # Start with False
can_guess = True
correct_culprit = False
planet2_completed = False # Start with False
planet3_completed = False
game_over = False

#IN SPACE#
in_space_1to2 = False
in_space_2to3 = False
in_space_3 = False

#HANDLE OBJECTS#

in_my_pockets = [100, 38, 40, 45, 47]
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
    if item_player_is_on in planet.items_player_may_carry:
        room_map[player_y][player_x] = planet.get_floor_type()
        add_object(item_player_is_on)
        show_text("Now carrying " + planet.objects[item_player_is_on][3], 0)
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
    planet.props[item][0] = 0

def display_inventory():
    pygame.draw.rect(screen, BLACK, (0, 550, 690, 100))

    if len(in_my_pockets) == 0:
        return

    start_display = (selected_item // 14) * 14
    list_to_show = in_my_pockets[start_display : start_display + 14]
    selected_marker = selected_item % 14

    for item_counter in range(len(list_to_show)):
        item_number = list_to_show[item_counter]
        image = planet.objects[item_number][0]
        screen.blit(image, (25 + (46 * item_counter), 560))

    box_left = (selected_marker * 46) - 3
    pygame.draw.rect(screen, WHITE, (22 + box_left, 555, 40, 40), 3)
    item_highlighted = in_my_pockets[selected_item]
    description = planet.objects[item_highlighted][2]

    myfont = pygame.font.SysFont('Verdana', 20)
    textsurface = myfont.render(description, False, WHITE)

    screen.blit(textsurface,(20, 600))

def drop_object(old_y, old_x):
    global room_map
    
    if planet.can_drop(old_y, old_x):
        planet.props[item_carrying][0] = current_room
        planet.props[item_carrying][1] = old_y
        planet.props[item_carrying][2] = old_x
        room_map[old_y][old_x] = item_carrying
        show_text("You have dropped " + planet.objects[item_carrying][3], 0)
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
    global text_on_screen, speech_bubble, speech_text
    
    item_player_is_on = get_item_under_player()
    left_tile_of_item = find_object_start_x()
    
    if item_player_is_on in [0, 1, 2, 3]: #problem
        return
    
    description = "You see: " + planet.objects[item_player_is_on][2]
    for prop_number, details in planet.props.items():
        if (details[0] == current_room):
            if (details[1] == player_y
                and details[2] == left_tile_of_item
                and room_map[details[1]][details[2]] != prop_number):
                add_object(prop_number)
                description = "You found " + planet.objects[prop_number][3]
                sound('combine')
    
    show_text(description, 0)
    show_text("", 1)
    pygame.time.delay(500)

#MAKE MAP#

def generate_map():
    global room_map, top_left_x, top_left_y
    
    floor_type = planet.get_floor_type()
    
    room_data = planet.game_map[current_room]
    
    room_map = [[floor_type] * ROOM_WIDTH]
    
    for y in range(ROOM_HEIGHT):
        room_map.append([floor_type] * ROOM_WIDTH)

    if current_room in planet.scenery:
        for this_scenery in planet.scenery[current_room]: 
            scenery_number = this_scenery[0]
            scenery_y = this_scenery[1]
            scenery_x = this_scenery[2]
            room_map[scenery_y][scenery_x] = scenery_number

            image_here = planet.objects[scenery_number][0]
            image_width = image_here.get_width()
            image_width_in_tiles = int(image_width / TILE_SIZE)

            for tile_number in range(1, image_width_in_tiles):
                room_map[scenery_y][scenery_x + tile_number] = 255

    for prop_number, prop_info in planet.props.items():
        prop_room = prop_info[0]
        prop_y = prop_info[1]
        prop_x = prop_info[2]
        if (prop_room == current_room and
            planet.can_drop(prop_y, prop_x)): # Check for floor types
            room_map[prop_y][prop_x] = prop_number
            image_here = planet.objects[prop_number][0]
            image_width = image_here.get_width()
            image_width_in_tiles = int(image_width / TILE_SIZE)
            for tile_number in range(1, image_width_in_tiles):
                room_map[prop_y][prop_x + tile_number] = 255

def close_text_boxes():
    global text_on_screen, help_menu, wall_of_achievements, achievement
    global speech_bubble, letter_1
    global in_space_1to2, in_space_2to3, in_space_3
    
    if help_menu:
        planet.scenery[current_room].remove([101, 15, 0])
        show_text("", 0)
        help_menu = False
        text_on_screen = False
        
    elif speech_bubble:
        planet.scenery[current_room].remove([planet.speech_text, 15, 2])
        planet.scenery[current_room].remove([90, 15, 0]) # remove speech bubble
        speech_bubble = False
        text_on_screen = False

    elif letter_1:
        planet.scenery[current_room].remove([102, 15, 0])
        show_text("", 0)
        letter_1 = False
        text_on_screen = False

    elif wall_of_achievements:
        planet.scenery[current_room].remove([achievement, 15, 0])
        wall_of_achievements = False
        text_on_screen = False

    elif in_space_1to2: #Planet 1 to 2
        planet.scenery[current_room].remove([240, 15, 0])
        show_text("You have arrived on a new planet!", 0)
        show_text("", 1)
        in_space_1to2 = False
        text_on_screen = True
        speech_bubble = True

    elif in_space_2to3: #Planet 2 to 3
        planet.scenery[current_room].remove([241, 15, 0])
        show_text("You have arrived on a new planet!", 0)
        show_text("", 1)
        in_space_2to3 = False
        text_on_screen = False
        speech_bubble = False

    elif in_space_3: #Planet 3 to Earth
        planet.scenery[current_room].remove([242, 15, 0])
        show_text("Well done! You have arrived on Earth!", 0)
        show_text("Press [A] to view your wall of achievements!", 1)
        in_space_3 = False
        text_on_screen = False
        speech_bubble = False

    planet.close_textboxes()

    pygame.time.delay(500)

#GAME LOOP#
                
def start_room():
    show_text("You are here: " + planet.game_map[current_room][0], 0)
    show_text("", 1)

def game_loop():
    global player_x, player_y, current_room
    global from_player_x, from_player_y
    global player_image, player_image_shadow 
    global selected_item, item_carrying
    global player_offset_x, player_offset_y
    global player_frame, player_direction
    global help_menu, speech_bubble, letter_1
    global text_on_screen, wall_of_achievements, achievement
    global can_guess, correct_culprit
    global in_space_1to2, in_space_3
    
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
        if text_on_screen:
            close_text_boxes()
        current_room += 1
        generate_map()
        player_x = 0
        player_y = int(ROOM_HEIGHT / 2)
        player_frame = 0
        start_room()
        return

    if player_x == -1: #goes through door on the left
        if text_on_screen:
            close_text_boxes()
        current_room -= 1
        generate_map()
        player_x = ROOM_WIDTH - 1
        player_y = int(ROOM_HEIGHT / 2)
        player_frame = 0
        start_room()
        return

    if player_y == ROOM_HEIGHT: #goes through door at the bottom
        if text_on_screen:
            close_text_boxes()
        current_room += planet.map_width
        generate_map()
        player_y = 0
        player_x = int(ROOM_WIDTH / 2)
        player_frame = 0
        start_room()
        return
    
    if player_y == -1: #goes through door at the top
        if text_on_screen:
            close_text_boxes()
        current_room -= planet.map_width
        generate_map()
        player_y = ROOM_HEIGHT - 1
        player_x = int(ROOM_WIDTH / 2)
        start_room()
        return

    if keys[pygame.K_g]:
        pick_up_object()

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

    if keys[pygame.K_d] and item_carrying:
        drop_object(old_player_y, old_player_x)

    if keys[pygame.K_SPACE]:
        examine_object()
        planet.speak()

    if keys[pygame.K_u]:
        planet.use_object()
        pygame.time.delay(300)

    if keys[pygame.K_h]:
        if text_on_screen == False:
            planet.scenery[current_room].append([101, 15, 0])
            help_menu = True
            text_on_screen = True
            show_text("Help Menu", 0)
        elif text_on_screen:
            show_text("Please press Enter to continue.", 0)

    if keys[pygame.K_a]:
        if text_on_screen == False:
            if planet1_completed:
                if treehouse_destroyed == False:
                    achievement = 104
            if planet2_completed == True:
                if correct_culprit:
                    if treehouse_destroyed:
                        achievement = 105
                    else:
                        achievement = 106
            if planet3_completed == True:
                if correct_culprit:
                    if treehouse_destroyed:
                        achievement = 109
                    else:
                        achievement = 107                        
                else:
                    if treehouse_destroyed:
                        achievement = 110
                    else:
                        achievement = 108
            planet.scenery[current_room].append([achievement, 15, 0])
            wall_of_achievements = True
            text_on_screen = True
        else:
            show_text("Please press Enter to continue.", 0)

    if keys[pygame.K_1] or keys[pygame.K_3]:
        if visited_centre:
            planet.scenery[current_room].remove([planet.speech_text, 15, 2])
            planet.scenery[current_room].append([95, 15, 2])
            speech_bubble = True
            planet.speech_text = 95
            text_on_screen = True
            can_guess = False

    if keys[pygame.K_2]:
        if visited_centre:
            planet.scenery[current_room].remove([planet.speech_text, 15, 2])
            planet.scenery[current_room].append([96, 15, 2])
            speech_bubble = True
            planet.speech_text = 96
            text_on_screen = True
            can_guess = False
            correct_culprit = True

    if keys[pygame.K_RETURN]:
        close_text_boxes()

    #TELEPORTER
    if keys[pygame.K_x]:
        current_room = int(input("Enter room number:"))
        player_x = 10
        player_y = 10
        generate_map()
        start_room()

    if in_space_1to2:
        player_x = 6
        player_y = 11
    elif in_space_2to3:
        player_x = 7
        player_y = 11
    elif in_space_3:
        player_x = 9
        player_y = 10
        player_direction = "down"
    elif room_map[player_y][player_x] not in planet.items_player_may_stand_on:
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

    floor_type = planet.get_floor_type()

    for y in range(ROOM_HEIGHT):
        for x in range(ROOM_WIDTH):
            draw_image(planet.objects[floor_type][0], y, x)
            if room_map[y][x] in planet.items_player_may_stand_on:
                draw_image(planet.objects[room_map[y][x]][0], y, x)

    for y in range(ROOM_HEIGHT):
        for x in range(ROOM_WIDTH):
            item_here = room_map[y][x]
            # Player cannot walk on 255: it marks spaces used by wide objects.
            if item_here not in planet.items_player_may_stand_on + [255]:
                image = planet.objects[item_here][0]
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

def planet_1_to_2():
    global in_space_1to2, text_on_screen, planet, current_room
    global in_my_pockets, selected_item
    
    planet = planet2()
    current_room = 9
    selected_item = 0
    in_my_pockets = [100, 69]
    item_highlighted = 0
    planet.scenery[current_room].append([240, 15, 0])
    show_text("Press enter to continue your journey~", 1)
    in_space_1to2 = True
    text_on_screen = True

def planet_2_to_3():
    global in_space_2to3, text_on_screen, planet, current_room
    global in_my_pockets, selected_item
    
    planet = planet3()
    current_room = 7
    selected_item = 0
    in_my_pockets = [100, 57]
    item_highlighted = 0
    planet.scenery[current_room].append([241, 15, 0])
    show_text("Press enter to continue your journey~", 1)
    in_space_2to3 = True
    text_on_screen = True

def planet_3_to_earth():
    global in_space_3, text_on_screen, planet, current_room
    global in_my_pockets, selected_item
    
    planet = earth()
    current_room = 0
    selected_item = 0
    in_my_pockets = [100]
    item_highlighted = 0
    planet.scenery[current_room].append([242, 15, 0])
    show_text("Press enter to continue your journey~", 1)
    in_space_3 = True
    text_on_screen = True
    

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
