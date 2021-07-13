export default function concatArrays(array1, array2, string) {
  const newArry = [...array1, ...array2, ...string];
  return newArry;
}
