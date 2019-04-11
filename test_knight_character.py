from unittest import TestCase
import inspect
from knight_character import KnightCharacter

class TestKnightCharacter(TestCase):

    def setUp(self):
        """ Creates a test_knight instance and logs the test.
        """
        self.test_knight = KnightCharacter('Connor',10000,100,100,10,10,10,10,10)
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

    def test_get_damage(self):
        """ Test that crit damage works if 19 or 20 is rolled.
            Test that the normal damage range is returned otherwise.
        """
        self.assertEqual(1100, self.test_knight.get_damage(10),
                        "Crit Damage must equal 15.")
        self.assertIn(self.test_knight.get_damage(1), range(1,101),
                      "Damage must be in range: 5-10")

    def test_to_dict(self):
        self.assertEqual(dict, type(self.test_knight.to_dict()),'Type must be of type dictionary')