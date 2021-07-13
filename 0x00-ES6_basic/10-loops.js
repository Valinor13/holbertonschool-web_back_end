export default function appendToEachArrayValue(array, appendString) {
  const newArry = [];
  for (const [idx, value] of array) {
    if (array[idx] === value) {
      newArry.push(appendString + value);
    } else {
      newArry.push(appendString + array[idx]);
    }
  }
  return newArry;
}
