'''
Question 1
Implement deletion operation from the end of the linked list and Insertion operation from the
beginning of the linked list
'''
class Node:
  def __init__(self,item):
    self.item = item
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert_at_begin(self,data):
    node = Node(data)

    node.next = self.head
    self.head = node
  

  def print_list(self):
    temp_node = self.head
    while(temp_node):
      print(str(temp_node.item),end="")
      temp_node = temp_node.next
    
llist = LinkedList()
llist.insert_at_begin(5)
llist.insert_at_begin(8)
llist.insert_at_begin(6)
llist.insert_at_begin(7)
llist.print_list()


'''
Question 2
Implement binary search using python language.
(Write a function which returns the index of x in given array arr if present, else returns -1)
'''
def binary_search(arr,x):
  l = 0
  m = len(arr)-1
  n = 0

  while m >= l:
    n = (m+l)//2

    if arr[n] < x:
      l = n+1
    
    elif arr[n] > x :
      m = n-1
    
    else:
      return n
  return -1

arr = [25,55,87,98,10,25]
x = 15

output = binary_search(arr,x)

if output != -1:
  print("element present at index ", str(output))
else:
  print("-1")

'''
Question 3
Write a Python program to find the middle of a linked list.
'''

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def push(self,new_data):
    node = Node(new_data)
    node.next = self.head
    self.head = node

  def print_midddle(self):
    slowPtr = self.head
    fastPtr = self.head

    if self.head is not None:
      while(fastPtr is not None and fastPtr.next is not None):
        fastPtr = fastPtr.next.next
        slowPtr = slowPtr.next
      print(slowPtr.data) 

llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(3)
llist.push(9)
llist.print_midddle()