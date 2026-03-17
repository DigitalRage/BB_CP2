# BB 1st Classes Notes

#example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age
    
    def __str__(self): 
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}"

    def birthday(self):
        self.age += 1

dog = Animal("Doug", "Dog", 4)
bunny = Animal("Judy", "Rabbit", 20)
print(dog)
print(bunny)
dog.birthday()
print(dog)

# Example 2
class ClassPeriod:
    def __init__(self, subject, teacher = "Ms. LaRose", room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher.capitalize()
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}"
    
first = ClassPeriod("Computer Programming 2", "Ms. LaRose", 200)
second = ClassPeriod("Computer Programming 2", "Ms. LaRose", 200)
third = ClassPeriod("Computer Science Principles", "Ms. LaRose", 200)
sixth = ClassPeriod("English 8", "Ms. Jensen", 216)
print(first, second, third, sixth, sep="\n\n")