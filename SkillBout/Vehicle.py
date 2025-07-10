class Vehicle:
    def navigate(self):
        pass
class Car(Vehicle):
        def navigate(self):
            print("navigate via car")
class Bicycle(Vehicle):
    def navigate(self):
        print("navigate via bicycle")
for v in [Car(), Bicycle()]:
    v.navigate()
