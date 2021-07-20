export default class Building {
  constructor(sqft) {
    this.sqft = sqft;
    if (this.constructor !== Building
      && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // sqft.getter
  get sqft() {
    return this._sqft;
  }

  // sqft.setter
  set sqft(newSqft) {
    if (typeof newSqft === 'number') {
      this._sqft = newSqft;
    } else {
      throw new TypeError('Sqft must be a number');
    }
  }
}
