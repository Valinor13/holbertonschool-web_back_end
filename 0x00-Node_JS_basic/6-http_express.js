const express = require('express');

const app = express();
const port = 1245;

app.gget('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(port);

module.exports = app;
