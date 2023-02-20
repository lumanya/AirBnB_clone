#1/usr/bin/env python3
"""
 unittest for Review class
"""

import os
import pycodestyle
import unittest
from models import review


class TestUserDocs(unittest.TestCase):
    """
    class to test docsting string of review module
    """

    def test_module_doctsring(self):
        """ test for doc string of module """
        self.assertTrue(review.__doc__ is not None,
                        'user module has no docstring')

    def test_user_class_doctstring(self):
        """ Tes for clas doctsring """
        self.assertTrue(review.Review.__doc__ is not None,
                        'Review class has no doctsring')
    def test_all_method_docs(self):
        """ test all method of User for docstring """
        for name in dir(review.Review):
            attr = getattr(review.Review, name)
            if callable(attr):
                self.assertTrue(attr.__doc__ is not None,
                                f"Method {name} has no doctring")

    def test_user_file_to_pep8(self):
        """ test the file if conforms to PEP8 """
        style = pycodestyle.StyleGuide(quite=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, result.messages)

    def test_file_is_executable(self):
        """ test if file is executable """
        filename = 'models/review.py'
        self.assertTrue(os.access(filename, os.X_OK))


if __name__ == '__main__':
    unittest.main()
