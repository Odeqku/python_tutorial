#!/usr/bin/node

class Shape {
  /*
  name;
  sides;
  sideLength;
  */
  constructor (name, sides, sideLength) {
    this.name = name;
    this.sides = sides;
    this.sideLength = sideLength;
  }

  calcPerimeter () {
    const peri = this.sides * this.sideLength;
    console.log(`Perimeter of the ${this.name} is: ${peri}`);
  }
}
/*
const square = new Shape('Square', 4, 5);
square.calcPerimeter();

const triangle = new Shape('Triangle', 3, 3);
triangle.calcPerimeter();
*/
export { Shape };
