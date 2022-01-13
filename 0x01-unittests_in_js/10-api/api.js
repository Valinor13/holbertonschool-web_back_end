const express = require('express');

app = express();
app.use(express.json());
const port = 7865;

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    try {
        Number(req.params.id);
        if (isNaN(req.params.id)) {
            throw new Error;
        }
        res.send(`Payment methods for cart ${req.params.id}`);
    } catch (err) {
        res.sendStatus(404);
    }
});

app.get('/available_payments', (req, res) => {
    res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

app.post('/login', (req, res) => {
    res.send(`Welcome ${req.body.userName}`);
    res.end();
});

app.listen(port, () => {
    console.log('API available on localhost port 7865');
});

module.exports = app;
