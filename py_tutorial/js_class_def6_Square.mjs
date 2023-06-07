#!/usr/bin/node

import { Shape } from './js_class_def5_Shape.mjs';

class Square extends Shape {
  constructor (sideLength) {
    super('square', 4, sideLength);
  }

  calcArea () {
    const area = this.sideLength * this.sideLength;
    console.log(`Area of the ${this.name} is ${area}`);
  }
}
const square = new Square(7);

square.calcArea();
square.calcPerimeter();
