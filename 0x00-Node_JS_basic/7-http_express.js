const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.write('This is the list of our students\n');
  try {
    if (process.argv[2] === '') {
      throw new Error();
    }
    const studentRes = await countStudents(process.argv[2]);
    studentRes.forEach((element) => {
      res.write(element.concat('\n'));
    });
  } catch (error) {
    res.write('Cannot load the database');
  }
  res.end();
});

app.listen(port);

module.exports = app;
