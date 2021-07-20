export default class Building {
  evacuationWarningMessage() {
    if (this.evacuationWarningMessage !== Building.prototype.evacuationWarningMessage
      && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  constructor(sqft) {
    this.sqft = sqft;
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
