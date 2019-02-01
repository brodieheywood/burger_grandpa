# Brodie Heywood
# November 18, 2018

"""Burger Grandpa v2.2"""
# TODO: finish commenting functions
# TODO: add/remove functions from player class

import json
import random
import time


def title_screen():
    """Display Burger Grandpa title screen.

    Tell user to "hit enter to coninue."
    PARAM: None
    POSTCONDITION: prints Burger Grandpa title screen
    RETURN: None
    """
    print("""
                ,-----.
              W/,-. ,-.\W
              ()>a   a<()
              (.--(_)--.)      
            ,'/.-'\\\U0001F5E2/`-.\`.    \x1b[1m𝔅𝔯𝔬𝔡𝔦𝔢 ℌ𝔢\x1b[0m𝔂\x1b[1m𝔴𝔬𝔬𝔡'𝔰\x1b[0m     
          ,' /    `-'    \ `.     ______                                   _____                        _             
         /   \           /   \\   (____  \                                /  ____)                      | |            
        /     `.       ,'     \\   ____)  )_   _  ____ ____ _____  ____   | |  ___  ____ _____ ____   __| |____  _____ 
       /    /   `-._.-'   \    \\ |  __  (| | | |/ ___) _  | ___ |/ ___)  | | (_  |/ ___|____ |  _ \ / _  |  _ \(____ |
     ,-`-._/|     |=|o    |\_.-< | |__)  ) |_| | |  ( (_| | ____| |      | |___) | |   / ___ | | | ( (_| | |_| / ___ |
    <,--.)  |_____| |o____|  )_ \\|______/|____/|_|   \___ |_____)_|       \_____/|_|   \_____|_| |_|\____|  __/\_____|
     `-)|    |//   _   \\\|     )/                   (_____|                                              |_|   
       ||    |'    |    `|         
       ||    |     |     |           .---'--.        .-'----.        .-----'.        .---'--.        .--'---.
       ||    (    )|(    )          /' .  '. \\      /. ' . ' \\      /' ' . ' \\      /. ' ' . \\      /' . . ' \\
       ||    |     |     |         (`-..:...-')    (`-....:.-')    (`-.:....-')    (`-.....:-')    (`-...:..-')
       ||    |     |     |          ;-......-;      ;-......-;      ;-......-;      ;-......-;      ;-......-; 
       ||    |_.--.|.--._|           '------'        '------'        '------'        '------'        '------'
       ||     /'""| |""`\\
       []     `===' `==='                                   \U0001F354  HIT \x1b[1mENTER\x1b[0m TO START  \U0001F354
    """)
    # ASCII Grandpa http://www.ascii-art.de/ascii/
    # "\U0001F5E2" - Unicode lips. "\U0001F354" - Unicode hamburger.
    # Triple quotes encapsulate ASCII art to preserve formatting.
    return enter_to_continue()


def introduction():
    """Display introduction.

    Explain game mechanics.
    PARAM: None
    POSTCONDITION: prints introduction text with one second pauses
    RETURN: None
    """
    print('You are the Burger Grandpa. It\'s your job to feed your hungry neighbours.\n')
    time.sleep(1)  # Used throughout program. Pauses program for given number of seconds.
    print('Your neighbours are wandering around the neighbourhood, starving. Find them and feed them hamburgers until '
          'their \nHP (\x1b[31mHunger Points\x1b[0m) reaches 0. Be careful, if Burger Grandpa drops all of his burgers '
          'and his HP (\x1b[32mHamburger Patties\x1b[0m) \nreaches 0, it\'s GAME OVER. Feed all three of your '
          'neighbours to win!\n')
    time.sleep(1)
    print('Good luck, Burger Grandpa...\n\n')


