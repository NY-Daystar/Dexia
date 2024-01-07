import unittest
from models import Calendar, GrandPrix

class TestGrandPrix(unittest.TestCase):
    calendar: Calendar = Calendar()

    @classmethod
    def setUpClass(cls): ### run once before all test cases ###
        cls.calendar.add_grand_prix(GrandPrix(1, '1st Grand Prix', '2020-05-05'))
        cls.calendar.add_grand_prix(GrandPrix(2, '2nd Grand Prix', '2020-05-12'))
        cls.calendar.add_grand_prix(GrandPrix(3, '3rd Grand Prix', '2020-05-19'))
        cls.calendar.set_year(2020)
        cls.calendar.set_version(1)
    
    @classmethod
    def tearDownClass(cls):
        print('run once after all test cases')
    
    def setUp(self):
        print('run before each test case')
    
    def tearDown(self):
        print('run after each test case')
    
    def test_get_grand_prix_with_good_id(self):
        # Arrange
        id : int = 1

        # Act
        result: GrandPrix = self.calendar.get_grand_prix(id) 

        # Assert
        self.assertIsNotNone(result)

    def test_get_grand_prix_with_bad_id(self):
        # Arrange
        id : int = 10

        # Act
        result: GrandPrix = self.calendar.get_grand_prix(id) 

        # Assert
        self.assertIsNone(result)