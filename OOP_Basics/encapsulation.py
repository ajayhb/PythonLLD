class Movie:
    def __init__(self, title="", genre="", year=-1) -> None:
        self.__title = title
        self.__genre = genre
        self.__year = year
    
    # Below methods are called Getters, which help in obtaining 
    # the value of a private attribute, via this public method.
    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_year(self):
        return self.__year

    # Below methods are called Setters, which help in setting 
    # the value passed by the user, to the private variable, 
    # via these public methods
    def set_title(self, value):
        self.__title = value

    def set_genre(self, value):
        self.__genre = value

    def set_year(self, value):
        self.__year = value


    def get_details(self):
        print(
                f"Title: {self.get_title()} :: " 
                f"Genre: {self.get_genre()} :: "
                f"Year: {self.get_year()}"
            )

def main():
    movie = Movie("Forestt Grump", "Drama", 2013)
    print(movie.get_year())
    movie.set_year(2022)
    movie.get_details()

if __name__ == "__main__":
    main()