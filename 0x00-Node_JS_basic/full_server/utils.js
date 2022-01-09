const fs = require('fs').promises;

async function readDatabase(path) {
  try {
    const fieldsList = [];
    const studentsByField = [];
    const returnDict = {};
    const file = await fs.readFile(path, { encoding: 'utf8' });
    let studentList = file.split('\n');
    studentList.shift();
    studentList = studentList.filter((student) => student !== '');
    studentList.forEach((student) => {
      const field = student.split(',');
      fieldsList.push(field[3]);
    });
    fieldsList.sort();
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
      returnDict[field] = studentsByField[j];
      j += 1;
    });
    return returnDict;
  } catch (err) {
    reject(new Error(err));
  }
}

module.exports = readDatabase;
