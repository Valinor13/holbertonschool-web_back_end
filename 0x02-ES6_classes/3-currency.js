export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  // code.getter
  get code() {
    return this._code;
  }

  // code.setter
  set code(newCode) {
    if (typeof newCode === 'string') {
      this._code = newCode;
    } else {
      throw new TypeError('Code must be a string');
    }
  }

  // name.getter
  get name() {
    return this._name;
  }

  // name.setter
  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
