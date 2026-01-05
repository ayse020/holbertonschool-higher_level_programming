#!/usr/bin/env python3
"""
Custom class serialization using pickle module
"""

import pickle


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle.
    
    Attributes:
        name (str): The name of the person
        age (int): The age of the person
        is_student (bool): Whether the person is a student
    """
    
    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize a CustomObject instance.
        
        Args:
            name: The name of the person
            age: The age of the person
            is_student: Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename: str) -> None:
        """
        Serialize the current instance to a file using pickle.
        
        Args:
            filename: The name of the file to save the serialized object to
        
        Returns:
            None. If an error occurs, returns None.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")
            return None
    
    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize a CustomObject instance from a file.
        
        Args:
            filename: The name of the file to load the object from
        
        Returns:
            CustomObject instance if successful, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                # Verify that the loaded object is of the correct type
                if isinstance(obj, cls):
                    return obj
                else:
                    print(f"Error: Loaded object is not a {cls.__name__}")
                    return None
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            return None
        except pickle.PickleError as e:
            print(f"Pickle error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
