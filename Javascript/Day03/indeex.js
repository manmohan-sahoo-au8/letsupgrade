/*Question 1
What is the value of clothes[0] and why?
*/
const clothes = ['jacket', 't-shirt'];
clothes.length = 0;
console.log(clothes[0]);

// output of this is undefined because of this length property, when it executes the line no 4 that time the array of elements got deleted. so right now the array is empty so the result is undefined.

/*
Question 2
Write a Javascript program to find the sum of all elements of a given array?
*/

var array = [2,4,5,5,8,9]
sum=0

for(i=0; i<array.length; i++) {
  sum += array[i]
}

console.log(sum)