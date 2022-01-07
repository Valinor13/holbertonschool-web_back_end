const readDatabase = require('../utils');

class StudentsController {
  async static getAllStudents(request, response) {
    response.write('This is the list of our students');
    try {
      if (process.argv[2] === '') {
        throw new Error();
      }
      const studentRes = await readDatabase(process.argv[2]);
      studentRes.forEach((element) => {
        res.write(element.concat('\n'));
      });
    } catch (error) {
      res.status(404).send(err.message);
    }
    res.end();
  }

  async static getAllStudentsByMajor(request, response) {
    return response.status(500).send('Major parameter must be CS or SWE');
  }
}

module.exports = StudentsController;
