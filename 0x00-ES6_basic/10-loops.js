export default function appendToEachArrayValue(array, appendString) {
  const newArry = [];
  for (const idx of array) {
    newArry.push(appendString + array[idx]);
  }
  return newArry;
}
