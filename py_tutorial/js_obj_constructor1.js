#!/usr/bin/node

function Person (name) {
  this.name = name;
  this.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
}

function createPerson (name) {
  return new Person (name);
}
module.exports = {
  createPersons: createPerson
};
/*
const salva = new Person('Salva');
//salva.name;
salva.introduceSelf();

const frankie = new Person('Frankie');
//frankie.name;
frankie.introduceSelf();
*/
