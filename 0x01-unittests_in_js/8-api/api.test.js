const app = require('./api');
const sinon = require('sinon');
const request = require('chai').request;

describe("getIndexPage", function() {
    it("should return index page", function(done) {
      chai.request(app).get('/')
      .end((err, response) => {
          response.should.have.status(200);
          response.body.should.be.eq('Welcome to the payment system')
          done();
      });
    });
});
