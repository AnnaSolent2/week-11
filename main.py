from inhabitant import Inhabitant

class Human(Inhabitant):

  def __init__(self, name="Human", age=0):
    super().__init__(name, age)
  
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

  def display(self):
    print(f"I am {self.name}")


if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))
  human.eat(20)
  print(repr(human))

from inhabitant import Inhabitant

class Robot(Inhabitant):

  # class attribute
  laws = "Protect, Obey and Survive"

  # A static method
  @staticmethod
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name="Robot", age=0):
    super().__init__(name, age)

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'
  
  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  robot = Robot()
  Robot.the_laws()
  print(repr(robot))
  robot.move(10)
  print(repr(robot))
  robot.eat(5)
  print(repr(robot))
  robot.eat(20)
  print(repr(robot))

from inhabitant import Inhabitant

class Alien(Inhabitant):

  def __init__(self):
    self.technology = []

  def __str__(self):
    return f"Alien has: {self.technology}."

  def __repr__(self):
    return f"alien(technology={self.technology})"

  def pickup(self, tech):
    self.technology.append(tech)

  def drop(self, tech):
    self.technology.remove(tech)


if __name__ == "__main__":
  alien = Alien()
  print(repr(alien))

from abc import ABC

class Inhabitant(ABC):

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0):
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY

  def grow(self):
    self.age += 1

  def eat(self, amount):
    potential_energy = self.energy + amount
    if (potential_energy > Inhabitant.MAX_ENERGY):
      self.energy = Inhabitant.MAX_ENERGY
      return potential_energy - self.energy
    else:
      self.energy = potential_energy
      return 0

  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
      self.energy = potential_energy
      return 0

from human import Human
from robot import Robot

class Planet:

  def __init__(self):
    self.inhabitants = []

  def __repr__(self):
    return f"planet(inhabitants={self.inhabitants})"

  def __str__(self):
    return f"This planet has {len(self.inhabitants)} inhabitants."

  def add(self, inhabitant):
    self.inhabitants.append(inhabitant)

  def remove(self, inhabitant):
    self.inhabitants.remove(inhabitant)

if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))
  prins = Human("Prins")
  planet.add(prins)
  print(repr(planet))
  print(planet)

