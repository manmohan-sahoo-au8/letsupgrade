'''
Question 1
Write a Python program to print even numbers in a list.
Sample:
Input: list1 = [12, 3, 55, 6, 144]
Output: [12, 6, 144]
Input: list2 = [2, 10, 9, 37]
Output: [2, 10]
'''
list1=[12,3,55,6,144] 
even_numbers = [i for i in list1 if i%2 ==0]
print(even_numbers)


'''
Question 2
Write a program to print the following pattern
1
22
333
4444
55555
'''
for i in range(1,6):
  print(str(i)*i)
