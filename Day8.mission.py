#10.1
class Thing:
    pass

print(Thing)

example = Thing()
print(example) #different

#10.2
class Thing2:
    letters = 'abc'

print(Thing2.letters)

#10.3

class Thing3:
    def __init__(self):
        self.letters = 'xyz'

example = Thing3()
print(example.letters)
#Yes

#10.4

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen = Element('Hydrogen', 'H', 1)

#10.5
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

element_data = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**element_data)

#10.6
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print("name:", self.name)
        print("symbol:", self.symbol)
        print("number:", self.number)

element_data = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**element_data)

hydrogen.dump()

#10.7
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return "Element: name={0}, symbol={1}, number={2}".format(self.name, self.symbol, self.number)

element_data = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**element_data)

print(hydrogen)

#10.8
class Element:
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def number(self):
        return self._number

element_data = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**element_data)

print("Name:", hydrogen.name)
print("Symbol:", hydrogen.symbol)
print("Number:", hydrogen.number)

#10.9
class Bear:
    def eats(self):
        return "berries"

class Rabbit:
    def eats(self):
        return "clover"

class Octothorpe:
    def eats(self):
        return "campers"


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()


print("Rabbit eats:", rabbit.eats())
print("Octothorpe eats:", octothorpe.eats())

#10.10
class Laser:
    def does(self):
        return "disintegrate"

class Claw:
    def does(self):
        return "crush"

class SmartPhone:
    def does(self):
        return "ring"

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print("Laser does:", self.laser.does())
        print("Claw does:", self.claw.does())
        print("Smartphone does:", self.smartphone.does())


robot = Robot()


robot.does()
