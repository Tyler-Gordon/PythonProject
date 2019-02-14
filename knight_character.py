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
        username = "Username: {}\n".format(self._username)
        health = "Health: {}\n".format(self._health)
        attack = "Attack: {}\n".format(self._attack)
        defence = "Defence: {}\n".format(self._defence)
        att_speed = "Attack Speed: {}\n".format(self._attack_speed)
        sword_crit = 'Sword Crit Chance: 10%\n'
        crit_damage = 'Sword Crit Damage: {}\n'.format(self.get_damage(20))
        def_modifier = 'Shield Defence Modifier: 30%\n'
        stats_string = username + health + attack + defence + att_speed + sword_crit + crit_damage + def_modifier
        return stats_string

    def get_damage(self, die_roll=0):
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll in self._sword_crit_chance:
            return self._attack + int(self._attack * self._sword_crit_modifier)
        else:
            return super().get_damage()

    def take_damage(self, damage):
        damage = damage - int(self._defence * self._shield_defence_modifier)
        self._health -= damage
