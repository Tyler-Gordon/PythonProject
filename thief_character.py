from random import randint
from abstract_character import AbstractCharacter

class ThiefCharacter(AbstractCharacter):
    """ Child Class from AbstractCharacter
    
    Arguments:
        AbstractCharacter {Class} -- Parent Class
    """

    def __init__(self):
        """ Initializer for ThiefCharacter class
        """

        super(ThiefCharacter, self).__init__()
        self._dodge_chance = (18,19,20)

    def get_type(self):
        """ Returns Character type
        
        Returns:
            string -- Character's type
        """

        return 'Thief'

    def get_stats(self):
        """ Returns stats for Thief
        
        Returns:
            string -- Thief Character's stats
        """

        id = "Id: {}\n".format(self._id)
        health = "Health: {}\n".format(self._health)
        attack = "Attack: {}\n".format(self._attack)
        defence = "Defence: {}\n".format(self._defence)
        att_speed = "Attack Speed: {}\n".format(self._attack_speed)
        dodge_chance = 'Dodge Chance: 15%'
        stats_string = id + health + attack + defence + att_speed + dodge_chance
        return stats_string

    def take_damage(self, damage, die_roll=0):
        """ Returns if 18,19,20 is rolled and Thief dodges the attack.
            Otherwise calls parent version of method.         
        Keyword Arguments:
            die_roll {int} -- die_roll implemented for testing purposes
            such that dodge can be guaranteed. Default is set for usage in
            Arena class and actual combat.(default: {0})
        
        Returns:
            int -- Damage dealt in combat
        """
        
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll in self._dodge_chance:
            return
        else:
            super().take_damage(damage)