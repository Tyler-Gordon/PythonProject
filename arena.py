class Arena:
    """Manager Class for all character classes"""
    
    def __init__(self):
        """Initializes the Arena class"""
        self._characters = []

    def add_character(self,character):
        """Adds a character object to the list of characters
        
        Arguments:
            character {class} -- character object
        """

        self._characters.append(character)
    
    def get_character(self,username):
        """Returns a character based on the username supplied
        
        Arguments:
            username {string} -- The username of the character
        
        Returns:
            object -- The character object
        """

        for character in self._characters:
            if character.get_username() == username:
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

        for character_in_list in self._characters:
            if character.get_username == character_in_list.get_username():
                self._characters.remove(character_in_list)
                self._characters.append(character)

    def delete(self,character):
        """Removes a character from the list of characters
        
        Arguments:
            character {class} -- Character object to be deleted
        """

        self._characters.remove(character)