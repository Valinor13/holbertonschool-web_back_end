const expect = require('chai').expect;
const request = require('request');

describe("getIndexPage", function() {
    it("should return index page", function(done) {
      request('http://localhost:7865', function(err, res, body) {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      })
    });
});
