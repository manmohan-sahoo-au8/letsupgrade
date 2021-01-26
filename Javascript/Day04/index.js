/* Question 1
Write a JavaScript program to display the reading status (i.e. display book name, author name,
  and reading status) of the following books.
  The output should look like this:
  Already read 'Bill Gates' by The Road Ahead.
  Already read 'Steve Jobs' by Walter Isaacson.
  You still need to read 'Mockingjay: The Final Book of The Hunger Games' by Suzanne
  Collins.
  */
  var library = [
{
author: 'Bill Gates',
title: 'The Road Ahead',
readingStatus: true
},
{
author: 'Steve Jobs',
title: 'Walter Isaacson',
readingStatus: true
},
{
author: 'Suzanne Collins',
title: 'Mockingjay: The Final Book of The Hunger Games',
readingStatus: false
}];


for(var i= 0; i<library.length; i++) {
  var book = '' + library[i].title+''+'by'+library[i].author
  if(library[i].readingStatus) {
    console.log(`Already read ${book}`)
  } else {
    console.log(`You still need to read ${book}`)
  }
}

/*
Question 2
Write a javascript program that generates an alert "Not legal age to drive" if the driver age is
below 18 years old, if driver age is greater than or equal to 18, it generates an alert "Drive safe".
*/
age = prompt("enter your age")
if(age<18){
  alert("Not legal age to drive")
} else {
  alert("Drive Safe")
}