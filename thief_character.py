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
        username = "Username: {}\n".format(self._username)
        health = "Health: {}\n".format(self._health)
        attack = "Attack: {}\n".format(self._attack)
        defence = "Defence: {}\n".format(self._defence)
        att_speed = "Attack Speed: {}\n".format(self._attack_speed)
        dodge_chance = 'Dodge Chance: 15%'
        stats_string = username + health + attack + defence + att_speed + dodge_chance
        return stats_string

    def take_damage(self, damage, die_roll=0):
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll in self._dodge_chance:
            return
        else:
            super().take_damage(damage)