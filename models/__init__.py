#!/usr/bin/python3
"""
 create a unique FileStorage instance for this application
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel



storage = FileStorage()
storage.reload()
