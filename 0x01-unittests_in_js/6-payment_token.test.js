const getPaymentTokenFromAPI = require('./6-payment_token');
const expect = require('chai').expect;

describe('getPaymentTokenFromAPI', function () {
    it('Test async return of function', function(done) {
        getPaymentTokenFromAPI(true).then(function(result) {
            expect(result.data).to.equal('Successful response from the API');
            done();
        });
    });
});
