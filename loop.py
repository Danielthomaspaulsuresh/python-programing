
# forloop
"""
name = "danny"
for letters in name:
    print (letters)

"""
fruits = ["apple","banna","cherry","orange"]

for letter in fruits:
    print(letter)

name = "danny"

for i in name:

    if i == "n":
        continue
        print("n : is present")
        break
    else:
        print("its not present")
    print(i)

    #range

    for number in range(100, 500, 50):
        print(number)


for number in range(5,10):
    print(number)
    for i in range(2):
        print(i)
else:
    print("all numbers are finished")

# whlie loop

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("over")


#lambda

add_5 = lambda number : number + 10
print(add_5(10))