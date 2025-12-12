
"""

import json
name = '{"name" : "john", "city" : "dubai"}'

x = json.loads(name)

print(x["name"])

class Myclass:
    x = 5

p1 = Myclass()
print(p1.x)
"""
 # OOPS

 
class car():  #class
    speed = 400
    wheels = 4
    airbags = 5
    mileage = 23.4

    def moveforward(self):
        print("car is moving forward")

    def backward(self):
        print("car is moving backward")


mustang = car() #objects or instance
mustang.speed = 490
print("mustang = ", mustang.speed)
print("mustang = ", mustang.mileage)
mustang.moveforward()

audi = car()
audi.speed = 299
print("audi = ", audi.speed)
print("audi = ", audi.mileage)
audi.backward()