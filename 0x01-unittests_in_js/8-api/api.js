const express = require('express');

app = express();
const port = 7865;
const getIndexPage = function(req, res) {
    res.send('Welcome to the payment system');
}

app.get('/', getIndexPage);

app.listen(port, () => {
    console.log('API available on localhost port 7865');
});

module.exports = app;
