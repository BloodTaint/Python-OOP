from project.movie_specification.movie import Movie


class Thriller(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value: int):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value

    # If no age restriction is given, it should be set to 16 (years).
    # If the age restriction is less than 16, raise a ValueError with the message
    # "Thriller movies must be restricted for audience under 16 years!"

    def details(self):
        pass
        # return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner}"
