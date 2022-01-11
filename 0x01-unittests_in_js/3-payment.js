const Utils = require('./utils.js');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const sum = Utils.calculateNumber(totalAmount, totalShipping, 'SUM');
    console.log(`The total is: ${sum}`);
}
