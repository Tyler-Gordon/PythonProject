from unittest import TestCase
import inspect
from arena import Arena
from mage_character import MageCharacter
from knight_character import KnightCharacter

class TestArena(TestCase):

    def setUp(self):
        self.test_arena = Arena('arena.json')
        self.test_mage = MageCharacter('Tyler',10000,100,100,10)
        self.test_knight = KnightCharacter('Connor',10000,100,100,10)
        self.test_arena._overwrite_json()
        self.logPoint()

    def logPoint(self):
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in {} calling {}'.format(current_test, calling_function))
    
    def test_add_character(self):
        self.test_arena._overwrite_json()
        self.test_arena.add_character(self.test_mage)

        self.assertEqual(1, len(self.test_arena.get_all()), 'Must return 1')
        # cant really test the id since its randomly assigned???

    def test_get_character(self):
        self.test_arena._overwrite_json()
        self.test_arena.add_character(self.test_mage)
        self.assertIsInstance(self.test_mage, MageCharacter,'Must be instance of Mage')

    def test_get_all(self):
        self.test_arena._overwrite_json()
        self.test_arena.add_character(self.test_mage)
        self.assertEqual(3, len(self.test_arena.get_all()), 'Must return 3')

    def test_get_all_by_type(self):
        self.test_arena._overwrite_json()
        self.test_arena.add_character(self.test_mage)
        self.test_arena.add_character(self.test_knight)

        self.assertEqual(3, len(self.test_arena.get_all_by_type('mage')), 'Must return 3')
        
    def test_update(self):
        self.test_arena._overwrite_json()
        self.test_arena.add_character(self.test_mage)
        self.test_new_garry = KnightCharacter('Connor',10000,100,100,10)
        self.test_arena.update(self.test_new_garry)
        self.assertEqual(1, len(self.test_arena.get_all()), 'Must return 1')

    def test_delete(self):
        self.test_arena._overwrite_json()
        self.test_arena.add_character(self.test_mage)
        self.test_arena.add_character(self.test_knight)
        self.test_arena.delete(self.test_mage.get_id())
        self.assertEqual(2, len(self.test_arena.get_all()), 'Must return 2')

    def test_write_characters_to_file(self):
        self.test_arena._overwrite_json()
        self.test_arena.add_character(self.test_mage)
        self.test_arena.add_character(self.test_knight)
        self.assertEqual(3, len(self.test_arena.get_all()), 'Must return 27')


    def test_read_characters_from_file(self):
        pass
