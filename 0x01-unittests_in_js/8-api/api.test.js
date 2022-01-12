const getIndexPage = require('./api');
const sinon = require('sinon');
const expect = require('chai').expect;

describe("getIndexPage", function() {
    it("should return index page", function() {
      let req = {}
      let res = {
        send: sinon.spy()
      }
      getIndexPage(req, res);
      console.log(res.send);
    });
});
