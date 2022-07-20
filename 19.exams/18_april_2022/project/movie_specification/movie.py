import abc

from project.user import User


class Movie(abc.ABC):
    @abc.abstractmethod
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        # The movie is unsuitable for people under the given age.
        # The age restriction value depends on the movie genre.
        self.likes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        if value.strip() == "":
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value: User):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value
        # owner: User
        # A user object that represents the one who made the movie
        # If the owner is NOT an object of type User, raise a ValueError with the message
        # "The owner must be an object of type User!"

    def details(self):
        pass
    # It returns a string with information about the movie by its type.