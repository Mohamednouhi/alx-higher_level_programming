#!/usr/bin/python3
"""Module for Base class and JSON operations"""

import json

class Base:
    """Base class for managing instances."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance.

        Args:
            id (int): ID of the new instance.
        """
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        l_o = "[]"
        filename = str(cls.__name__) + ".json"
        if list_objs is not None:
            l_o = cls.to_json_string([ob.to_dictionary() for ob in list_objs])
        with open(filename, 'w') as f:
            f.write(l_o)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        str_list = []
        if json_string is not None and len(json_string) > 0:
            str_list = json.loads(json_string)
        return str_list

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file."""
        filename = str(cls.__name__) + ".json"
        dict_list = []
        try:
            with open(filename, 'r') as file:
                data_str = file.read()
                str_list = cls.from_json_string(data_str)
                for dictionary in str_list:
                    dict_list.append(cls.create(**dictionary))
                return dict_list
        except FileNotFoundError:
            return dict_list

