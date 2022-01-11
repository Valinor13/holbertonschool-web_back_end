const chai = require('chai');
const calculateNumber = require("./2-calcul_chai");

describe('calculateNumber SUM', function() {
    it('should determine if calculateNumber returns the correct sum', function() {
        const num = calculateNumber('SUM', 4, 5);
        chai.expect(num).to.equal(9, '4.0 + 5.0 = 9');
    })
})

describe('calculateNumber SUBTRACT', function() {
    it('should determine if calculateNumber returns the correct subtraction', function() {
        const num = calculateNumber('SUBTRACT', 5, 1);
        chai.expect(num).to.equal(4, '5.0 - 1.0 = 4');
    })
})

describe('calculateNumber DIVIDE', function() {
    it('should determine if calculateNumber returns the correct division', function() {
        const num = calculateNumber('DIVIDE', 5, 5);
        chai.expect(num).to.equal(1, '5.0 / 5.0 = 1');
    })
})

describe('calculateNumber divideZero', function() {
    it('should determine if calculateNumber returns the correct error', function() {
        const num = calculateNumber('DIVIDE', 5, 0);
        chai.expect(num).to.equal('Error', '5.0 / 0.0 = Error');
    })
})
