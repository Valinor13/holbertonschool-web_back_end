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
      if (process.argv[2] === '') {
        throw new Error();
      }
      const studentRes = await countStudents(process.argv[2]);
      res.write('This is the list of our students\n');
      studentRes.forEach((element) => {
        res.write(element.concat('\n'));
      });
    } catch (error) {
      res.write('Cannot load the database');
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
