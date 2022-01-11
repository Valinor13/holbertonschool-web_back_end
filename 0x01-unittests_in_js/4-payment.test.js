const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

const expect = chai.expect;

describe('sendPaymentRequestToApi', function() {
    it('Test to use function', function() {
        expect(sendPaymentRequestToApi(100, 20)).to.equal(120);
    });
    it('Stub the use of object function', function() {
        const stub = sinon.stub(Utils, 'calculateNumber');
        stub.withArgs(100, 20).returns(10);
        expect(sendPaymentRequestToApi(100, 20)).to.equal(10);
        spy.restore();
    });
});
