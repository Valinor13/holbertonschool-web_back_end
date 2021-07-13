export default function concatArrays(array1, array2, string) {
  const newArry = array1.concat(array2);
  for (let i = 0; i < string.length; i += 1) {
    newArry.push((string.charAt(i)));
  }
  return newArry;
}
