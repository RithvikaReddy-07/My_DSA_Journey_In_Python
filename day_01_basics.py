#Topics Available:print statement, variables, datatypes

#example of print statement
a = 2
b = 6
c = a+b 

print("the sum of a+b is:", c)
print("Hello, Python!")

#example for assignment of variables
name = "Rithvika"
age =20
pi = 3.14

print(name, age, pi)

#examples of numeric datatypes (int, float, complex)
num1 = 10
num2 = 0.5
num3 = 2+3j

print(type(num1))
print(type(num2))
print(type(num3))

print(type(num1), type((num2)), type((num3)))

#examples of string datatype (str)
branch_name = "CSE C"

print(type(branch_name))
print("my branch name is:", branch_name)

#examples of sequence types (list, tuple, range)

#(1) list
my_list = [1,2,3,"munna"]
my_list.append(4)   #adding elements
print(my_list)

#(2) tuple
my_tuple = [1,2,3,"munna"]
print(my_tuple[1])  #access elements

#(3) range
r = range(1,10,2)
print(list(r))