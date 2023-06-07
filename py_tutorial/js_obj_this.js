#!/usr/bin/node

const person1 = {
  name: 'Chris',
  introduceSelf () {
  console.log(`Hi! I'm ${this.name}.`);
  }
};

const person2 = {
  name: 'Deepti',
  introduceSelf () {
  console.log(`Hi! I'm ${this.name}.`);
  }
};
//console.log(person1.name);
person1.introduceSelf ();

//console.log(person2.name);
person2.introduceSelf ();
