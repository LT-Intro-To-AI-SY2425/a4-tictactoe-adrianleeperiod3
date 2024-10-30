# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n = "?", a = 0):
        self.name = n
        self.age = a

    def __str__(self):
        s = f"{self.name} is {self.age} years old."
        return s

logan = Dog("Logan", 8)
airbud = Dog("Airbud", 24)
roger = Dog()

print(logan)
print(airbud)
print(roger)
