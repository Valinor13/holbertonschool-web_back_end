const assert = require('assert');
const calculateNumber = require("./0-calcul");

describe('calculateNumber', function() {
    it('should determine if calculateNumber returns the correct value', function() {
        const num = calculateNumber(4, 5);
        assert.equal(num, 9, '4.0 + 5.0 = 9');
    })
})

describe('calculateNumber aRounded', function() {
    it('should determine if calculateNumber returns the correct value', function() {
        const num = calculateNumber(4.4, 5);
        assert.equal(num, 9, '4.4 + 5.0 = 4 + 5 = 9');
    })
})

describe('calculateNumber bRounded', function() {
    it('should determine if calculateNumber returns the correct value', function() {
        const num = calculateNumber(4.0, 5.3);
        assert.equal(num, 9, '4.0 + 5.3 = 4 + 5 = 9');
    })
})

describe('calculateNumber bothRounded', function() {
    it('should determine if calculateNumber returns the correct value', function() {
        const num = calculateNumber(4.7, 5.5);
        assert.equal(num, 11, '4.7 + 5.5 = 5 + 6 = 11');
    })
})