def map_display(coordinates):
    """Display world map showing location of player.

    PARAM: coordinates, a set of two positive integers that represents player's coordinates on a 5x5 grid (map)
    PRECONDITION: coordinates must be a set containing two positive integers between 1 and 5, inclusive
    POSTCONDITION: Draws a 5x5 grid. Grid has coordinates inside each cell. Where player coordinates match cell
    coordinates, coordinates are replaced with "GRANDPA."
    RETURN: None
    """
    display_map_name()

    # define character's current coordinates (will be replaced by "GRANDPA" inside map cell).
    to_be_replaced = ' (' + str(coordinates[0]) + ',' + str(coordinates[1]) + ') '

    horizontal_cell_border = (("|" + ("-" * 9)) * 5) + "|"
    vertical_cell_border = (("|" + (" " * 9)) * 5) + "|"

    for row in range(5, 0, -1):  # y-axis labels
        print(horizontal_cell_border)
        print(vertical_cell_border)
        for column in range(1, 6):  # x-axis labels
            coordinates_str = "|  (" + str(column) + "," + str(row) + ")" + (" " * 2)
            print(coordinates_str.replace(to_be_replaced, '\x1b[35mGRANDPA\x1b[0m'), end="")  # coordinates replaced
        print("|")
        print(vertical_cell_border)
    print(horizontal_cell_border)


def display_map_name():
    """Display map name.

    PARAM: None
    PRECONDITION: None
    POSTCONDITION: print title above game map to indicate what map represents
    RETURN: None
    """
    print('\n\nMap of the Neighbourhood')


def get_lot_type(coordinates):
    """Return place name assigned to coordinate point on map.

    PARAM: coordinates, a set of two positive integers that represents player's coordinates on a 5x5 grid (map)
    PRECONDITION: coordinates must be a set containing two positive integers between 1 and 5
    POSTCONDITION: return a two to three word string that briefly describes the given coordinate with a place name
    RETURN: key, a string stating the user-displayed name of the coordinate point
    """
    # first, convert character's coordinates to string that is readable by dictionary lookup functions.
    coordinate_str = convert_to_coordinate_string(coordinates[0], coordinates[1])
    lot_info = get_lot_info_dict()

    # then look up lot type (key) using coordinates string (coordinates found in level two values in dictionary)
    for key, value in lot_info.items():
        for key_2, value_2 in value.items():
            if coordinate_str in value_2:
                return key


def get_lot_info(lot_type, request):
    """Return specific information about a coordinate point on the game map.

    Access a dictionary using coordinate point's lot type as the key. Can access information stored in lot type
    dictionary's values: coordinates, description, and boundary.
    PARAM: lot_type, a two to three word string assigned to a coordinate point that briefly describes the given
           coordinate with a place name; lot_types are the keys of the first level dictionary in the lot_info_dict
           dictionary
           request, information that is requested of lot type; a one-word string that matches the first level values (or
           second level keys) in the lot_info_dict dictionary
    PRECONDITION: lot type and request must be strings
    POSTCONDITION: return string used to query dictionary
    RETURN: requested information about a coordinate point as a string
    """
    lot_info = get_lot_info_dict()
    return lot_info[lot_type][request]


