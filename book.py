from abc import ABC, abstractmethod

# Author class — composed inside Book (Composition)
class Author:
    def __init__(self, name, nationality):
        # Encapsulated private attributes
        self.__name = name
        self.__nationality = nationality

    @property
    def name(self):
        return self.__name

    @property
    def nationality(self):
        return self.__nationality

    def __str__(self):
        # String representation of the author
        return f"{self.name} ({self.nationality})"

    def __eq__(self, other):
        # Equality check between authors based on name and nationality
        return isinstance(other, Author) and self.name == other.name and self.nationality == other.nationality

# Abstract base class to enforce implementation of get_details() in subclasses
class BaseBook(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Book class inherits from BaseBook and uses Author (composition)
class Book(BaseBook):
    def __init__(self, title, author, year):
        # Private attributes
        self.__title = title
        self.__author = author      # Composition: uses Author instance
        self.__year = year
        self.publisher = None       # Will be set using nested class later

    # Getter for title
    @property
    def title(self):
        return self.__title

    # Getter for author
    @property
    def author(self):
        return self.__author

    # Getter for year
    @property
    def year(self):
        return self.__year

    # Implementation of abstract method from BaseBook
    def get_details(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    # Static method — logic that doesn’t depend on a specific instance
    @staticmethod
    def is_classic(year):
        return year < 1980

    # Composition with nested Publisher class
    def set_publisher(self, name, location):
        self.publisher = self.Publisher(name, location)

    # Custom string representation of a Book
    def __str__(self):
        pub_info = f" | Published by: {self.publisher}" if self.publisher else ""
        return self.get_details() + pub_info

    # Debug representation
    def __repr__(self):
        return f"Book('{self.title}', {self.author}, {self.year})"

    # Nested class: Publisher (Composition inside Book)
    class Publisher:
        def __init__(self, name, location):
            self.name = name
            self.location = location

        def __str__(self):
            return f"{self.name} ({self.location})"
