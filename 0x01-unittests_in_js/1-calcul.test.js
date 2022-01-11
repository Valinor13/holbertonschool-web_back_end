const assert = require('assert');
const calculateNumber = require("./1-calcul");

describe('calculateNumber SUM', function() {
    it('should determine if calculateNumber returns the correct sum', function() {
        const num = calculateNumber(4, 5, 'SUM');
        assert.equal(num, 9, '4.0 + 5.0 = 9');
    })
})

describe('calculateNumber SUBTRACT', function() {
    it('should determine if calculateNumber returns the correct subtraction', function() {
        const num = calculateNumber(5, 1, 'SUBTRACT');
        assert.equal(num, 4, '5.0 - 1.0 = 4');
    })
})

describe('calculateNumber DIVIDE', function() {
    it('should determine if calculateNumber returns the correct division', function() {
        const num = calculateNumber(5, 5, 'DIVIDE');
        assert.equal(num, 1, '5.0 / 5.0 = 1');
    })
})

describe('calculateNumber divideZero', function() {
    it('should determine if calculateNumber returns the correct error', function() {
        const num = calculateNumber(4, 0, 'DIVIDE');
        assert.equal(num, 'Error', '4.0 / 0.0 = Error');
    })
})
