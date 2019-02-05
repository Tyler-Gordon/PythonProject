from random import randint

class AbstractCharacter:
    """[summary]
    """
    def __init__(self, username):
        self._username = username
        self._health = 0
        self._attack = 0
        self._defence = 0
        self._attack_speed = 0
    
    def get_username(self):
        return self._username

    def get_health(self):
        return self._health
    
    def get_damage(self):
        damage = randint(int(self._attack * 0.5), self._attack)
        return damage

    def take_damage(self, damage):
        damage = damage - int(self._defence * 0.1)
        self._health -= damage
    
    def get_attack_speed(self):
        return self._attack_speed

    def get_stats(self):
        raise NotImplementedError

    def get_type(self):
        raise NotImplementedError

    def test_git(self):
        pass