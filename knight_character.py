from random import randint
from abstract_character import AbstractCharacter

class KnightCharacter(AbstractCharacter):
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
        self._sword_crit_chance = (19,20)
        self._sword_crit_modifier = 0.5
        self._shield_defence_modifier = 0.3

    def get_type(self):
        return 'Knight'

    def get_stats(self):
        print("Username: {}".format(self._username))
        print("Health: {}".format(self._health))
        print("Attack: {}".format(self._attack))
        print("Defence: {}".format(self._defence))
        print("Attack Speed: {}".format(self._attack_speed))
        print('Sword Crit Chance: 10%')
        print('Sword Crit Damage: {}'.format((self._attack + int(self._attack * self._sword_crit_modifier))))
        print('Shield Defence Modifier: 30%')

    def get_damage(self):
        if randint(1, 20) in self._sword_crit_chance:
            return self._attack + int(self._attack * self._sword_crit_modifier)
        else:
            return super().get_damage()

    def take_damage(self, damage):
        damage = damage - int(self._defence * self._shield_defence_modifier)
        self._health -= damage
