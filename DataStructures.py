from random import setstate

# lists
employees = ["Sylvia" , "Kathoni", "Tom" , 'Sylvia']
print(employees)
print(employees[0])
employees.append('susan')
print(employees)
# append is an addittion to the list
# employees.insert( _index:2 ,_object:"joseph")
# print(employees)
# tuples
languages = ('Python', 'java' , 'Koltin')
print(languages)
print(languages[1])
print(languages[1:4])
marks = (234 ,234, 564 , 765)
print(marks)
print(max(marks))
print(min(marks))
print(sum(marks))


# sets
students = {'john' , 'Ann', 'Carol' , 'Jovial'}
print(students)
if 'Jovial' in students:
    print('Jovial is Present')
else:
    print('Jovial is not Present')
students.add("Vivian")
print(students)
students.remove("Vivian")
print(students)
students.update("Marsai","Alex")
print(students)
# dictionary
Accesories ={
    'Jewelery':'Necklaces',
    'Skin care':'Gannier products',
    'Clothing':'Jorts',
    'Other':'Perfumes'
}
print(Accesories)
print(Accesories['Skin care'])
print(Accesories['Other'])
if Accesories['Skin care']:
    print("exist")
else:
    print("not  available")

#2nd query
input1 = bool(int(input("Enter first input (1 for True, 0 for False): ")))
input2 = bool(int(input("Enter second input (1 for True, 0 for False): ")))
input3 = bool(int(input("Enter third input (1 for True, 0 for False): ")))
input4 = bool(int(input("Enter fourth input (1 for True, 0 for False): ")))


result = input1 and input2 and input3 and input4

if result:
    print("All inputs are True (1).")
else:
    print("At least one input is False (0).")

# ctrl+/ creates a comment