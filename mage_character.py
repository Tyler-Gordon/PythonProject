from random import randint
from abstract_character import AbstractCharacter

class MageCharacter(AbstractCharacter):
    """ Child Class from AbstractCharacter
    
    Arguments:
        AbstractCharacter {Class} -- Parent Class
    """

    def __init__(self, username):
        """ Initializer for MageCharacter class
        
        Arguments:
            username {string} -- Character's input username
        """

        self._username = username
        self._health = 100
        self._attack = 10
        self._defence = 10
        self._attack_speed = 1
        self._spell_power = 30
        self._spell_chance = (19,20)

    def get_type(self):
        """ Returns Character type
        
        Returns:
            string -- Character's type
        """

        return "Mage"
    
    def get_stats(self):
        """ Returns stats for Mage
        
        Returns:
            string -- Mage Character's stats
        """

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
        """ Returns spell damage if 19,20 is rolled. Otherwise
            calls parent version of method.         
        Keyword Arguments:
            die_roll {int} -- die_roll implemented for testing purposes
            such that spells can be guaranteed. Default is set for usage in
            Arena class and actual combat.(default: {0})
        
        Returns:
            int -- Damage dealt in combat
        """
        
        if not die_roll:
            die_roll = self.get_die_roll()
        if die_roll in self._spell_chance:
            return self.spell()
        else:
            return super().get_damage()

    def spell(self):
        return self._attack + self._spell_power