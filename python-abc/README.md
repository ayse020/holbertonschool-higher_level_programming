# Python - Abstract Classes and Interfaces

## Project Description
This project focuses on implementing Object-Oriented Programming (OOP) concepts in Python, specifically abstract classes, interfaces, and inheritance patterns.

## Learning Objectives
- Understand and implement Abstract Base Classes (ABCs)
- Apply duck typing and interface concepts
- Extend standard Python classes
- Implement method overriding
- Work with multiple inheritance and mixins

## Tasks

### Task 0: Abstract Animal Class and its Subclasses
**File:** `task_00_abc.py`

**Description:**
Create an abstract class `Animal` using Python's ABC module with an abstract method `sound()`. Then create two subclasses `Dog` and `Cat` that implement the `sound()` method.

**Requirements:**
- Import `ABC` and `abstractmethod` from the `abc` module
- Create an abstract class `Animal` that inherits from `ABC`
- Define an abstract method `sound()` using `@abstractmethod` decorator
- Create `Dog` class that inherits from `Animal` and implements `sound()` to return "Bark"
- Create `Cat` class that inherits from `Animal` and implements `sound()` to return "Meow"

**Expected Behavior:**
- Instances of `Dog` and `Cat` can be created
- Calling `sound()` on a `Dog` instance returns "Bark"
- Calling `sound()` on a `Cat` instance returns "Meow"
- Trying to create an instance of `Animal` raises a `TypeError`

**Example Usage:**
```python
from task_00_abc import Dog, Cat

dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
