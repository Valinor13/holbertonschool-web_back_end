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

describe('getCartPage', function() {
  it('should return cart page specific to id', function(done) {
    request('http://localhost:7865/cart/13', function(err, res, body) {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 13');
      done();
    });
  });

  it('should return 404 when NaN', function(done) {
    request('http://localhost:7865/cart/NaN', function(err, res, body) {
      expect(res.statusCode).to.equal(404);
      expect(body).to.equal('Not Found');
      done();
    });
  })
});

describe('getAvailablePaymentsPage', () => {
  it('returns the right data object', (done) => {
    request('http://localhost:7865/available_payments', (err, res, body) => {
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});

describe('postLoginPage', () => {
  it('Returns the right message', function (done) {
    request.post('http://localhost:7865/login', {
      json: {
        userName: 'Valinor',
      }
    }, (err, res, body) => {
      expect(body).to.equal(`Welcome Valinor`);
      done();
    });
  });
});