#!/usr/bin/python3
"""
State class definition for MySQL database
This module defines the State class that maps to the 'states' table
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create a base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """
    State class representing a state in the database
    
    This class maps to the 'states' table in MySQL.
    
    Attributes:
        id (int): Auto-generated unique integer, primary key, cannot be null
        name (str): String with maximum 128 characters, cannot be null
    """
    
    # This specifies the name of the table in the database
    __tablename__ = 'states'
    
    # Define the id column
    id = Column(
        Integer,           # Column type is Integer
        primary_key=True,  # This column is the primary key
        autoincrement=True, # Value auto-increments for new rows
        nullable=False     # This column cannot be null
    )
    
    # Define the name column
    name = Column(
        String(128),      # Column type is String with max 128 characters
        nullable=False    # This column cannot be null
    )
