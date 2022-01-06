const http = require('http');

const port = 1245;
const app = http.createServer((res) => {
  res.end('Hello Holberton School!');
});

app.listen(port, (err) => {
  if (err) {
    console.error(err);
  }
});

module.exports = app;
