const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const fieldsList = [];
    const studentsByField = [];
    const returnList = [];
    const file = await fs.readFile(path, { encoding: 'utf8' });
    let studentList = file.split('\n');
    studentList.shift();
    studentList = studentList.filter((student) => student !== '');
    console.log(`Number of students: ${studentList.length}`);
    returnList.push(`Number of students: ${studentList.length}`);
    studentList.forEach((student) => {
      const field = student.split(',');
      fieldsList.push(field[3]);
    });
    const fieldSet = new Set(fieldsList);
    let i = 0;
    fieldSet.forEach((field) => {
      studentsByField.push([]);
      studentList.forEach((student) => {
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
      returnList.push(`Number of students in ${field}: ${studentsByField[j].length}. List: ${studentsByField[j].join(', ')}`);
      j += 1;
    });
    return returnList;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
