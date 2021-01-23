'''
Question 1
Name 5 sorting algorithms, also write their time complexities(best, average, worst).

1.Quick Sort:-
  Quick sort is devide and conquer algorithim. it picks an element as pivot and partitions the given array around the picked pivot.

  Time complexitiy:
    Best-O(nlogn)
    Average-O(nlogn)
    Worst-O(n^2)

2.Merge Sort:-
  It devides the input array into teo halves,calls itself for the two halves,and them merges the two sorted halves .

  Time complexitiy:
    Best-O(nlogn)
    Average-O(nlogn)
    Worst-O(nlogn)

3.Insertion Sort:-
  Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

  Time complexitiy:
    Best-O(n)
    Average-O(n^2)
    Worst-O(n^2)

4.Bubble Sort:-
   works by repeatedly swapping the adjacent elements if they are in wrong order.

  Time complexitiy:
    Best-O(n)
    Average-O(n^2)
    Worst-O(n^2)

5.Selection Sort:-
   The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

  Time complexitiy:
    Best-O(n^2)
    Average-O(n^2)
    Worst-O(n^2)

'''

'''
Question 2
Implement selection sort algorithm using Python.
'''
def selection_sort(array):
  a = len(array)
  for i in range(a-1):
    minimum_index=i
    for j in range(i+1,a-1):
      if array[minimum_index] > array[j]:
        minimum_index = j
    array[i],array[minimum_index] = array[minimum_index], array[i]

array = [5,8,9,4,6,7]
print(array)
selection_sort(array)
print(array)

'''
Question 3
Implement pop operation of the stack
'''
stack = []

stack.append(2)
stack.append(6)
stack.append(8)
stack.append(7)

print(stack)

stack.pop()

print(stack)


'''
Question 4
Implement dequeue operation of the queue
'''
queue = []

queue.append(9)
queue.append(1)
queue.append(3)
queue.append(4)

print(queue)

queue.pop()

print(queue)