#!/usr/bin/node

function createPerson (name = 'name', age = 0) {
  const obj = {};
  obj.name = name;
  obj.age = age;
  obj.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name} and I'm ${this.age} year old.`);
  };
  return obj;
}
module.exports = {
  createPerson: createPerson
};
