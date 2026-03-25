# Class Relationship Notes

# Inheritance "is a"
# Parent Class
class Vehical: 
    def __init__(self, model, brand): 
        self.model = model
        self.brand = brand

    def move(self): 
        print("Move!")
    
# Children Class
class Car(Vehical):
    pass

class Boat(Vehical): 
    def move(self): 
        print("Sail!")

class Plane(Vehical): 
    def move(self): 
        print("Fly!")
        
car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

car.move()
boat.move()
plane.move()


#Aggrehation "has a"
class Library:
    def __init__(self, name, catalog = []): 
        self.name = name
        self.catalog = catalog

    def add_book(self, book): 
        self.catalog.append(book)
    
    def revove_book(self, book): 
        if book in self.catalog: 
            self.catalog.pop(book)
        else: 
            print("That book isn't in the library!")

    def view_catalog(self): 
        for book in self.catalog: 
            print(book)

class Book: 
    def __init__(self, title, author): 
        self.title = title.title()
        self.author = author

    def __str__(self): 
        return f"{self.title} by {self.author}"


lib = Library("Provo Library")

lib.add_book(Book("Way of Kings", "Brandon Sanderson"))
lib.add_book(Book("Fellowship of the Ring", "J.J.R. Tolkien"))
lib.add_book(Book("The Last Battle", "C.S. Lewis"))

lib.view_catalog()
