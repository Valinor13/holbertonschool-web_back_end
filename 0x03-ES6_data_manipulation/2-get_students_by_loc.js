export default function getListStudentIds(inputArray, filterString) {
  if (!(inputArray instanceof Array)) {
    return [];
  }

  return inputArray.filter((students) => students.location === filterString);
}
