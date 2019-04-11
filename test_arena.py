from unittest import TestCase
import inspect
from arena import Arena
from mage_character import MageCharacter
from knight_character import KnightCharacter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import os
try:
    os.remove('characters.sqlite')
except:
    print('Database did not exist... creating')
import create_tables
class TestArena(TestCase):

    def setUp(self):
        self.test_arena = Arena('characters.sqlite')
        self.test_mage = MageCharacter('Tyler',10000,100,100,10,'mage',10,10)
        self.test_knight = KnightCharacter('Connor',10000,100,100,10,'knight',10,10,10)
        self.logPoint()

    def logPoint(self):
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in {} calling {}'.format(current_test, calling_function))

    def test_add_character(self):
        self.test_arena.add_character(self.test_mage)

        self.assertEqual(1, len(self.test_arena.get_all()), 'Must return 1')
        # cant really test the id since its randomly assigned???

    def test_get_character(self):
        self.test_arena.add_character(self.test_mage)
        self.assertIsInstance(self.test_mage, MageCharacter,'Must be instance of Mage')

    def test_get_all(self):
        self.test_arena.add_character(self.test_mage)
        self.assertEqual(3, len(self.test_arena.get_all()), 'Must return 3')

    def test_get_all_by_type(self):
        self.test_arena.add_character(self.test_mage)
        self.test_arena.add_character(self.test_knight)

        self.assertEqual(3, len(self.test_arena.get_all_by_type('mage')), 'Must return 3')
        
    def test_update(self):
        self.test_arena.add_character(self.test_knight)
        self.test_new_connor = KnightCharacter('Connor',900,100,100,10,'knight',10,10,10)
        self.test_new_connor.id = 3
        #print(self.test_new_connor.username,self.test_new_connor.id)
        self.test_arena.update_character(self.test_new_connor)
        self.assertEqual(7, len(self.test_arena.get_all()), 'Must return 1')

    def test_delete(self):
        self.test_arena.add_character(self.test_mage)
        self.test_arena.add_character(self.test_knight)
        self.test_arena.delete_character(self.test_mage.get_id())
        self.assertEqual(2, len(self.test_arena.get_all()), 'Must return 2')