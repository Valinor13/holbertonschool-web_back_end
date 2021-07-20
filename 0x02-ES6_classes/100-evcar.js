/* eslint-disable class-methods-use-this */
import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this.range = range;
  }

  cloneCar() {
    return new Car();
  }

  // range.getter
  get range() {
    return this._range;
  }

  // brand.setter
  set range(newRange) {
    this._range = newRange;
  }
}
