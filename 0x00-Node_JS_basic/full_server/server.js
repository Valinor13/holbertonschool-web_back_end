import express from 'express';
import userRouter from './routes/index';

app = express();
port = 1245;

app.use('', userRouter);

app.listen(port, (err) => {
  if (err) {
    console.error(err);
  }
});

module.exports = app;
