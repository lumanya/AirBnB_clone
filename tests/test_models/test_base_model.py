#!/usr/bin/python3
"""
Unit test for BaseModel class
"""

import os
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
        self.assertEqual(result.total_errors, 0, result.messages)

    def test_file_is_executable(self):
        """ test if the file is exceutable  using os.access() function with
        the os.X_OK flag.
        `chmod +x my_script.py`
        that command set the execute bit on the file, so when check if a file
        is excutable wwe are essentially checking if the exceute bit is set on
        the file
        """
        filename="models/base_model.py"
        self.assertTrue(os.access(filename, os.X_OK))

class TestBaseModelInstances(unittest.TestCase):
    """ testing for class instances """
    def setUp(self):
        """ initilizes new BaseModel instance for testing """
        self.model = base_model.BaseModel()

    def test_instation(self):
        """ check if BaseModel is properly instatied """
        self.assertIsInstance(self.model, base_model.BaseModel)

if __name__ == '__main__':
    unittest.main()
