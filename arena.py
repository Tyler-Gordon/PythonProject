class Arena:
    def __init__(self):
        self._characters = []

    def add_character(self,character):
        self._characters.append(character)
    
    def get_character(self,username):
        for character in self._characters:
            if character.get_username() == username:
                return character

    def get_all(self):
        return self._characters

    def get_all_by_type(self,type):
        type_list = []
        for character in self._characters:
            if character.get_type() == type:
                type_list.append(character)

        return type_list

    def update(self,character):
        pass

    def delete(self,character):
        self._characters.remove(character)

    def start_tournament(self):
        pass

    @staticmethod
    def start_battle(player1, player2):
        pass