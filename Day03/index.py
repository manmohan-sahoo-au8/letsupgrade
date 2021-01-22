'''
Question 1
Write a Python program to add two numbers using class and object.
(Take both numbers as input from the user)
'''
class Add:
  def add_numbers(self,a,b):
    sum1 = a+b
    return sum1

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

A = Add()
sum1 = A.add_numbers(a,b)
print(sum1)

'''
Question 2
Define a function swap that should swap two values and print the swapped variables outside the
swap function.
'''
def swap(x,y):
  a=x
  x=y
  y=a

  return x,y

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

x,y = swap(x,y)

print((x,y))