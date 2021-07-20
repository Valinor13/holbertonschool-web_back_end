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
    return new Species();
  }

  // brand.getter
  get brand() {
    return this._brand;
  }

  // brand.setter
  set brand(newBrand) {
    this._brand = newBrand;
  }

  // motor.getter
  get motor() {
    return this._motor;
  }

  // motor.setter
  set motor(newMotor) {
    this._motor = newMotor;
  }

  // color.getter
  get color() {
    return this._color;
  }

  // color.setter
  set color(newColor) {
    this._color = newColor;
  }
}
