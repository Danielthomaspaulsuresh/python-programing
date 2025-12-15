#read
"""
file = open('text.txt', 'r')
print(file.read())
#print(file.readline())
#print(file.readline())

#print(file.readlines())
file.close()


# write


file = open('text.txt', 'w')
file.write("hello this id danny fromcoimbatore")

file.close()

#uppend


file = open('text.txt', 'a')
file.write("now i am studying in charles darwin university")
lst = ['hey everyone', 'how is your day']
file.writelines(lst)
file.close()

"""
file = open('text.txt','r')
print(file.read())
print(file.tell())
file.seek(0)
print(file.read())
file.close()