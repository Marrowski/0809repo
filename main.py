Завдання 1

class Book:
    def __init__(self, author: str, name: str, year: int, genre: str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.list_reviews = ['Good', 'Great', 'Masterpiece']

    def __str__(self):
        return f'Book name: {self.name}, book author: {self.author}, year of publishing:{self.year}, genre: {self.genre}'

    def __repr__(self):
        return f'Books with repr method: Name:{self.name!r}, author: {self.author!r},published: {self.year!r}, genre:{self.genre!r}'

#Завдання 2


class BookReview(Book):
    def add_review(self, review: Book):
        for review in self.list_reviews:
            print(self.list_reviews.append(review))



book1 = BookReview('Mario Puzo', 'The Godfather', 1935, 'Criminal drama')


#Завдання 4
class Automobile:
    def __init__(self, name: str, year: int, speed: int):
        self.name = name
        self.year = year
        self.speed = speed

    def __str__(self):
        return f'Name of car: {self.name}, year of manufaturing: {self.year}, speed: {self.speed}'


car1 = Automobile('Mazda', 2008, 240)
car2 = Automobile('Ford', 2012, 300)
car3 = Automobile('Suzuki', 2020, 320)
print(car1)


class Autoshop(Automobile):
    def automobiles(self):
        list_cars = [car1, car2, car3]
        while True:
            print(f'Available cars {list_cars}')
            sell = int(input('What car you would like to buy?'))
            if sell == 1:
                print(f'You sucessfully bought {car1}')
            elif sell == 2:
                print(f'You successfully bought {car2}')
            elif sell == 3:
                print(f'You successfully bouth {car3}')
            elif sell == 'exit'.lower():
                print('Goodbye!')
                break
            else:
                print('Unknown action. Try again')
                continue
            return list_cars


car4 = Autoshop(name= '', year = 0, speed = 0).automobiles()