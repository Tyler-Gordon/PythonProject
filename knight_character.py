from sqlalchemy import Column, Integer, String
from random import randint
from abstract_character import AbstractCharacter

class KnightCharacter(AbstractCharacter):
    """ Child Class from AbstractCharacter
    
    Arguments:
        AbstractCharacter {Class} -- Parent Class
    """

    KNIGHT_CHARACTER_TYPE = "knight"

    sword_crit_chance = Column(Integer),
    sword_crit_modifier = Column(Integer),
    shield_defence_modifier = Column(Integer)

    def __init__(self, username, health, attack, defence, attack_speed, type, sword_crit_chance,
                sword_crit_modifier, shield_defence_modifier):
        """ Constructor """
        super(KnightCharacter, self).__init__(username, health, attack, defence, attack_speed, type)
        self.sword_crit_chance = sword_crit_chance
        self.sword_crit_modifier = sword_crit_modifier
        self.shield_defence_modifier = shield_defence_modifier

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
        if die_roll in self.sword_crit_chance:
            return self.sword_swing()
        else:
            return super().get_damage()

    def take_damage(self, damage):
        """ Applies damage to Knight after being reduced by its shield modifier
        
        Arguments:
            damage {int} -- Damage dealt to Knight
        """

        damage = damage - int(self.defence * self.shield_defence_modifier)
        self.health -= damage

    def sword_swing(self):
        return self.attack + int(self.attack * self.sword_crit_modifier)

    def to_dict(self):
        dict = super().to_dict()
        dict['sword_crit_chance'] = self.sword_crit_chance
        dict['sword_crit_modifier'] = self.sword_crit_modifier
        dict['shield_defence_modifier'] = self.shield_defence_modifier
        return dict

    def copy(self, object):
        super().copy(object)
        self.sword_crit_chance = object.sword_crit_chance
        self.sword_crit_modifier = object.sword_crit_modifier
        self.shield_defence_modifier = object.shield_defence_modifier