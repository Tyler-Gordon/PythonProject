from abstract_character import AbstractCharacter
from knight_character import KnightCharacter
from mage_character import MageCharacter
from ranger_character import RangerCharacter
from thief_character import ThiefCharacter

from random import random
class Arena:
    """Manager Class for all character classes"""
    
    def __init__(self,filepath):
        """Initializes the Arena class"""
        self._characters = []
        self._filepath = filepath
    def add_character(self,new_character):
        """Adds a character object to the list of characters
        
        Arguments:
            character {class} -- character object
        """
        charid = random()

        id = [character.get_id() for character in self._characters]

        if charid not in id:
            new_character.set_id(charid)
            self._characters.append(new_character)
        else:
            print('Character ID already in use.')
        ##############################################
        #       must somehow return an int????       #
        ############################################## 

    def get_character(self,id):
        """Returns a character based on the id supplied
        
        Arguments:
            id {string} -- The id of the character
        
        Returns:
            object -- The character object
        """

        for character in self._characters:
            if character.get_id() == id:
                return character

    def get_all(self):
        """Returns all of the objects in the character list
        
        Returns:
            list -- list of all character objects
        """

        return self._characters

    def get_all_by_type(self,type):
        """Returns all characters based on their player class
        
        Arguments:
            type {string} -- The class, or type of the user
        
        Returns:
            list -- list of all objects with given type
        """

        type_list = []
        for character in self._characters:
            if character.get_type() == type:
                type_list.append(character)

        return type_list

    def update(self,character):
        """Replaces the character with the same ID with an updated character
        
        Arguments:
            character {class} -- The new character to be replaced
        """
        if character not in self._characters:
            return 'Character not in the arena'
        else:
            for character_in_list in self._characters:
                if character.get_id == character_in_list.get_id():
                    self._characters.remove(character_in_list)
                    self._characters.append(character)

    def delete(self,id):
        """Removes a character from the list of characters
        
        Arguments:
            character {class} -- Character object to be deleted
        """

        for character in self._characters:
            if character.get_id() == id:
                self._characters.remove(character)

    def _read_employees_from_file():
        with open(self._filepath) as file:
            data = json.load(f)
            
        for user in data:
            if user.type == 'Knight':
                character = KnightCharacter()
            elif user.type == 'Mage':
                character = MageCharacter()
            elif user.type == 'Ranger':
                character = RangerCharacter()
            elif user.type == 'Thief':
                character = ThiefCharacter()
        
            self._characters.append(character)

    def _write_employees_to_file():
        data = []
        for character in self._characters:
            data.append(character.to_dict())

        with open(self._filepath, 'w') as file:  
            json.dump(data, file)
    
    @staticmethod
    def _validate_string_input(id):
        """ Private helper to validate string values """
        if id is None:
            raise ValueError("ID cannot be undefined.")

        if id == "":
            raise ValueError("ID cannot be empty.")

    @staticmethod
    def _validate_student(character):
        """ Private helper to validate students """

        if character is None:
            raise ValueError("Character must be defined.")
