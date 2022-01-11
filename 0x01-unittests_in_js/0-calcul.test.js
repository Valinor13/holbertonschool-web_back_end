const { assert } = require("chai");
const calculateNumber = require("./0-calcul");

describe('calculateNumber exists', function() {
    it('should determine if caclulateNumber returns a value', function() {
        assert.exists(calculateNumber(4, 5), 'Return exists');
        assert.isNumber(calculateNumber(4, 5), 'Return is a number');
        assert.isNotNaN(calculateNumber(4, 5), 'Return is a number');
        assert.equal(calculateNumber(4, 5), 9, '4.0 + 5.0 = 9');
    })
})