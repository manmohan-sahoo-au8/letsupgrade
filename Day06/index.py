'''
Question 1
A Barua number is a number that consists of only zeroes and ones and has only one 1. Barua’s
number will start with 1. Given numbers, find out the multiplication of the numbers. Note: The
input may contain one decimal number and all other Barua numbers. (Assume that each number
is the very large and the total number of values give is also very large)
Input 1: 100 10 12 1000
Output 1: 12000000
Input 2: 100 121 1000000000000000
Output 2: 12100000000000000000
Input 3: 10 100 1000
Output 3: 1000000
'''
'''
Question 2
Implement push, pop and find the minimum element in a stack in O(1) time complexity.
'''
class stack:
  min = float("inf")
  def __init__(self):
    self.min = float("inf")
    self.stack=[]
  def push(self,data):
    if data <= self.min:
      self.stack.append(self.min)
      self.min = data
    self.stack.append(data)
  def pop(self):
    data=self.stack[-1]
    if self.min == data:
      self.min = self.stack[-1]
      self.stack.pop()
  def top(self):
    return self.stack[-1]
  def getMin(self):
    return self.min
  def display(self):
    print("elements present in stack")
    for i in self.stack:
      print(i)

  

stack1=stack()
stack1.push(3)
stack1.push(5)
stack1.push(10)
stack1.push(30)
stack1.push(40)
print(stack1.getMin())



