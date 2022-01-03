const process = require('process');

function displayMessage(message) {
  process.stdout.write(message);
}

module.exports = displayMessage;
