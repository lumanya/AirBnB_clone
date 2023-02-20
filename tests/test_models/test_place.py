#1/usr/bin/env python3
"""
 unittest for Place class
"""

import os
import pycodestyle
import unittest
from models import place


class TestUserDocs(unittest.TestCase):
    """
    class to test docsting string of place module
    """

    def test_module_doctsring(self):
        """ test for doc string of module """
        self.assertTrue(place.__doc__ is not None,
                        'place module has no docstring')

    def test_user_class_doctstring(self):
        """ Tes for clas doctsring """
        self.assertTrue(place.Place.__doc__ is not None,
                        'Place class has no doctsring')
    def test_all_method_docs(self):
        """ test all method of Place for docstring """
        for name in dir(place.Place):
            attr = getattr(place.Place, name)
            if callable(attr):
                self.assertTrue(attr.__doc__ is not None,
                                f"Method {name} has no doctring")

    def test_user_file_to_pep8(self):
        """ test the file if conforms to PEP8 """
        style = pycodestyle.StyleGuide(quite=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, result.messages)

    def test_file_is_executable(self):
        """ test if file is executable """
        filename = 'models/place.py'
        self.assertTrue(os.access(filename, os.X_OK))


if __name__ == '__main__':
    unittest.main()
