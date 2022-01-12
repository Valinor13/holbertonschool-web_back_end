const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

const expect = chai.expect;

describe('sendPaymentRequestToApi', function() {
    it('Stub the use of object function', function() {
        const stub = sinon.stub(Utils, 'calculateNumber');
        const spy = sinon.spy(console, 'log');
        stub.withArgs('SUM', 100, 20).returns(10);
        expect(sendPaymentRequestToApi(100, 20)).to.equal(10);
        expect(spy.calledWith('The total is: 10')).to.be.true;
        stub.restore();
        spy.restore();
    });
});
