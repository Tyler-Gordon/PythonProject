from unittest import TestCase
import inspect
from knight_character import KnightCharacter

class TestKnightCharacter(TestCase):

    def setUp(self):
        """ Creates a test_knight instance and logs the test.
        """
        self.test_knight = KnightCharacter()
        self.logPoint()

    def logPoint(self):
        """ Override of logPoint that documents console test output.
        """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in {} calling {}'.format(current_test, calling_function))
    
    def test_knight_character_class(self):
        """ Test that knight has been properly instantiated.
        """
        self.assertIsNotNone(self.test_knight,"Knight Character must be defined.")

    def test_get_type(self):
        """ Test that get_type returns "Knight"
        """
        self.assertEqual('Knight', self.test_knight.get_type(), 'Must return "Knight"')

    def test_get_stats(self):
        """ Test returns the same string.
        """
        id = "Id: {}\n".format('None')
        health = "Health: {}\n".format(100)
        attack = "Attack: {}\n".format(10)
        defence = "Defence: {}\n".format(10)
        att_speed = "Attack Speed: {}\n".format(1)
        sword_crit = 'Sword Crit Chance: 10%\n'
        crit_damage = 'Sword Crit Damage: {}\n'.format(self.test_knight.get_damage(20))
        def_modifier = 'Shield Defence Modifier: 30%\n'
        test_stats_string = id + health + attack + defence + att_speed + sword_crit + crit_damage + def_modifier

        self.assertEqual(test_stats_string, self.test_knight.get_stats(),
                         "Strings must be the same.")


    def test_get_damage(self):
        """ Test that crit damage works if 19 or 20 is rolled.
            Test that the normal damage range is returned otherwise.
        """
        self.assertEqual(15, self.test_knight.get_damage(20),
                        "Crit Damage must equal 15.")
        self.assertIn(self.test_knight.get_damage(1), range(5,11),
                      "Damage must be in range: 5-10")

    def test_take_damage(self):
        """ Test that damage is properly reduced by _shield_modifier.
        """
        self.test_knight.take_damage(10)
        self.assertEqual(self.test_knight.get_health(), 93, "Health must equal 93.")


    #Testing Abstract methods
    def test_get_health(self):
        """ Test health is equal to 100
        """
        self.assertEqual(100, self.test_knight.get_health(),
                         'Health must be 100.')
    
    def test_get_attack_speed(self):
        """ Test attack_speed is equal to 1
        """
        self.assertEqual(1, self.test_knight.get_attack_speed(),
                         'Attack Speed must be 1.')
    
    def test_get_die_roll(self):
        """ Test die_roll is between 1,20
        """
        self.assertIn(self.test_knight.get_die_roll(),range(1,21),
                         'Die roll must be in range 1-20.')

        