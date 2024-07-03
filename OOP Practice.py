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



# 2. 간단한 은행 시스템 구현하기

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self.balance
    

    def withdraw(self, amount):
        if amount > self.balance:
            return "잔고를 확인해주세요."
        self.balance -= amount
        return self. balance
    

    def __str__(self):
        return f"성함: {self.owner}\n잔고: {self.balance}"
    

# Test Cases
    
HT = Account("Hantaek", 100)
print(HT)                   # 성함: Hantaek \n잔고: 100
print(HT.deposit(50))       # 150
print(HT.withdraw(80))      # 70
print(HT.withdraw(80))      # 잔고를 확인해주세요.



# 3. Apply Inheritance and Polymorphism to interest rate 상속과 다형성을 이용해서 계좌에 이자 붙이기

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance
    

# Test Cases
    
savings = SavingsAccount("Hantaek", 500)
print(savings)                              # 성함: Hantaek \n잔고: 500
print(savings.apply_interest())             # 510