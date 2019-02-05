class Arena:
    def __init__(self):
        self._characters = []

    def add(self,character):
        self._characters.append(character)
    def get(self,username):
        for character in self._characters:
            if character.get_username() == username:
                return character
            else: 
                next

    def get_all(self):
        return self._characters
    def get_all_by_type(self,type):
        player_type_list = []
        for character in self._characters:
            if character.get_type() == type:
                player_type_list.append(character)
            else:
                next
        return player_type_list

    def update(self,character):
        pass

    def delete(self,username):
        for character in self._characters:
            if character.get_username == username:
                self._characters.pop(character)
            else:
                next

    def start_tournament(self,):
        pass

    @staticmethod
    def _start_battle(player1, player2):
        pass