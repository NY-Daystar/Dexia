import unittest
from scraper import uploader
from helper import path_combine

class TestUpload(unittest.TestCase):

    def test_get_version_from_document_expected_valid_version(self):
        # Arrange
        expected: int  = 5
        path: str = path_combine('tests', 'samples', 'calendar_with_version.json')
        
        # Act
        result = uploader.get_version(path) 

        # Assert
        self.assertEqual(result, expected, "not the same version")

    def test_get_version_from_document_expected_invalid_version(self):
        '''by default version with number 1 has to be returned'''
        # Arrange
        expected: int = 1
        path: str = path_combine('tests', 'samples', 'calendar_without_version.json')

        # Act
        result = uploader.get_version(path) 

        # Assert
        self.assertEqual(result, expected, "not the same version")