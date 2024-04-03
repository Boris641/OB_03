class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} кушает")
    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Поёт")

class Mammal(Animal):
    def make_sound(self):
        print("Рычит")
class Reptile(Animal):
    def make_sound(self):
        print("Шипит")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal} Добавлено в зоопарк")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Cотрудник {new_staff} Добавлено в зоопарк")

class ZooKeeper():
    def feed_animal(self, animal):
        print(f"Сотрудник кормит {animal. name}")

class Veterinarian():
    def heal_animal(self, animal):
        print(f"Сотрудник лечит {animal. name}")

bird1 = Bird("Скворец","Два года")
mammal1 = Mammal("Тигр", "Пять лет")
reptile1 = Reptile("Кобра", "Десять лет")

zoo = Zoo()
zookeeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)
