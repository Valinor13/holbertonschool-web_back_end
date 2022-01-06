const fs = require('fs');

function countStudents(path) {
  try {
    const fieldsList = [];
    const studentsByField = [];
    const file = fs.readFileSync(path, { encoding: 'utf8' });
    const studentList = file.split('\r\n');
    studentList.shift();
    const filteredStudents = studentList.filter((student) => student !== '');
    console.log(`Number of students: ${filteredStudents.length}`);
    filteredStudents.forEach((student) => {
      const field = student.split(',');
      fieldsList.push(field[3]);
    });
    const fieldSet = new Set(fieldsList);
    let i = 0;
    fieldSet.forEach((field) => {
      studentsByField.push([]);
      filteredStudents.forEach((student) => {
        const fields = student.split(',');
        if (field === fields[3]) {
          studentsByField[i].push(fields[0]);
        }
      });
      i += 1;
    });
    let j = 0;
    fieldSet.forEach((field) => {
      console.log(`Number of students in ${field}: ${studentsByField[j].length}. List: ${studentsByField[j].join(', ')}`);
      j += 1;
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
