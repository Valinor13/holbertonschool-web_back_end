const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;
const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  }
  if (req.url === '/students') {
    try {
      const studentRes = await countStudents(process.argv[2]);
      res.write('This is the list of our students');
      studentRes.forEach((element) => {
        res.write(element);
      });
    } catch (error) {
      res.write(error);
    }
    res.end();
  }
});

app.listen(port, (err) => {
  if (err) {
    console.error(err);
  }
});

module.exports = app;
