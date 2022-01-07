import readDatabase from 'utils';

class StudentController {
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
      res.write('Cannot load the database');
      res.status(500);
    }
    res.end();
  }

  async static getAllStudentsByMajor(request, response) {
    return 'Major parameter must be CS or SWE', 500;
  }
}
