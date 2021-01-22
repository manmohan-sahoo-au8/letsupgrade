/*
Question 1
What will the code below output to the console and why ?
*/
console.log(1 + "2" + "2");
//output - 122 , '+' act as concatenate operator, so the result is 122. 
console.log(1 + +"2" + "2");
//output - 32 , beacuse the first + sign makes addition so it adding first two numbers, and the second + sign makes the string, so the result is 32. 
console.log(1 + -"1" + "2");
//output - 02 , beacuse the first + sign makes addition so it adding first two numbers(1 & -1 i.e 0 ) and second + sign makes the string(2) . so the remaining output is 02.
console.log(+"1" + "1" + "2");
//output - 112 , because all + sign concatenate all the string , in js it will be join the values so the output is 112.
console.log( "A" - "B" + "2");
//output - NAN2 , because "A"-"B" is not a number so this output is NAN and rest cancat between NAN and "2". here "2" is a string. so the output is NAN2 
console.log( "A" - "B" + 2);
//output - 122 ,  because "A"-"B" is not a number so this output is NAN and rest cancat between NAN and 2, 2 is a number , so it print only NAN


/*
Question 2
You are given a variable “marks”. Your task is to print:
- AA if the mark is greater than 90
- AB if the mark is greater than 80 and less than or equal to 90
- BB if the mark is greater than 70and less than or equal to 80
- BC if the mark is greater than 60 and less than or equal to 70
- CC if the mark is greater than 50 and less than or equal to 60
- CD if the mark is greater than 40 and less than or equal to 50
- DD if the mark is greater than 30 and less than or equal to 40
- FF if the mark is less than or equal to 30
*/

var marks = prompt("enter your marks : ");

if (marks>90) {
  console.log("AA")
} else if (marks >80 && marks <= 90){
  console.log("AB")
} else if (marks >70 && marks <= 80) {
  console.log("BB")
} else if (marks >60 && marks <= 70){
  console.log("BC")
} else if (marks >50 && marks <= 60){
  console.log("CC")
}else if (marks >40 && marks <= 50){
  console.log("CD")
}else if (marks >30 && marks <= 40){
  console.log("DD")
} else {
  console.log("FF")
}