def get_lot_info_dict():
    """Dictionary containing coordinate information.

    The dictionary contains keys (as strings) for each lot type found in the game. The lot types are represented by
    coordinates in the world map. Most lot types have more than one associated coordinate.
    The keys contain nested dictionaries, each with the following keys:
    - coordinates: a list containing strings of 1 to 5 coordinate points
    - description: a one-line string describing the lot type
    - boundary: another one-line string describing the "boundary" of the lot; enhances game immersion (player movement
    is bounded by edge of map)
    PARAM: None
    PRECONDITION: None
    POSTCONDITION: return a two-level dictionary containing coordinate/lot type information
    RETURN: a dictionary containing strings for keys and values
    """
    lot_info_dict = {
        'an alleyway': {
            'coordinates': ['2,2', '3,2', '2,3'],
            'description': 'There\'s not a lot going on here.',
            'boundary': ''
        },
        'the creek': {
            'coordinates': ['5,4'],
            'description': 'Now he\'s all muddy.',
            'boundary': 'There is a steep, muddy embankment'
        },
        'the empty lot': {
            'coordinates': ['5,2'],
            'description': 'This lot has been abandoned for years.',
            'boundary': 'There are untamed brambles'
        },
        'Burger Grandpa\'s house': {
            'coordinates': ['3,3'],
            'description': 'It\'s cozy and lived-in.',
            'boundary': ''
        },
        'his neighbour\'s house': {
            'coordinates': ['3,1', '5,1', '1,3', '5,3'],
            'description': 'He\'s looking through all of their drawers like a snoop.',
            'boundary': 'There is a tall fence'
        },
        'the park': {
            'coordinates': ['1,1', '2,1', '1,2'],
            'description': 'It\'s an L-shaped, grassy area with wooden benches set along the edge.',
            'boundary': 'There are beautiful, but thorny, rose bushes'
        },
        'the pond': {
            'coordinates': ['4,5', '5,5'],
            'description': 'It\'s really cold in there. Burger Grandpa is shivering.',
            'boundary': 'The water is too deep'
        },
        'the road': {
            'coordinates': ['4,2', '4,3', '2,4', '3,4', '4,4'],
            'description': 'The streets are nice and calm in his neighbourhood.',
            'boundary': ''
        },
        'an intersection': {
            'coordinates': ['4,1', '1,4'],
            'description': 'It connects his neighbourhood to the highway. Watch out for cars, you old rapscallion!',
            'boundary': 'Burger Grandpa refuses to cross the pedestrian-unfriendly highway'
        },
        'the woods': {
            'coordinates': ['1,5', '2,5', '3,5'],
            'description': 'It\'s really spooky, like the woods in Snow White. Burger Grandpa is super scared.',
            'boundary': 'There\'s thick, even spookier woods (that Burger Grandpa wouldn\'t dare enter)'
        }
    }
    return lot_info_dict


def convert_to_coordinate_string(x, y):
    """Convert coordinates to a string.

    Used to search dictionary values for coordinates.
    PARAM: x and y are integer coordinate points
    PRECONDITION: x and y must be integers
    POSTCONDITION: convert integers to a string in coordinate format
    RETURN: coordinates in a correctly formatted string
    """
    coordinate_str = str(x) + ',' + str(y)
    return coordinate_str


def enter_to_continue():
    """Return empty input field to slow down text.

    Should be paired with text that prompts user to "hit enter".
    PARAM: None
    PRECONDITION: None
    POSTCONDITION: slows down text output to user with empty input that requires user to press enter
    RETURN: empty input field requiring user to hit enter
    """
    return input()


def invalid_selection():
    """Display message indicating user input was invalid.

    Should only be used before user-input field.
    PARAM: None
    PRECONDITION: None
    POSTCONDITION: notifies user of incorrect entry and asks user to retry with new input
    RETURN: None
    """
    print('\nInvalid entry. Please choose again.')


def thank_you():
    """Display message thanking user for playing.

     PARAM: None
     PRECONDITION: None
     POSTCONDITION: prints string thanking user for playing Burger Grandpa
     RETURN: None
     """
    print('\nThanks for playing Burger Grandpa!')


def roll_die(number_of_rolls, number_of_sides):
    """Return the sum of simulated die rolls.

    Useful as a random number generator.
    PARAM: number_of_rolls, simulated number of die rolls; a positive integer
    number_of_sides, number of sides on simulated die; must be a positive integer
    PRECONDITION: number_of_rolls and number_of_sides must be positive integers
    POSTCONDITION: returns a random positive integer between the two parameters, where number_of_rolls was the minimum
    and number_of_sides was the maximum range
    RETURNS: random positive integer
    >>> roll_die(-3, 4)
    number_of_rolls and number_of_sides must be positive integers.
    >>> roll_die(3, -4)
    number_of_rolls and number_of_sides must be positive integers.
    >>> roll_die(-3, -4)
    number_of_rolls and number_of_sides must be positive integers.
    >>> roll_die(0, 4)
    number_of_rolls and number_of_sides must be positive integers.
    >>> roll_die(3, 0)
    number_of_rolls and number_of_sides must be positive integers.
    >>> roll_die(0, 0)
    number_of_rolls and number_of_sides must be positive integers.
    """
    if (number_of_rolls > 0) and (number_of_sides > 0):
        return random.randint(number_of_rolls, number_of_rolls * number_of_sides)


