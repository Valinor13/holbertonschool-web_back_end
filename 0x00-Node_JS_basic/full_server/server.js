const express = require('express');
const userRouter = require('./routes/index');

app = express();
port = 1245;

app.use(userRouter);

app.listen(port, (err) => {
  if (err) {
    console.error(err);
  }
});

module.exports = app;
