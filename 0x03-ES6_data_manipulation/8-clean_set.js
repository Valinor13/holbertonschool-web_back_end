export default function cleanSet(inputSet, startString) {
  if (!(startString) || !(typeof startString === 'string')) {
    return '';
  }
  const retArr = [];
  for (const str of inputSet) {
    if (str.startsWith(startString)) {
      retArr.push(str.replace(startString, ''));
    }
  }
  return retArr.join('-');
}
