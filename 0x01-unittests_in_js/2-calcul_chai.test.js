const chai = require('chai');
const calculateNumber = require("./1-calcul");

describe('calculateNumber SUM', function() {
    it('should determine if calculateNumber returns the correct sum', function() {
        const num = calculateNumber(4, 5, 'SUM');
        chai.expect(num).to.equal(9, '4.0 + 5.0 = 9');
    })
})

describe('calculateNumber SUBTRACT', function() {
    it('should determine if calculateNumber returns the correct subtraction', function() {
        const num = calculateNumber(5, 1, 'SUBTRACT');
        chai.expect(num).to.equal(4, '5.0 - 1.0 = 4');
    })
})

describe('calculateNumber DIVIDE', function() {
    it('should determine if calculateNumber returns the correct division', function() {
        const num = calculateNumber(5, 5, 'DIVIDE');
        chai.expect(num).to.equal(1, '5.0 / 5.0 = 1');
    })
})

describe('calculateNumber divideZero', function() {
    it('should determine if calculateNumber returns the correct error', function() {
        const num = calculateNumber(5, 0, 'DIVIDE');
        chai.expect(num).to.equal('Error', '5.0 / 0.0 = Error');
    })
})
