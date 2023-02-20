#1/usr/bin/env python3
"""
 unittest for User class
"""

import os
import pycodestyle
import unittest
from models import user


class TestUserDocs(unittest.TestCase):
    """
    class to test docsting string of user module
    """

    def test_module_doctsring(self):
        """ test for doc string of module """
        self.assertTrue(user.__doc__ is not None,
                        'user module has no docstring')

    def test_user_class_doctstring(self):
        """ Tes for clas doctsring """
        self.assertTrue(user.User.__doc__ is not None,
                        'User class has no doctsring')
    def test_all_method_docs(self):
        """ test all method of User for docstring """
        for name in dir(user.User):
            attr = getattr(user.User, name)
            if callable(attr):
                self.assertTrue(attr.__doc__ is not None,
                                f"Method {name} has no doctring")

    def test_user_file_to_pep8(self):
        """ test the file if conforms to PEP8 """
        style = pycodestyle.StyleGuide(quite=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, result.messages)

    def test_file_is_executable(self):
        """ test if file is executable """
        filename = 'models/user.py'
        self.assertTrue(os.access(filename, os.X_OK))


if __name__ == '__main__':
    unittest.main()