def find_unavailable_moves(coordinates):
    """Find unavailable player moves based on coordinate.

    Determines if player has reached the boundary of the play area.
    PARAM: coordinates, a set containing two positive integers that represent player character's position on game map
    (index 0 is x-coordinate, index 1 is y-coordinate)
    PRECONDITION: coordinates must be a set containing two positive integers between 1 and 5
    POSTCONDITION: returns list of moves unavailable to player
    RETURN: list containing 0 to 2 strings where string is a cardinal direction
    """
    unavailable_directions = list()
    x = coordinates[0]
    y = coordinates[1]

    if (y - 1) < 1:
        unavailable_directions.append('south')
    if (y + 1) > 5:
        unavailable_directions.append('north')
    if (x + 1) > 5:
        unavailable_directions.append('east')
    if (x - 1) < 1:
        unavailable_directions.append('west')

    return unavailable_directions


def game_over(player):
    """Display game over message.

    PARAM: player, an object in a class with a .name attribute that holds a string
    PRECONDITION: player must be an initialized object in a class containing a .name attribute that holds a string
    POSTCONDITION: prints game over text and to user
    RETURN: None
    """
    print('\n\nOh no! Burger Grandpa', player.name, 'is out of Hamburger Patties, but there are still more neighbours '
                                                    'to feed!\nHe\'ll have to go home to cook up some more; but maybe '
                                                    'he\'ll just have a quick nap first...\n')
    time.sleep(2)
    game_over_screen()
    time.sleep(1)
    Character.display_score(player)
    time.sleep(3)
    restart_game()


def game_over_screen():
    """Display game over screen.

    PARAM: None
    PRECONDITION: None
    POSTCONDITION: display "GAME OVER" ASCII to user
    RETURN: None
    """
    print("""\x1b[31m\x1b[1m
    *****************************************
    *************** GAME OVER ***************
    *****************************************
    \x1b[0m\n""")  # triple quotes used for ease of formatting; colour is set to red


def restart_game():
    """Prompt user to restart or quit game.

     PARAM: None
     PRECONDITION: None
     POSTCONDITION: asks for user input to restart or quit game, returns itself if entry is invalid
     RETURN: None
     """
    play_again = input('Would you like to play again? [Y/N] ').lower()
    if play_again == 'y':
        print('\nBurger Grandpa is getting up, just give him a couple of seconds...\n\n')
        time.sleep(3)
        return main()
    elif play_again == 'n' or 'quit':
        thank_you()
        quit()
    else:
        invalid_selection()
        restart_game()


def interaction_chance():
    """Determine if an interaction will occur during turn.

    PARAM: None
    PRECONDITION: None
    POSTCONDITION: if random number chosen by roll_die function is equal to four, notifies user that interaction will
    occur. Returns True, allowing main function to call next appropriate function.
    RETURN: Boolean True if interaction will occur
    """
    if roll_die(1, 10) == 4:  # 10% chance
        print('\n\n!!! A HUNGRY NEIGHBOUR APPEARS !!!\n\n')
        return True  # continue in main()
    else:
        return  # next function in main()


def get_interaction_choice(player):
    """Ask for user input to enter into interaction (or not).

    PARAM: player, an object in a class with a display_hp function contained within
    PRECONDITION: player must be an initialized object in a class with a display_hp function contained within its class
    POSTCONDITION: returns True, allowing main function to call next appropriate function.
    RETURN: True Boolean if user chooses 'y'
    """
    player.display_hp()
    interaction_choice = (input('Feed the hungry neighbour? [Y/N] ')).lower()
    if interaction_choice == 'y':
        return True  # proceed to next function in main (interaction sequence, aka 'attack')
    elif interaction_choice == 'n':
        run(player)
    elif interaction_choice == 'quit':
        Character.save_profile(player)
    else:
        invalid_selection()
        get_interaction_choice(player)


def run(player):
    """Display run message to user.

    PARAM: player, an object in a class with a .name attribute that holds a string
    PRECONDITION: player must be an initialized object in a class containing a .name attribute that holds a string
    POSTCONDITION: displays message to user indicating that the character ran away
    RETURN: None
    """
    print('\nThat neighbour was freaking Burger Grandpa out. Burger Grandpa', player.name, 'ran away!')
    time.sleep(1)
    check_for_damage(player)


