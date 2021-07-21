/* eslint-disable no-new-wrappers */
export default function hasValuesFromArray(inputSet, inputArray) {
  const booArry = inputArray.map((element) => inputSet.has(element));
  if (booArry.includes(false)) {
    return false;
  }
  return true;
}
