import random
import time


class Pet:

    def __init__(self, name, hunger: int = 2, happiness: int = 5, energy: int = 5):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def feed(self):
        if self.hunger > 1:
            self.hunger -= 2
            self.energy = self.energy + random.randint(-1, 0)
            print(f"{self.name} is eating...")
            time.sleep(1)
        else:
            print(f"{self.name} is full. Do smth else.")
        self.check_status()

    def play(self):
        if self.energy >= 2:
            self.hunger += 1
            self.happiness += 3
            print(f"{self.name} is playing...")
            time.sleep(1)
        else:
            print(f"{self.name} is exhausted. It need to recover it's energy.")
        self.check_status()

    def sleep(self):
        if self.energy <= 7:
            self.energy = 10
            self.happiness -= 2
            self.hunger += 1
            print(f"{self.name} is sleeping... ", end='')
            time.sleep(1)
            print(f"Now {self.name} is full of energy!")
        else:
            print(f"{self.name} isn't exhausted. ")
        self.check_status()


    def status(self):
        print(f"{self.name}'s status:")
        print(f"- {self.hunger}/10 hunger")
        print(f"- {self.happiness}/10 happiness")
        print(f"- {self.energy}/10 energy")

    def check_status(self):
        if self.hunger >= 10:
            print(f"The {self.name} is sick.")
        if self.happiness <= 0:
            print(f"The {self.name} is sad.")
        if self.energy <= 0:
            print(f"The {self.name} is exhausted. It's need to take a rest.")
        if self.hunger > 10:
            self.hunger = 10
        if self.happiness > 10:
            self.happiness = 10
        if self.energy > 10:
            self.energy = 10


pet = Pet("Fufa")
pet.status()
pet.feed()
pet.status()
pet.feed()
pet.status()
pet.feed()
pet.status()