from random import randint
from abstract_character import AbstractCharacter

class KnightCharacter(AbstractCharacter):
    """ Child Class from AbstractCharacter
    
    Arguments:
        AbstractCharacter {Class} -- Parent Class
    """
    def __init__(self, username):
        """ Initializer for KnightCharacter class
        
        Arguments:
            username {string} -- Character's input username
        """

        self._username = username
        self._health = 100
        self._attack = 10
        self._defence = 10
        self._attack_speed = 1
        self._sword_crit_chance = (19,20)
        self._sword_crit_modifier = 0.5
        self._shield_defence_modifier = 0.3

    def get_type(self):
        """ Returns Character type
        
        Returns:
            string -- Character's type
        """

        return 'Knight'

    def get_stats(self):
        """ Returns stats for Knight
        
        Returns:
            string -- Knight Character's stats
        """

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
        """ Returns crit damage if 19,20 is rolled. Otherwise
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
        if die_roll in self._sword_crit_chance:
            return self._attack + int(self._attack * self._sword_crit_modifier)
        else:
            return super().get_damage()

    def take_damage(self, damage):
        """ Applies damage to Knight after being reduced by its shield modifier
        
        Arguments:
            damage {int} -- Damage dealt to Knight
        """

        damage = damage - int(self._defence * self._shield_defence_modifier)
        self._health -= damage
