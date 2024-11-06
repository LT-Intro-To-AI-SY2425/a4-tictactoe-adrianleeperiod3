# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    species = "canis familiaris"
    fetch_count = 0

    def __init__(self, n = "?", a = 0):
        self.name = n
        self.age = a

    def __str__(self):
        s = f"{self.name} is {self.age} years old."
        return s
    
    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch

    def fetch_reset(self):
        self.fetch_count = 0

logan = Dog("Logan", 8)
airbud = Dog("Airbud", 24)
roger = Dog()

print(logan.fetch_count)
logan.play_fetch(8)
print(logan.fetch_count)
logan.fetch_reset()
print(logan.fetch_count)

