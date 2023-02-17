#!/usr/bin/env python3

"""
 unittest for FileStorage class
"""
import os
import pycodestyle
import unittest
from models.engine import file_storage


class TestFilestorageDpocs(unittest.TestCase):
    """
    class to test docstring of Filestorage model
    """

    def test_module_docstring(self):
        """ test doc string of module"""
        self.assertTrue(file_storage.__doc__ is not None,
                        "file_storage module has no doctsring")

    def test_file_storage_class_docstring(self):
        """ test doc string of FileStorage class """
        self.assertTrue(file_storage.FileStorage.__doc__ is not None,
                        "FileStorage class has no docstring")

    def test_all_method_docs(self):
        """ test if all method of FileStorage class have docstring """
        for name in dir(file_storage.FileStorage):
            attr = getattr(file_storage.FileStorage, name)
            if callable(attr):
                self.assertTrue(attr.__doc__ is not None,
                                f"Method {name} has no doctsing")

    def test_file_storage_to_pep8(self):
        """ test that file_storage.py conforms to PEP8 """
        style = pycodestyle.StyleGuide(quite=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, result.messages)

    def test_file_is_executable(self):
        """ test if file is executable"""
        filename = "models/engine/file_storage.py"
        self.assertTrue(os.access(filename, os.X_OK))

if __name__ == '__main__':
    unittest.main()
