from unittest import TestCase
import inspect
from thief_character import ThiefCharacter

class TestThiefCharacter(TestCase):

    def setUp(self):
        """ Creates a test_thief instance and logs the test.
        """
        self.test_thief = ThiefCharacter('Garry')
        self.logPoint()

    def logPoint(self):
        """ Override of logPoint that documents console test output.
        """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in {} calling {}'.format(current_test, calling_function))
    
    def test_thief_character_class(self):
        """ Test that thief has been properly instantiated.
        """
        self.assertIsNotNone(self.test_thief,"Thief Character must be defined.")

    def test_get_type(self):
        """ Test that get_type returns "Thief"
        """
        self.assertEqual('Thief', self.test_thief.get_type(), 'Must return "Thief"')

    def test_get_stats(self):
        """ Test returns the same string.
        """
        username = "Username: {}\n".format('Garry')
        health = "Health: {}\n".format(100)
        attack = "Attack: {}\n".format(10)
        defence = "Defence: {}\n".format(10)
        att_speed = "Attack Speed: {}\n".format(1)
        dodge_chance = 'Dodge Chance: 15%'
        test_stats_string = username + health + attack + defence + att_speed + dodge_chance

        self.assertEqual(test_stats_string, self.test_thief.get_stats(),
                         "Strings must be the same.")

    def test_take_damage(self):
        """ Test that thief properly dodges and takes no damage.
            Test that thief properly reduces damage when hit.
        """
        self.test_thief.take_damage(10, 20)
        self.assertEqual(self.test_thief.get_health(), 100, "Health must equal 100.")

        self.test_thief.take_damage(10, 1)
        self.assertEqual(self.test_thief.get_health(), 91, "Health must equal 91.")


    #Testing Abstract Methods
    def test_get_damage(self):
        """ Test that the normal damage range is returned.
        """
        self.assertIn(self.test_thief.get_damage(), range(5,11),
                        "Damage must be in range: 5-10")

    def test_get_username(self):
        """ Test username is Garry
        """
        self.assertEqual('Garry', self.test_thief.get_username(),
                         'Username must be Garry.')
                         
    def test_get_health(self):
        """ Test health is equal to 100
        """
        self.assertEqual(100, self.test_thief.get_health(),
                         'Health must be 100.')
    
    def test_get_attack_speed(self):
        """ Test attack_speed is equal to 1
        """
        self.assertEqual(1, self.test_thief.get_attack_speed(),
                         'Attack Speed must be 1.')
    
    def test_get_die_roll(self):
        """ Test die_roll is between 1,20
        """
        self.assertIn(self.test_thief.get_die_roll(),range(1,21),
                         'Die roll must be in range 1-20.')