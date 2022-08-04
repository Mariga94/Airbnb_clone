#!/usr/bin/python3
"""
Contains a class FileStorage that serializes instances to JSON file
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represents a file storage

    Attributes:
        __file_path (str):
        __objects (dict):
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionay of instatiated __objects"""
        if cls is not None:
            dictionary = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    dictionary[key] = value
                return dictionary
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key < obj class name>.id"""
        self.__objects["{}.{}".format(__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dictionary = {}
        for key in self.__objects:
            dictionary[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the
            JSON file (__file_path) exists; otherwise, do nothing.
        """

        try:
            with open(self.__file_path, "r", encoding="utf-8") as jsonfile:
                for obj in json.load(jsonfile).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(exec(name)(**obj))
        except Exception:
            pass
