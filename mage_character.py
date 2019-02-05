from random import randint
from abstract_character import AbstractCharacter

class MageCharacter(AbstractCharacter):
    """[summary]
    """
    def __init__(self, username):
        self._username = username
        self._health = 100
        self._attack = 10
        self._defence = 10
        self._attack_speed = 1
        self._spell_power = 30
        self._spell_chance = (19,20)

    def get_type(self):
        return "Mage"
    
    def get_stats(self):
        print("Username: {}".format(self._username))
        print("Health: {}".format(self._health))
        print("Attack: {}".format(self._attack))
        print("Defence: {}".format(self._defence))
        print("Attack Speed: {}".format(self._attack_speed))
        print('Spell Chance: 10%')
        print('Spell Damage: {}'.format((self._attack + self._spell_power)))

    def get_damage(self):
        if randint(1,20) in self._spell_chance:
            return self._attack + self._spell_power
        else:
            return super().get_damage()
