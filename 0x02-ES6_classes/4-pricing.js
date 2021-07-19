import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this._currency = currency;
  }

  // amount.getter
  get amount() {
    return this._amount;
  }

  // name.setter
  set amount(newAmount) {
    if (typeof newAmount === 'number') {
      this._amount = newAmount;
    } else {
      throw new TypeError('Amount must be a number');
    }
  }

  displayFullPrice() {
    return `${this.amount} ${Currency.name} (${Currency.code})`;
  }
}
