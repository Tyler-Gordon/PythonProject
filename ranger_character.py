from random import randint
from abstract_character import AbstractCharacter

class RangerCharacter(AbstractCharacter):
    """ Child Class from AbstractCharacter
    
    Arguments:
        AbstractCharacter {Class} -- Parent Class
    """

    def __init__(self, username):
        """ Initializer for RangerCharacter class
        
        Arguments:
            username {string} -- Character's input username
        """

        self._username = username
        self._health = 100
        self._attack = 10
        self._defence = 10
        self._attack_speed = 1
        self._dodge_chance = 20
        self._bow_crit_chance = (18,19,20)
        self._bow_crit_modifier = 0.5

    def get_type(self):
        """ Returns Character type
        
        Returns:
            string -- Character's type
        """

        return 'Ranger'

    def get_stats(self):
        """ Returns stats for Ranger
        
        Returns:
            string -- Ranger Character's stats
        """

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
        """ Returns crit damage if 18,19,20 is rolled. Otherwise
            calls parent version of method.         
        Keyword Arguments:
            die_roll {int} -- die_roll implemented for testing purposes
            such that crits can be guaranteed. Default is set for usage in
            Arena class and actual combat.(default: {0})
        
        Returns:
            int -- Damage dealt in combat
        """
        
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll in self._bow_crit_chance:
            return self.shoot_bow()
        else:
            return super().get_damage()

    def take_damage(self, damage, die_roll=0):
        """ Returns if 20 is rolled and Ranger dodges the attack.
            Otherwise calls parent version of method.         
        Keyword Arguments:  
            die_roll {int} -- die_roll implemented for testing purposes
            such that dodges can be guaranteed. Default is set for usage in
            Arena class and actual combat.(default: {0})
        
        Returns:
            int -- Damage dealt in combat
        """
        
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll == self._dodge_chance:
            return
        else:
            super().take_damage(damage)
    
    def shoot_bow(self):
        return self._attack + int(self._attack * self._bow_crit_modifier)