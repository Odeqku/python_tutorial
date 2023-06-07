#!/usr/bin/node

const person = {
  name: ['Bob', 'Smith'],
  age: 32
};

function logProperty (propertyName) {
  // Accessing the attribute of person object using 'bracket notation
  console.log(person[propertyName]);
}

logProperty('name');
logProperty('age');
