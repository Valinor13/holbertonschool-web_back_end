const express = require('express');

app = express();
const port = 7865;

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    if (typeof req.params.id === 'number') {
        res.send(`Payment methods for cart ${req.params.id}`);
    };
});

app.listen(port, () => {
    console.log('API available on localhost port 7865');
});

module.exports = app;
