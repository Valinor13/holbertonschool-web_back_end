const assert = require('assert');
const calculateNumber = require("./0-calcul");

describe('calculateNumber', function() {
    it('should determine if calculateNumber returns the correct value', function() {
        const num = calculateNumber(4, 5);
        assert.equal(num, 9, '4.0 + 5.0 = 9');
    })
})
