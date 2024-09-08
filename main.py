#Завдання 1

class Book:
    def __init__(self, author: str, name: str, year: int, genre: str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __str__(self):
        return f'Book name: {self.name}, book author: {self.author}, year of publishing: {self.year}, genre: {self.genre}'

    def __repr__(self):
        return f'Books with repr method: Name:{self.name!r}, author: {self.author!r}, published: {self.year!r}, genre:{self.genre!r}'


book1 = Book('Mario Puzo', 'The Godfather', 1936,'Drama')
book2 = Book('Andzhei Sapkowski', 'The Witcher', 2005, 'Adventure')
book3 = Book('Arthur Conan Doyle', 'Scherlock Holmes', 1887, 'Detective')

print(str(book1))
print(repr(book1))
