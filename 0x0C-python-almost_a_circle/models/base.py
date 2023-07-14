#!/usr/bin/python3
"""
    import module json
"""
import json
import os
import csv


"""
    Base class file
"""


class Base:
    """
        base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            iniate the class Base
            args:
                id: an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            the JSON string representation of list_dictionaries
            args:
                list_dictionaries: list of dictionaries
            return: JSON string
        """
        lis = "[]"
        if list_dictionaries is None:
            return lis
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file
            args:
                list_objs: a list of instances who inherits of Base
        """
        list_dict = []
        str = ""

        if list_objs is None:
            list_objs = []
        for inst in list_objs:
            list_dict.append(inst.to_dictionary())

        str = cls.to_json_string(list_dict)

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as buf:
            buf.write(str)

    @staticmethod
    def from_json_string(json_string):
        """
            the list of the JSON string
            args:
                json_string:  a string representing a list of dictionaries
            return:
                the list
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            an instance with all attributes already set
            args:
                dictionary: can be thought of as a double pointer
                to a dictionary
            return:
                an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(2, 3)
        else:
            dummy_obj = cls(2)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """
            a list of instances by json file
            return:
                a list of instances
        """
        list_obj = []
        list_json = []
        if not os.path.exists(cls.__name__ + ".json"):
            return list_obj
        else:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as fo:
                list_json = cls.from_json_string(fo.read())

            for inst in list_json:
                list_obj.append(cls.create(**inst))
            return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            saves python object in CSV file
        """
        str = ""

        if list_objs is None:
            list_objs = []

        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as fd:
            if cls.__name__ == "Rectangle":
                str = ["id", "width", "height", "x", "y", "\0"]
            else:
                str = ["id", "size", "x", "y", "\0"]

            ldict = csv.DictWriter(fd, fieldnames=str)
            for attributes in list_objs:
                ldict.writerow(attributes.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
            CSV file to python
        """
        list_pyt = []
        if not os.path.exists(cls.__name__ + ".csv"):
            return list_pyt
        else:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as fd:
                for line in csv.reader(fd):
                    print(line)
                    if cls.__name__ == "Rectangle":
                        header = {
                                "id": int(line[0]),
                                "width": int(line[1]),
                                "height": int(line[2]),
                                "x": int(line[3]),
                                "y": int(line[4])
                        }
                    else:
                        header = {
                                "id": int(line[0]),
                                "size": int(line[1]),
                                "x": int(line[2]),
                                "y": int(line[3])
                        }
                    attributes = cls.create(**header)
                    list_pyt.append(attributes)
        return list_pyt
