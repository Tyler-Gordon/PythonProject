from sqlalchemy import Column, Integer, String
from random import randint
from abstract_character import AbstractCharacter

class MageCharacter(AbstractCharacter):
    """ Child Class from AbstractCharacter
    
    Arguments:
        AbstractCharacter {Class} -- Parent Class
    """

    MAGE_CHARACTER_TYPE = "mage"

    spell_power = Column(Integer)
    spell_chance = Column(Integer)

    def __init__(self, username, health, attack, defence, attack_speed, type, spell_power, spell_chance):
        """ Initializer for MageCharacter class
        """

        super(MageCharacter, self).__init__(username, health, attack, defence, attack_speed, type)
        self.spell_power = spell_power
        self.spell_chance = spell_chance

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
        if die_roll in self.spell_chance:
            return self.spell()
        else:
            return super().get_damage()

    def spell(self):
        return self.attack + self.spell_power

    def to_dict(self):
        dict = super().to_dict()
        dict['spell_power'] = self.spell_power
        dict['spell_chance'] = self.spell_chance
        return dict

    def copy(self, object):
        super().copy(object)
        self.spell_power = object.spell_power
        self.spell_chance = object.spell_chance