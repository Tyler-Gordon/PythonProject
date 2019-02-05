from random import randint
from abstract_character import AbstractCharacter

class ThiefCharacter(AbstractCharacter):
    """[summary]
    
    Arguments:
        AbstractCharacter {[type]} -- [description]
    """
    def __init__(self, username):
        self._username = username
        self._health = 100
        self._attack = 10
        self._defence = 10
        self._attack_speed = 1
        self._dodge_chance = (18,19,20)

    def get_type(self):
        return 'Thief'

    def get_stats(self):
        print("Username: {}".format(self._username))
        print("Health: {}".format(self._health))
        print("Attack: {}".format(self._attack))
        print("Defence: {}".format(self._defence))
        print("Attack Speed: {}".format(self._attack_speed))
        print('Dodge Chance: 15%')

    def take_damage(self, damage):
        if randint(1, 20) in self._dodge_chance:
            return
        else:
            super().take_damage(damage)