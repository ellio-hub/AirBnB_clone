#!/usr/bin/python3
"""
    module that contain the class
    that defines all common
    attributes/methods for other classes
"""
import uuid
import datetime


class BaseModel:
    """
    class
    that defines all common
    attributes/methods for other classes
    """
    def __init__(self):
        """
        init method to assign instance
        attributes when an instance is created
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        print method
        should print in this format:
                    [<class name>] (<self.id>) <self.__dict__>
        """
        x = ("[{}] ({}) {}".format(self.__class__.__name__,
                                   self.id, self.__dict__))
        return x

    def save(self):
        """
        method to update "update_at" attribute
        when an update to the instances occures
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        method that return a dictionary
        containing all keys/values of __dict__
        of the instance
        """
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
