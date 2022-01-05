const http = require('http');

const port = 1245;
const app = http.createServer((res) => {
  res.write('Hello Holberton School!');
  res.end();
});

app.listen(port, (err) => {
  if (err) {
    console.error(err);
  }
});

module.exports = app;
