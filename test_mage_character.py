from unittest import TestCase
import inspect
from mage_character import MageCharacter

class TestMageCharacter(TestCase):

    def setUp(self):
        """ Creates a test_mage instance and logs the test.
        """
        self.test_mage = MageCharacter('Tyler',10000,100,100,10,10,10,10)
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

    def test_get_damage(self):
        """ Test that spell damage works if 19 or 20 is rolled.
            Test that the normal damage range is returned otherwise.
        """
        self.assertEqual(110, self.test_mage.get_damage(10),
                        "Spell Damage must equal 110.")           

    def test_to_dict(self):
        self.assertEqual(dict, type(self.test_mage.to_dict()),'Type must be of type dictionary')