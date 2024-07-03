# 1. 동물원 관리하는 프로그램

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


    def sound(self):
        raise NotImplementedError("Subclass must implement this method")
    

    def __str__(self):
        return f"{self.name} the {self.species}"
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")


    def sound(self):
        return "왈!"
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")


    def sound(self):
        return "야옹~"

# Test cases
dog = Dog("Jindo")
cat = Cat("Odd-eye")

print(dog) # Jindo the dog
print(dog.sound()) # 왈!
print(cat) # Odd-eye the cat
print(cat.sound()) # 야옹~