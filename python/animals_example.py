class Animal:
    def __init__(self):
        self.fur = True

    def make_sound(self):
        return '{}!'.format(self.sound)


class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__()
        self.name = name
        self.sound = sound


class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__()
        self.name = name
        self.sound = sound

c = Cat('Tigernice', 'Meow')
d = Cat('SomeCoolName', 'Bork')

print(c.make_sound())
print(d.make_sound())
print(c.fur)