def check_for_damage(player):
    """Determine if player will be damaged from running away from interaction.

    PARAM: player, an object in a class with a .hp attribute that holds an integer
    PRECONDITION: player must be an initialized object in a class containing a .hp attribute that holds an integer
    POSTCONDITION: chooses random number to determine if user will be damaged from declining interaction
    RETURN: None
    """
    damage_chance = roll_die(1, 10)
    if damage_chance == 4:  # 10% chance
        run_damage(player)
        return
    else:
        return


def run_damage(player):
    """Apply damage to user from declining interaction.

    PARAM: player, an object in a class with a .hp attribute that holds an integer
    PRECONDITION: player must be an initialized object in a class containing a .hp attribute that holds an integer
    POSTCONDITION: subtract random amount between 1 to 4 from player's hp
    RETURN: None
    """
    damage = roll_die(1, 4)  # number from 1 to 4
    player.hp -= damage
    print('Burger Grandpa dropped', damage, 'patties.')
    time.sleep(1)


def interaction_sequence(player, npc):
    """Run interaction between player and non-player character until the HP of one party reaches zero.

    Actions will decrement each player's hp.
    PARAM: player, an object in a class with a .hp attribute that holds an integer
    npc, an object in a different class from player parameter with a .hp attribute that holds an integer
    PRECONDITION: player and npc must be initialized objects in a class containing a .hp attribute that holds an integer
    POSTCONDITION: sequence of functions will reduce hp of each party until one party's .hp attribute reaches zero. If
    the player reaches zero, game_over function will be called. If npc reaches zero, player wins the interaction and
    battle_win function will be called.
    RETURN: None
    """
    while npc.hp and player.hp > 0:
        display_hp_for_battle(player, npc)  # displays hp of each participant
        Character.burger_attack(player, npc)  # player attack
        if npc.hp > 0:  # opponents turn to attack
            time.sleep(1)
            display_hp_for_battle(player, npc)
            enemy_attack(player)  # opponent attack
            if player.hp > 0:
                continue
            else:
                game_over(player)
        else:
            interaction_win(player)
            return


def decrement_by(class_with_total, amount):
    """Apply damage to defending opponent.

    PARAM: class_with_total, a class with a .hp attribute
    amount, what will be subtracted from the class' .hp attribute
    PRECONDITION: class_with_total must be a class with a .hp attribute that holds an integer
    amount must be a positive integer
    POSTCONDITION: decrement classes .hp attribute by amount given
    RETURN: None
    """
    class_with_total.hp -= amount
    return


def display_hp_for_battle(player, npc):
    """Display HP with icons in a battle-friendly format.

    PARAM: player, an object in a class with a .hp attribute that holds an integer
    npc, an object in a different class from player parameter with a .hp attribute that holds an integer
    PRECONDITION: player must be a class with a .hp attribute that holds an integer
    amount, must be a positive integer
    POSTCONDITION: decrement classes .hp attribute by amount given
    RETURN: None
    """
    print('\n\n\x1b[32mBurger Grandpa HP:', '\x1b[33m\U0001F354\x1b[0m' * player.hp, '\x1b[32m(' + str(player.hp) +
          '/10)\x1b[0m')
    print('\x1b[31mNeighbour HP:', '\U0001F374' * npc.hp, '(' + str(npc.hp) + '/10)\x1b[0m\n')
    time.sleep(1)
    return


def enemy_attack(defender):
    """Simulate enemy attack.

    PARAM: defender, an object in a class with a .hp attribute that holds an integer
    PRECONDITION: defender must be a class with a .hp attribute that is a positive integer
    POSTCONDITION: decrement defenders' .hp attribute by amount given
    RETURN: None
    """
    print('\nThe neighbour is still hungry! Hit ENTER to see what happens.', end='')
    enter_to_continue()
    print('\n"I ASKED FOR NO PICKLES!"')
    time.sleep(1)
    damage = roll_die(1, 6)
    decrement_by(defender, damage)
    print('Burger Grandpa got startled and dropped', str(damage), 'Hamburger Patties.')
    time.sleep(1)
    return


