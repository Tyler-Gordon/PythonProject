from abstract_character import AbstractCharacter
from knight_character import KnightCharacter
from mage_character import MageCharacter
import json
from random import randint


class Arena:
    """Manager Class for all character classes"""
    
    def __init__(self,filepath):
        """Initializes the Arena class"""
        self._characters = []
        self._filepath = filepath
        self._read_characters_from_file()

    def add_character(self, new_character):
        """Adds a character object to the list of characters
        
        Arguments:
            character {class} -- character object
        """
        char_id = randint(1,10000)

        all_char_ids = [character.get_id() for character in self._characters]

        if char_id not in all_char_ids:
            new_character.set_id(char_id)
            self._characters.append(new_character)
            self._write_characters_to_file()
            return char_id

        else:
            print('Character ID already in use.')
            return None

    def get_character(self, char_id):
        """Returns a character based on the char_id supplied
        
        Arguments:
            char_id {string} -- The char_id of the character
        
        Returns:
            object -- The character object
        """

        for character in self._characters:
            if character.get_id() == char_id:
                return character

    def get_all(self):
        """Returns all of the objects in the character list
        
        Returns:
            list -- list of all character objects
        """

        return self._characters

    def get_all_by_type(self, char_type):
        """Returns all characters based on their player class
        
        Arguments:
            char_type {string} -- The class, or type of the user
        
        Returns:
            list -- list of all objects with given type
        """

        char_type_list = [character for character in self._characters if character.get_type() == char_type]
        return char_type_list

    def update(self, new_character):
        """Replaces the character with the same ID with an updated character
        
        Arguments:
            new_character {class} -- The new character to be replaced
        """
        for character in self._characters:
            if character.get_id() == new_character.get_id():
                self._characters.remove(character)
                self._characters.append(new_character)
                self._write_characters_to_file()
                return

        return 'Character not in the arena'

    def delete(self,char_id):
        """Removes a character from the list of characters
        
        Arguments:
            char_id {class} -- ID of Character object to be deleted
        """

        for character in self._characters:
            if character.get_id() == char_id:
                self._characters.remove(character)
                self._write_characters_to_file()

    def _read_characters_from_file(self):
        with open(self._filepath) as f:
            data = json.load(f)
            
        for character in data:
            if character["type"] == 'knight':
                current_character = KnightCharacter(character["username"], character["health"],
                                        character["attack"], character["defence"], character["attack_speed"])
                current_character.set_id(character['id'])

            elif character["type"] == 'mage':
                current_character = MageCharacter(character["username"], character["health"],
                                        character["attack"], character["defence"], character["attack_speed"])
                current_character.set_id(character['id'])

            self._characters.append(current_character)

    def _write_characters_to_file(self):
        data = [character.to_dict() for character in self._characters]

        with open(self._filepath, 'w') as f:  
            f.write(json.dumps(data))
        
    @staticmethod
    def _validate_string_input(char_id):
        """ Private helper to validate string values """
        if char_id is None:
            raise ValueError("ID cannot be undefined.")

        if char_id == "":
            raise ValueError("ID cannot be empty.")

    @staticmethod
    def _validate_character(character):
        """ Private helper to validate students """

        if character is None:
            raise ValueError("Character must be defined.")
