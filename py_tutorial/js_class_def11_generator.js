#!/usr/bin/node

const obj2 = {
  g: function * () {
    let index = 0;
    while (true) {
      yield index++;
    }
  }
};

/*
// The same object using shorthand syntax
const obj2 = {
  *g () {
    let index = 0;
    while (true) {
      yield index++;
    }
  },
};
*/

const it = obj2.g();
console.log(it.next().value);
console.log(it.next().value);
