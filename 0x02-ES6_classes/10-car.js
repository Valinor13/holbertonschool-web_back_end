export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  // species.getter
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species(this.brand, this.motor, this.color);
  }

  // brand.getter
  get brand() {
    return this._brand;
  }

  // brand.setter
  set brand(newBrand) {
    if (typeof newBrand === 'string') {
      this._brand = newBrand;
    } else {
      throw new TypeError('Brand must be a string');
    }
  }

  // motor.getter
  get motor() {
    return this._motor;
  }

  // motor.setter
  set motor(newMotor) {
    if (typeof newMotor === 'string') {
      this._motor = newMotor;
    } else {
      throw new TypeError('Motor must be a string');
    }
  }

  // color.getter
  get color() {
    return this._color;
  }

  // color.setter
  set color(newColor) {
    if (typeof newColor === 'string') {
      this._color = newColor;
    } else {
      throw new TypeError('Color must be a string');
    }
  }
}
