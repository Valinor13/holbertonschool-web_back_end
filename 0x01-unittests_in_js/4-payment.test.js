const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

const expect = chai.expect;

describe('sendPaymentRequestToApi', function() {
    it('Test to use function', function() {
        expect(sendPaymentRequestToApi(100, 20)).to.equal(120);
    });
    it('Spy the use of callback function', function() {
        const spy = sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestToApi(100, 20);
        expect(spy.called).to.be.true;
        spy.restore();
    });
});
