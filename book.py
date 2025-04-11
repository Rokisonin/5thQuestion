from abc import ABC, abstractmethod

class Author:
    def __init__(self, name, nationality):
        self.__name = name
        self.__nationality = nationality

    @property
    def name(self):
        return self.__name

    @property
    def nationality(self):
        return self.__nationality

    def __str__(self):
        return f"{self.name} ({self.nationality})"

    def __eq__(self, other):
        return isinstance(other, Author) and self.name == other.name and self.nationality == other.nationality

class BaseBook(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Book(BaseBook):
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author  # Composition: Author object
        self.__year = year
        self.publisher = None

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    def get_details(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    @staticmethod
    def is_classic(year):
        return year < 1980

    def set_publisher(self, name, location):
        self.publisher = self.Publisher(name, location)

    def __str__(self):
        pub_info = f" | Published by: {self.publisher}" if self.publisher else ""
        return self.get_details() + pub_info

    def __repr__(self):
        return f"Book('{self.title}', {self.author}, {self.year})"

    class Publisher:
        def __init__(self, name, location):
            self.name = name
            self.location = location

        def __str__(self):
            return f"{self.name} ({self.location})"
