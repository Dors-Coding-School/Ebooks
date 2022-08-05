class Vehicle:
 def __init__(self, name, mileage, capacity):
 self.name = name
 self.mileage = mileage
 self.capacity = capacity
 def fare(self):
 amount = super().fare()
 amount += amount * 10 / 100
 return amount
class Bus(Vehicle):
 pass
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
