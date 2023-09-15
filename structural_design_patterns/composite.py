from abc import ABC, abstractmethod

class StarWarsCinema(ABC):

    @abstractmethod
    def duration(self):
        pass

class Movie(StarWarsCinema):

    def __init__(self, name, duration):
        self.__name = name
        self.__duration = duration

    def duration(self):
        return self.__duration

class Block(StarWarsCinema):

    def __init__(self, name, content):
        self.__name = name
        self.__content = content

    def duration(self):
        return sum(element.duration() for element in self.__content)

if __name__ == '__main__':
    epIV = Movie("A New Hope", 121)
    epV = Movie("The Empire Strikes Back", 124)
    epVI = Movie("Return of the Jedi", 131)
    original_trilogy = Block('Original Trilogy', [epIV, epV, epVI])

    epI = Movie("The Phantom Menace", 136)
    epII = Movie("Attack of the Clones", 142)
    epIII = Movie("Revenge of the Sith", 140)
    prequel_trilogy = Block("Prequel Trilogy", [epI, epII, epIII])

    epVII = Movie("The Force Awakens", 138)
    epVIII = Movie("The Last Jedi", 152)
    epIX = Movie("The Rise of Skywalker", 142)
    sequel_trilogy = Block("Sequel Trilogy", [epVII, epVIII, epIX])

    trilogies = Block("Trilogies", [original_trilogy, prequel_trilogy, sequel_trilogy])

    movie1 = Movie("Rogue One", 133)
    movie2 = Movie("Solo: A Star Wars Story", 135)
    standalone_movies = Block("Standalone Movies", [movie1, movie2])

    extras = Block("Extras", [standalone_movies])

    star_wars = Block("Star Wars Universe", [trilogies, extras])
    print(f"Congratulations! You have enjoyed at least {star_wars.duration() // 60} hours of an iconic movie saga.")
