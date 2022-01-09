const readDatabase = require('../utils');

class StudentsController {
  async static getAllStudents(request, response) {
    response.write('This is the list of our students\n');
    try {
      if (process.argv[2] === '') {
        throw new Error();
      }
      const studentRes = await readDatabase(process.argv[2]);
      for (const [key, value] of Object.entries(studentRes)) {
        response.write(`Number of students in ${key}: ${value.length}. List: ${value}\n`);
      }
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
    response.end();
  }

  static getAllStudentsByMajor(request, response) {
   response.status(500).send('Major parameter must be CS or SWE');
  }
}

module.exports = StudentsController;
