#!/usr/bin/python3
"""
 file_storage
"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel



class FileStorage:
    """
     FileStorage
    """
 

    __file_path = "/home/shaibu/Desktop/AirBnB_clone/file.json"
    __objects = {}


    def all(self):
        """ return dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with <obj class name>.id """
        """key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj"""
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file(path: __file_path)"""
        """new_dict = {}
        for obj_id, objs in FileStorage.__objects.items():
            new_dict[obj_id] = objs.to_dict()"""
        new_dict = {}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            for key, obj in FileStorage.__objects.items():
                new_dict[key] = obj.to_dict()
           
            json.dump(new_dict, fname)

    def reload(self):
        """deserializes the JSON file to __objets (only if the JSOn file
          (__file_path) exists; otherwise, do nothing, if the file does not
         exists, no exception should be raise"""
        #FileStorage.__objects = {}
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dict = json.load(f)
        except:
            return
        for key, value in dict.items():
            cls = value["__class__"]
            FileStorage.__objects[key] = eval(cls)(**value)
