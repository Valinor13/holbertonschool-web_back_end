/* eslint-disable no-param-reassign */
export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  if (!(studentsList instanceof Array)) {
    return [];
  }

  function addGrade(student) {
    const newGrade = newGrades.filter((stud) => stud.studentId === student.id)[0];
    if (newGrade && newGrade.grade) {
      student.grade = newGrade.grade;
    } else {
      student.grade = 'N/A';
    }
    return student;
  }
  const filteredStudentList = studentsList.filter((students) => students.location === city);
  return filteredStudentList.map(addGrade);
}
