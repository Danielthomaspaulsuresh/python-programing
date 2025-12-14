"""

class application():
    name =str("") 
    age = 0
    gender = str("")

danny  = application() 
danny.name = "danny"
print("danny's name = " , danny.name)
danny.age = 24
print("danny's age = " , danny.age)
danny.gender = "male"
print("danny's gender = ", danny.gender)



print(  
now we are gonna see the application of ragul 
      )




ragul = application()
ragul.name = "ragul"
print("ragul name = ", ragul.name)
ragul.age = 25
print("ragul age = ", ragul.age)
ragul.gender = "male"
print("ragul gender = ", ragul.gender)
    


class studentform:
    def __init__(self,name,age,gender,standard,marks):
        self.name = name
        self.age = age
        self.gender = gender
        self.standard = standard
        self.marks = marks

danny = studentform("danny",24,"male","12th standard",499)
ragul = studentform("ragul", 23,"male","10th standard",488)

print("
dannys information
")

print(danny.name)
print(danny.age)
print(danny.gender)
print(danny.standard)
print(danny.marks)

print("
raguls information
")

print(ragul.name)
print(ragul.age)
print(ragul.gender)
print(ragul.standard)
print(ragul.marks)
        
        
        
"""

class employee:
    def __init__(self,name,employee_id,department,salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary


emp_1 = employee("danny",101,"data science department", 10000000 )
emp_2 = employee("ragul",101,"cybersecurity departmenyt", 20000)       
        

print("""
danny employee detatils
"""
)
        
print("name = ",emp_1.name)
print("employee-id =",emp_1.employee_id)
print("department =", emp_1.department)
print("salary =",emp_1.salary)

print("""
ragul employee details
""")

print("name =" ,emp_2.name)
print("employee-id = ",emp_2.employee_id)
print("department =",emp_2.department)
print("salary = ",emp_2.salary)

class person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("hey hello ", self.name)
        
p1 = person("emil")
p1.greet()

class calculator():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    
calc = calculator()
print(calc.add(10, 40))
print(calc.sub(40, 20))


class car:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def move(self):
        print("drive")

class boat:
    def __init__(self,name,model):
        self.name =name
        self.model = model

    def move(self):
        print("sail")

class plane:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def move(self):
        print("fly")

cars = car("ford mustang", 1997)
boats = boat("suzuki", 2003)
planes = plane("boeing", 747)

for x in (cars,boats,planes):
    x.move()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