def interaction_win(player):
    """Display message to user indicating that interaction was won.

    PARAM: player, an object in a class with a .score attribute that holds an integer
    PRECONDITION: player must be in a class, their class must have a .score attribute that contains an integer
    POSTCONDITION: display message to user indicating that interaction was won
    RETURN: None
    """
    print('\n\nThe neighbour has no more Hunger Points. The neighbour is full!')
    print('"Thank you Burger Grandpa!"\n\n')
    increment_score(player)
    Character.display_score(player)
    return return_to_map()


def increment_score(player):
    """Increment score attribute by one.

    PARAM: player, an object in a class with a .score attribute that holds an integer
    PRECONDITION: player must be in a class, their class must have a .score attribute that contains an integer
    POSTCONDITION: .score of player is incremented by one
    RETURN: None
    """
    player.score += 1
    return


def return_to_map():
    """Prompt user to hit enter to return to map view.

    PARAM: None
    PRECONDITION: None
    POSTCONDITION: prompts user to hit enter, continuing with main function (and starting the next move cycle)
    RETURN: None
    """
    print('Hit ENTER to find some more neighbours to feed.', end='')
    enter_to_continue()
    return  # continues with main function


def game_win(player):
    """Display to user that they have won the game.

    PARAM: player, an object in a class with a .name attribute that holds a string
    PRECONDITION: player must be in a class with a .name attribute. .name must hold a string.
    POSTCONDITION: displays game-winning message to the user
    RETURN: None
    """
    print('\n\n\x1b[34mYou fed all of your hungry neighbours! Good job', player.name,
          '!\nHere\'s a burger for yourself:\x1b[0m\n\n', ' ' * 15,
          ' \x1b[33m\U0001F354\x1b[0m\n\n\x1b[34mToo bad it\'s '
          'not real!\x1b[0m\n\n')
    print('Now Burger Grandpa can go home for a nap.')
    restart_game()


