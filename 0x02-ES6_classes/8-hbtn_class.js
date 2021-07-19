export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  toNum() {
    return this.size;
  }

  toString() {
    return this.location;
  }

  // size.getter
  get size() {
    return this._size;
  }

  // size.setter
  set size(newSize) {
    if (typeof newSize === 'number') {
      this._size = newSize;
    } else {
      throw new TypeError('Size must be a number');
    }
  }

  // location.getter
  get location() {
    return this._location;
  }

  // location.setter
  set location(newLocation) {
    if (typeof newLocation === 'string') {
      this._location = newLocation;
    } else {
      throw new TypeError('Location must be a string');
    }
  }
}
