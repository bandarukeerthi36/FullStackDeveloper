class Animal:
    def sounds(self):
        pass
class Dog(Animal):
    def sounds(self):
        print("Bow")
class Cat(Animal):
    def sounds(self):
        print("Meow")
for a in [Dog(),Cat()]:
    a.sounds()