#!/usr/bin/python3
"""
Unit test for BaseModel class
"""

import unittest
import pycodestyle
from models import base_model

class TestBaseModelDocs(unittest.TestCase):
    """
    Class to test if the BaseModel module has a docstring.
    """

    def test_module_docstring(self):
        """
        Test if base_module has doctsring.
        """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_base_model_class_docstring(self):
        """
        Test if BaseModel class has docstring
        """
        self.assertTrue(len(base_model.BaseModel.__doc__) > 0)

    def test_all_function_docs(self):
        """ test if all method of class BaseModel are documented """
        for name in dir(base_model.BaseModel):
            attr = getattr(base_model.BaseModel, name)
            if callable(attr):
                self.assertTrue(attr.__doc__ is not None,
                                f"Method {name} has no doctstring")

    def test_base_model_conformance(self):
        """ Test that bas_model.py conforms to PEP8. """
        style = pycodestyle.StyleGuide(quite=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "found code style errors and (warning)")

if __name__ == '__main__':
    unittest.main()
