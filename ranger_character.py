from random import randint
from abstract_character import AbstractCharacter

class RangerCharacter(AbstractCharacter):
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
        username = "Username: {}\n".format(self._username)
        health = "Health: {}\n".format(self._health)
        attack = "Attack: {}\n".format(self._attack)
        defence = "Defence: {}\n".format(self._defence)
        att_speed = "Attack Speed: {}\n".format(self._attack_speed)
        dodge_chance = 'Dodge Chance: 5%'
        bow_chance = 'Bow Crit Chance: 20%'
        bow_damage = 'Bow Crit Damage: {}'.format(self.get_damage(20))
        stats_string = username + health + attack + defence + att_speed + dodge_chance + bow_chance + bow_damage
        return stats_string
        
    def get_damage(self, die_roll=0):
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll in self._bow_crit_chance:
            return self._attack + int(self._attack * self._bow_crit_modifier)
        else:
            return super().get_damage()

    def take_damage(self, damage, die_roll=0):
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll == self._dodge_chance:
            return
        else:
            super().take_damage(damage)