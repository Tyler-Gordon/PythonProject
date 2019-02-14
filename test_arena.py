from unittest import TestCase
import inspect
from arena import Arena
from mage_character import MageCharacter
from knight_character import KnightCharacter

class TestArena(TestCase):

    def setUp(self):
        self.test_arena = Arena()
        self.test_mage = MageCharacter('Garry')
        self.test_knight = KnightCharacter('Joe')
        self.logPoint()

    def logPoint(self):
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in {} calling {}'.format(current_test, calling_function))
    
    def test_add_character(self):
        self.test_arena.add_character(self.test_mage)
        
        self.assertEqual(1, len(self.test_arena.get_all()), 'Must return 1')

    def test_get_character(self):
        self.test_arena.add_character(self.test_mage)

        self.assertEqual(self.test_mage,self.test_arena.get_character('Garry'),'Must return Garry')

    def test_get_all(self):

        self.test_arena.add_character(self.test_mage)
        self.assertEqual(1, len(self.test_arena.get_all()), 'Must return 1')

    def test_get_all_by_type(self):
        self.test_arena.add_character(self.test_mage)
        self.test_arena.add_character(self.test_knight)

        self.assertEqual(1, len(self.test_arena.get_all_by_type('Mage')), 'Must return 1')
        
    def test_update(self):
        self.test_arena.add_character(self.test_mage)
        self.test_new_garry = KnightCharacter('Garry')
        self.test_arena.update(self.test_new_garry)
        self.assertEqual(1, len(self.test_arena.get_all()), 'Must return 1')

    def test_delet(self):
        self.test_arena.add_character(self.test_mage)
        self.test_arena.add_character(self.test_knight)
        self.test_arena.delete(self.test_mage)
        self.assertEqual(1, len(self.test_arena.get_all()), 'Must return 1')
