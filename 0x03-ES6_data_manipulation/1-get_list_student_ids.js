export default function getListStudentIds(inputArray) {
  if (!(inputArray instanceof Array)) {
    return [];
  }

  return inputArray.map((student) => student.id);
}
