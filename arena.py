from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

from abstract_character import AbstractCharacter
from knight_character import KnightCharacter
from mage_character import MageCharacter
from random import randint


class Arena:
    """Manager Class for all character classes"""
    
    def __init__(self, db_filename):
        """Initializes the Arena class"""
        if not db_filename:
            raise ValueError("Invalid Database File")

        engine = create_engine('sqlite:///' + db_filename)
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)

    def add_character(self, character):
        """Adds a character """

        char_class = Arena._check_type(character)
        if not character or not isinstance(character, char_class):
            raise ValueError("Invalid Character Object")

        session = self._db_session()
        session.add(character)
        session.commit()

        char_id = character.id
        session.close()
        return char_id

    def update_character(self, character):
        """Replaces the character with the same ID """
        char_class = Arena._check_type(character)
        if not character or not isinstance(character, char_class):
            raise ValueError("Invalid Character Object")

        session = self._db_session()
        existing_character = session.query(char_class).filter(char_class.id == character.id).first()
        existing_character.copy(character)

        session.commit()
        session.close()
    
    def delete_character(self,char_id):
        """Removes a character """
        session = self._db_session()
        existing_character = self.get_character(char_id)

        session.delete(existing_character)
        session.commit()
        session.close()

    

    def get_character(self, char_id):
        """Returns a character with the given char_id"""

        session = self._db_session()
        existing_character = session.query(KnightCharacter).filter(KnightCharacter.id == char_id).first()
        
        if existing_character:
            if existing_character.type != 'knight':
                existing_character = session.query(MageCharacter).filter(MageCharacter.id == char_id).first()
                
        session.close()

        return existing_character


    def get_all(self):
        """Returns all characters"""
        existing_characters = []
        session = self._db_session()
        
        existing_characters.extend(session.query(KnightCharacter,KnightCharacter.id).filter(KnightCharacter.type == 'knight').all())
        existing_characters.extend(session.query(MageCharacter,MageCharacter.id).filter(MageCharacter.type == 'mage').all())
        #print(existing_characters)
        # session.query(AbstractCharacter.id).distinct():

        
        session.close()
        return existing_characters

    def get_all_by_type(self, char_type):
        """Returns all characters based type"""
        session = self._db_session()
        existing_characters = []

        if char_type == 'knight':
            existing_characters.extend(session.query(KnightCharacter).filter(KnightCharacter.type == 'knight').all())
        elif char_type == 'mage':
            existing_characters.extend(session.query(MageCharacter).filter(MageCharacter.type == 'mage').all())

        session.close()

        return existing_characters
            
    @staticmethod
    def _check_type(character):
        if not character:
            raise ValueError("Invalid Character Object")
        if character.type == 'mage':
            return MageCharacter
        elif character.type == 'knight':
            return KnightCharacter
