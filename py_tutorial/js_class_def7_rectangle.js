#!/usr/bin/node

// Declaration of a class

class Rectangle {
  constructor (height, width) {
    this.height = height;
    this.width = width;
  }
}

// Expression; the class is anonymous but assigned to a variable
const Rectangle = class {
  constructor (heightm width) {
    this.height = height;
    this.width = width;
  }
};

// Expression; the class has its own name
const Rectangle = class Rectangle2 {
  constructor (height, width) {
    this.height = height;
    this.width = width;
  }
};
