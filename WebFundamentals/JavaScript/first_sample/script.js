console.log("Hello World")

var myNum = 123;
var myString1 = "abc";
var myString2 = 'abc';
var myString3 = `abc`;
var boolean1 = true;
var boolean2 = false;
var filecabinet = [1,2,3,[100,1,1]];

console.log(myNum);
console.log(filecabinet[0]);
console.log(filecabinet[3][0]);

var object = {
    first_name: 'Ryan' , last_name: 'Kula' , email: "yoyo@gmail.com"
}

console.log(object);

console.log(object['first_name']);

console.log("-----------")
console.log(100%4)

var age = 13;

if (age >= 18) {
    console.log("You're an adult!")
}
else {
    console.log("You're a kid!")
}