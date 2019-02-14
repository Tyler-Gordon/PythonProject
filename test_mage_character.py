from unittest import TestCase
import inspect
from mage_character import MageCharacter

class TestMageCharacter(TestCase):

    def setUp(self):
        """ Creates a test_mage instance and logs the test.
        """
        self.test_mage = MageCharacter('Garry')
        self.logPoint()

    def logPoint(self):
        """ Override of logPoint that documents console test output.
        """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in {} calling {}'.format(current_test, calling_function))
    
    def test_mage_character_class(self):
        """ Test that mage has been properly instantiated.
        """
        self.assertIsNotNone(self.test_mage,"Mage Character must be defined.")

    def test_get_type(self):
        """ Test that get_type returns "Mage"
        """
        self.assertEqual('Mage', self.test_mage.get_type(), 'Must return "Mage"')

    def test_get_stats(self):
        """ Test returns the same string.
        """
        username = "Username: {}\n".format('Garry')
        health = "Health: {}\n".format(100)
        attack = "Attack: {}\n".format(10)
        defence = "Defence: {}\n".format(10)
        att_speed = "Attack Speed: {}\n".format(1)
        spell_chance = 'Spell Chance: 10%'
        spell_damage = 'Spell Damage: {}'.format(self.test_mage.get_damage(20))
        test_stats_string = username + health + attack + defence + att_speed + spell_chance + spell_damage

        self.assertEqual(test_stats_string, self.test_mage.get_stats(),
                         "Strings must be the same.")


    def test_get_damage(self):
        """ Test that spell damage works if 19 or 20 is rolled.
            Test that the normal damage range is returned otherwise.
        """
        self.assertEqual(40, self.test_mage.get_damage(20),
                        "Spell Damage must equal 40.")
        self.assertIn(self.test_mage.get_damage(1), range(5,11),
                      "Damage must be in range: 5-10")


    #Testing Abstract Methods
    def test_take_damage(self):
        """ Test that damage is properly reduced.
        """
        self.test_mage.take_damage(10)
        self.assertEqual(self.test_mage.get_health(), 91, "Health must equal 91.")

    def test_get_username(self):
        """ Test username is Garry
        """
        self.assertEqual('Garry', self.test_mage.get_username(),
                         'Username must be Garry.')
                         
    def test_get_health(self):
        """ Test health is equal to 100
        """
        self.assertEqual(100, self.test_mage.get_health(),
                         'Health must be 100.')
    
    def test_get_attack_speed(self):
        """ Test attack_speed is equal to 1
        """
        self.assertEqual(1, self.test_mage.get_attack_speed(),
                         'Attack Speed must be 1.')
    
    def test_get_die_roll(self):
        """ Test die_roll is between 1,20
        """
        self.assertIn(self.test_mage.get_die_roll(),range(1,21),
                         'Die roll must be in range 1-20.')