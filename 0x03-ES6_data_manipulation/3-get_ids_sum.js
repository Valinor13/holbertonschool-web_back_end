export default function getStudentIdsSum(inputArray) {
  if (!(inputArray instanceof Array)) {
    return [];
  }

  const a = inputArray.map((student) => student.id);
  return a.reduce((aV, cV) => aV + cV);
}
