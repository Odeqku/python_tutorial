#!/usr/bin/node
/*
function MyObject (name, message) {
  this.name = name.toString();
  this.message = message.toString();
  this.getName = function () {
    return this.name;
  };
  // declaring a method on the object
  this.getMessage = function () {
    return this.message;
  }
}

const myObject = new MyObject('Abdul', 'Hello');
console.log(myObject.getMessage(), myObject.getName());
*/

function MyObject (name, message) {
  this.name = name.toString();
  this.message = message.toString();
}
MyObject.prototype = {
  getName () {
    return this.name;
  },
  getMessage () {
    return this.message;
  }
};
const myObject = new MyObject('Abdul', 'Hi');
console.log(myObject.getName(), myObject.getMessage());
