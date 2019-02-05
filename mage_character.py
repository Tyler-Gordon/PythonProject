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
    
    def get_damage(self):
        if randint(1,20) in self._spell_chance:
            return self._attack + self._spell_power
        else:
            return super().get_damage()

    def get_stats(self):
        raise NotImplementedError

    def get_type(self):
        return "Mage"
