# Brodie Heywood
# A01058795
# October 10, 2018

"""COMP1510 Lab 5: More about if statements, and lists"""
# Due: Sunday 10PM

import doctest
import random


# Global variables: character_class, opponent_one, opponent_two
character_class = ''


def user_messages(message):
    if message == 'introduction':
        print('"Who goes there?"')
        print('(Enter HELP for a list of characters)')
    elif message == 'opponent_select':
        print('\n\n\nLet\'s see who you\'re up against. It looks like it\'s...')
    elif message == 'get_ready':
        print('\n\n\n"Ready to fight?"')
        print('"Okay, fight!"' + input('Press ENTER') + '\n\n')
    elif message == 'roll_for_first':
        print('Rolling to see who goes first...')


def generate_name(syllables):
    name = ""
    for i in range(1, syllables + 1):
        name = name + generate_syllable()
    return name.title()


def generate_vowel():
    i = random.choice([101, 105, 111, 117, 121])  # decimal values for Unicode lowercase Latin alphabet vowels
    return chr(i)  # chr() method accesses unicode character set


def generate_consonant():
    i = random.choice(range(98, 123))  # decimal value for Unicode lowercase Latin alphabet ('b' to 'z')
    if i not in [101, 105, 111, 117, 121]:  # exclude Unicode vowels
        return chr(i)
    else:
        return generate_consonant()


def generate_syllable():
    syllable = generate_consonant() + generate_vowel()
    return syllable


def roll_die(number_of_rolls, number_of_sides):
    """Return the sum of simulated die rolls.

    PRECONDITION: number_of_rolls and number_of_sides are not strings or floats.
    POSTCONDITION: Returned a positive integer or printed a message and returned nothing.

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
        return str(random.randint(number_of_rolls, number_of_rolls * number_of_sides))
    else:
        print('number_of_rolls and number_of_sides must be positive integers.')
        return


def generate_character():
    global character_class
    # generate character name:
    character = [generate_name(3)]
    # generate character attributes:
    strength = ['Strength: ' + roll_die(3, 6)]
    character.extend(strength)
    intelligence = ['Intelligence: ' + roll_die(3, 6)]
    character.extend(intelligence)
    wisdom = ['Wisdom: ' + roll_die(3, 6)]
    character.extend(wisdom)
    dexterity = ['Dexterity: ' + roll_die(3, 6)]
    character.extend(dexterity)
    constitution = ['Constitution: ' + roll_die(3, 6)]
    character.extend(constitution)
    charisma = ['Charisma: ' + roll_die(3, 6)]
    character.extend(charisma)
    # set initial experience points
    experience_points = [str(0) + ' XP']
    character.extend(experience_points)
    # set class
    character.insert(1, choose_class())
    # set initial hit points
    character.insert(2, (class_die_roll(character[1]) + ' HP'))
    print(character)
    return character


def choose_class():
    # docstring for incomplete name ('bar')
    global character_class
    classes_help_message = '\nHere\'s what\'s available:\n\nBarbarian\nBard\nCleric\nDruid\nFighter\nMonk\nPaladin\n' \
                           'Ranger\nRogue\nSorcerer\nWarlock\nWizard\nBlood Hunter'
    classes_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer',
                    'Warlock', 'Wizard', 'Blood Hunter']
    character_class = (input('\nEnter a class: ')).title()
    if character_class == 'Help':
        print(classes_help_message)
        return choose_class()
    elif character_class in classes_list:
        print('\n\n\n"Ah, the ' + character_class + '... A most excellent choice."\n')
        return character_class
    else:
        print('\n"That\'s not a class!" Try again or type HELP for your options: ')
        return choose_class()


def class_die_roll(character):
    global character_class
    if character in ['Bard', 'Cleric', 'Druid', 'Monk', 'Rogue', 'Warlock']:
        return roll_die(1, 8)
    elif character in ['Fighter', 'Paladin', 'Ranger', 'Blood Hunter']:
        return roll_die(1, 10)
    elif character in ['Sorcerer', 'Wizard']:
        return roll_die(1, 6)
    elif character == 'Barbarian':
        return roll_die(1, 12)
    else:
        return


def combat_round(opponent_one, opponent_two):
    """

    :param opponent_one:
    :param opponent_two:
    :return:
    PRECONDITION: 'will not work unless both parameters are well-formed lists each containing a correct character.
    """
    opponent_one_first_roll = int(roll_die(1, 20))
    print(opponent_one[0] + ' the ' + opponent_one[1] + ' rolls a ' + str(opponent_one_first_roll) + '.')
    opponent_two_first_roll = int(roll_die(1, 20))
    print(opponent_two[0] + ' the ' + opponent_two[1] + ' rolls a ' + str(opponent_two_first_roll) + '.')
    if opponent_one_first_roll > opponent_two_first_roll:
        print(opponent_one[0] + ' attacks first!\n\n')
        print(input('Press ENTER'))
        hit_checker(opponent_two, opponent_one)
    elif opponent_one_first_roll < opponent_two_first_roll:
        print(opponent_two[0] + ' attacks first!\n\n')
        print(input('Press ENTER'))
        hit_checker(opponent_one, opponent_two)
    else:
        print('Tie! Roll again.')
        return combat_round(opponent_one, opponent_two)


def hit_checker(defender, attacker):
    defense_dexterity = defender[6]
    print('\n' + defender[0] + '\'s ' + defense_dexterity.lower())
    defense_dexterity_list = list(defense_dexterity)
    defense_dexterity_slice = defense_dexterity_list[11:]
    if len(defense_dexterity_slice) == 2:
        defense_dexterity_integer = int(str(defense_dexterity_slice[0]) + str(defense_dexterity_slice[1]))
    else:
        defense_dexterity_integer = int(defense_dexterity_slice[0])
    hit_roll = int(roll_die(1, 20))
    print(attacker[0] + ' takes aim... (' + attacker[0] + ' rolls a ' + str(hit_roll) + ')')
    if int(hit_roll) > defense_dexterity_integer:
        print(attacker[0] + ' lands the hit!\n')
        attack(defender, attacker)
    else:
        print(attacker[0] + ' misses!')
        return hit_checker(attacker, defender)
# change to element[0][2]


def attack(defender, attacker):
    defense_initial_hp = defender[2]
    print(defender[0] + ' had ' + defense_initial_hp + '.')
    defense_initial_hp_list = list(defense_initial_hp)
    defense_initial_hp_integer = int(defense_initial_hp_list[0])
    damage = int(class_die_roll(attacker[1]))
    print(attacker[0] + ' inflicts ' + str(damage) + ' damage.')
    defense_hp_after_hit = defense_initial_hp_integer - damage
    if defense_hp_after_hit <= 0:
        print(defender[0] + ' DIED!')
    else:
        print(defender[0] + ' has ' + str(defense_hp_after_hit) + ' HP remaining.')
# split into damage taken function.


def main():
    """Execute the program."""
    user_messages('introduction')
    opponent_one = generate_character()
    user_messages('opponent_select')
    opponent_two = generate_character()
    user_messages('get_ready')
    user_messages('roll_for_first')
    combat_round(opponent_one, opponent_two)


if __name__ == '__main__':
    main()
    doctest.testmod()
