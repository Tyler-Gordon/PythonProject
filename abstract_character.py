from sqlalchemy import Column, Integer, String
from base import Base
from random import randint

class AbstractCharacter(Base):
    """ Character Declarative """
    
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    health = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defence = Column(Integer, nullable=False)
    attack_speed = Column(Integer, nullable=False)
    type = Column(String(10), nullable=False)

    def __init__(self, username, health, attack, defence, attack_speed, type):
        """ Constructor """

        AbstractCharacter._validate_parameter(username)
        self.username = username

        AbstractCharacter._validate_parameter(health, int)
        self.health = health

        AbstractCharacter._validate_parameter(attack, int)
        self.attack = attack

        AbstractCharacter._validate_parameter(defence, int)
        self.defence = defence

        AbstractCharacter._validate_parameter(attack_speed, int)
        self.attack_speed = attack_speed

        self.type = type

    def get_damage(self):
        """ Calculates damage based on 50% to 100% of Character's attack
        
        Returns:
            int -- Damage Character deals when attacking
        """
        
        damage = randint(int(self.attack * 0.5), self.attack)
        return damage

    def take_damage(self, damage):
        """ Calculates and deals damage to Character based on input damage and Defence
        
        Arguments:
            damage {int} -- Damage dealt to Character
        """
        AbstractCharacter._validate_parameter(damage, int)

        damage = damage - int(self.defence * 0.1)
        self.health -= damage
        
    def get_die_roll(self):
        """ Returns an integer between 1,20 to simulate a d20 roll
        
        Returns:
            int -- Die roll between 1,20
        """

        return randint(1,20)
        
    def to_dict(self):
        """ Converts attributes to dict """
        dict = {}
        dict['username'] = self.username
        dict['health'] = self.health
        dict['attack'] = self.attack
        dict['defence'] = self.defence
        dict['attack_speed'] = self.attack_speed
        dict['type'] = self.type

        return dict

    def copy(self, object):
        """ Copies object to character """
        if object.type == self.type:
            self.username = object.username
            self.health = object.health
            self.attack = object.attack
            self.defence = object.defence
            self.attack_speed = object.attack_speed

    @staticmethod
    def _validate_parameter(arg, optional_type=None):
        if optional_type:
            if not isinstance(arg, optional_type):
                raise ValueError
        if not arg:
            raise ValueError