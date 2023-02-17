#!/usr/bin/python3
"""
Unit test for BaseModel class
"""

import os
import unittest
import pycodestyle
from models import base_model
from datetime import datetime


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

    def test_str(self):
        """ test for __str__ method if it returns
        [<class name>] (<self.id>) <self.__dict__>
        """
        expected_str = "[BaseModel] ({}) {}".format(self.model.id,
                                                    self.model.__dict__)
        self.assertEqual(expected_str, str(self.model))

    def test_to_dict(self):
        """ test to to_dict if it returns dictionary that contains
        id, created_at, updated_at and __class__
        """
        base_dict = self.model.to_dict()

        self.assertTrue(isinstance(base_dict, dict))
        self.assertTrue('id' in base_dict)
        self.assertTrue('created_at' in base_dict)
        self.assertTrue('updated_at' in base_dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')

        self.assertTrue(isinstance(base_dict['updated_at'], str),
                        "updated_at attr is not string")
        self.assertTrue(isinstance(base_dict['created_at'], str),
                        "created_at attribute is notstring")

    def test_save_method_updates_updated_at_attributes(self):
        """ test on save method if it update updated_at attributes """
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at,
                            "save method didnt update updated_at")

    def test_attributes_instatied(self):
        """ Test if attributes are propery instatieted in BaseModel """
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

        self.assertEqual(type(self.model.id), str)
        self.assertEqual(type(self.model.created_at), datetime)
        self.assertEqual(type(self.model.updated_at), datetime)

if __name__ == '__main__':
    unittest.main()
