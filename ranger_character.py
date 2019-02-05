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
        self._dodge_chance = 20
        self._bow_crit_chance = (18,19,20)
        self._bow_crit_modifier = 0.5

    def get_type(self):
        return 'Ranger'

    def get_stats(self):
        print("Username: {}".format(self._username))
        print("Health: {}".format(self._health))
        print("Attack: {}".format(self._attack))
        print("Defence: {}".format(self._defence))
        print("Attack Speed: {}".format(self._attack_speed))
        print('Dodge Chance: 5%')
        print('Bow Crit Chance: 20%')
        print('Bow Crit Damage: {}'.format((self._attack + int(self._attack * self._bow_crit_modifier))))

    def get_damage(self):
        if randint(1, 20) in self._bow_crit_chance:
            return self._attack + int(self._attack * self._bow_crit_modifier)
        else:
            return super().get_damage()

    def take_damage(self, damage):
        if randint(1, 20) == self._dodge_chance:
            return
        else:
            super().take_damage(damage)