class Character:
    """Simulate a simple character that can move and attack."""

    def __init__(self, name, hp, x, y, score):
        """Initialize name, health points (hp), and coordinates attributes.

        PARAM: name, name of character
        hp, Hamburger Patties of character (functions like HP in Dungeons and Dragons)
        x, x-coordinate of player on map
        y, x-coordinate of player on map
        score, number of neighbours fed.
        PRECONDITION: name, must be string
        hp, must be postive integer
        x, must be positive integer
        y, must be positive integer
        score, must be positive integer
        POSTCONDITION: initializes attributes of class instance
        RETURN: None
        """
        self.name = name
        self.hp = hp
        self.coordinates = x, y
        self.score = score

    def get_hp(self):
        """character hp

        PARAM: None
        PRECONDITION: None
        POSTCONDITION: return hp of class
        RETURN: hp of class
        """
        return self.hp

    def increment_hp(self):
        """increment hp

        PARAM: None
        PRECONDITION: None
        POSTCONDITION: increment hp
        RETURN: incremented hp
        """
        if self.hp < 10:
            self.hp += 1
            return
        else:
            return

    def burger_attack(self, neighbour):
        """Simulate character attack.

        PARAM: neighbour, enemy
        PRECONDITION: neighbour must be a class that contains .hp attribute that is an integer
        POSTCONDITION: decrements neighbour hp by amount of player attack.
        RETURN: None
        """
        print('\nHit ENTER to feed the hungry neighbour some burgers.\n' + '-' * 52, end='')
        enter_to_continue()
        damage = roll_die(1, 6)
        decrement_by(neighbour, damage)
        print('Burger Grandpa', self.name, 'feeds the neighbour', str(damage), 'burgers.')
        return

    def new_turn(self):
        """Start new turn."""
        map_display(self.coordinates)
        self.display_character_info()
        self.display_location_info()
        self.display_surrounding_coordinates()
        self.move()

    def display_character_info(self):
        """Display character info"""
        self.display_coordinates()
        self.display_hp()
        self.display_score()

    def display_coordinates(self):
        """Get character coordinates.

        PARAM: coordinates, a set containing x-coordinate and y-coordinate
        PRECONDITION: coordinates must be a set
        POSTCONDITION: print string
        RETURN: None
        """
        print('Current location:', '(' + str(self.coordinates[0]) + ',', str(self.coordinates[1]) + ')')

    def display_hp(self):
        """Display player HP."""
        print('Burger Grandpa', self.name + '\'s HP:', str(self.hp))

    def display_score(self):
        """Display player score."""
        print('Neighbours fed:', str(self.score) + '/3', end='\n\n')

    def display_location_info(self):
        """Display character location."""
        lot_type = get_lot_type(self.coordinates)
        description = get_lot_info(lot_type, 'description')
        boundary = get_lot_info(lot_type, 'boundary')
        boundary_direction = self.location_boundaries_display()

        print('Burger Grandpa', self.name, 'is in', lot_type + '.', description)
        if boundary != '':
            print(boundary, boundary_direction)
        else:
            return

    def location_boundaries_display(self):
        """Display boundary."""
        boundary_directions = find_unavailable_moves(self.coordinates)
        if len(boundary_directions) == 2:
            return 'to the ' + boundary_directions[0].title() + ' and ' + boundary_directions[1].title() + '.'
        elif len(boundary_directions) == 1:
            return 'to the ' + boundary_directions[0].title() + '.'
        else:
            return

    def display_surrounding_coordinates(self):
        """Display coordinates around player."""
        directions = ['north', 'east', 'south', 'west']
        print('\n', end='')
        for direction in directions:
            if self.check_move_possibility(direction) is True:
                print('To the', direction.title(), 'is',
                      get_lot_type(self.get_new_coordinates(direction)) + '.')
        print('')

    def move(self):
        """Move character."""
        self.coordinates = self.select_move_direction()

    def select_move_direction(self):
        """Select movement direction."""
        direction_choice = input('Enter a direction to move in: ').lower()
        directions = ['north', 'east', 'south', 'west']

        if (direction_choice in directions) and self.check_move_possibility(direction_choice) is True:
            return self.get_new_coordinates(direction_choice)
        elif direction_choice == 'quit':
            self.save_profile()
        else:
            invalid_selection()
            return self.select_move_direction()

    def check_move_possibility(self, selected_direction):
        """Check if move within boundary."""
        unavailable_directions = (find_unavailable_moves(self.coordinates))
        if selected_direction not in unavailable_directions:
            return True
        else:
            return False

    def get_new_coordinates(self, direction_choice):
        """Get new coordinates."""
        x = self.coordinates[0]
        y = self.coordinates[1]
        if direction_choice == 'north':
            y += 1
        elif direction_choice == 'east':
            x += 1
        elif direction_choice == 'south':
            y -= 1
        elif direction_choice == 'west':
            x -= 1
        return x, y

    def create_profile(self):
        """Create profile."""
        new_profile = {
            'Name': self.name,
            'HP': self.hp,
            'Neighbours Fed': self.score,
            'Coordinates': self.coordinates
        }
        return new_profile

    def save_profile(self):
        """Save profile."""
        saved_profile = (self.create_profile())
        file_name = self.name + '.json'
        with open(file_name, 'w') as profile_json_file:
            json.dump(saved_profile, profile_json_file)
        print('*Profile Saved: ' + self.name.title() + '*')
        thank_you()
        time.sleep(1)
        return quit()


class Neighbour:
    """Simulate a neighbour that can attack."""

    def __init__(self, hp):
        """Initialize health points (hp)."""
        self.hp = hp


def main():
    title_screen()
    introduction()
    main_character = Character(input('What is your name? ').title(), 10, 3, 4, 0)
    while main_character.score < 3:  # endgame condition
        main_character.new_turn()
        start_battle = interaction_chance()  # check 10% chance of 'battle' starting
        if start_battle is True:
            feed_or_run = get_interaction_choice(main_character)
            if feed_or_run is True:  # if player chooses to feed neighbour
                enemy = Neighbour(10)  # initialize an enemy
                interaction_sequence(main_character, enemy)  # 'battle' sequence
                continue
            else:
                continue
        else:
            main_character.increment_hp()  # increase HP by one every time player moves without encountering enemy
            continue
    game_win(main_character)


if __name__ == '__main__':
    main()
