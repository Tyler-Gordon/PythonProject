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
        username = "Username: {}\n".format(self._username)
        health = "Health: {}\n".format(self._health)
        attack = "Attack: {}\n".format(self._attack)
        defence = "Defence: {}\n".format(self._defence)
        att_speed = "Attack Speed: {}\n".format(self._attack_speed)
        spell_chance = 'Spell Chance: 10%'
        spell_damage = 'Spell Damage: {}'.format(self.get_damage(20))
        stats_string = username + health + attack + defence + att_speed + spell_chance + spell_damage
        return stats_string

    def get_damage(self, die_roll=0):
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll in self._spell_chance:
            return self._attack + self._spell_power
        else:
            return super().get_damage()
