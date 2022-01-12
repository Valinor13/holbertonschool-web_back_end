const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');
const chai = require('chai');
const sinon = require('sinon');

const expect = chai.expect;

describe('sendPaymentRequestToApi', function() {
    it('Test the console log is called once with correct value', function() {
        const spy = sinon.spy(console, 'log');
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledWith('The total is: 120')).to.be.true;
        expect(spy.calledOnce).to.be.true;
        spy.restore();
    });
});
