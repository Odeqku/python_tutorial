#!/usr/bin/node

class Base {
  baseGetX () {
    return 1;
  }

  static staticBaseGetX () {
    return 3;
  }
}
class AnotherBase {
  baseGetX () {
    return 2;
  }

  static staticBaseGetX () {
    return 4;
  }
}
class Extended extends Base {
  getX () {
    return super.baseGetX();
  }

  static staticGetX () {
    return super.staticBaseGetX();
  }
}

const e = new Extended();

Object.setPrototypeOf(Extended.prototype, AnotherBase.prototype);
console.log(e.getX());
console.log(Extended.staticGetX());
