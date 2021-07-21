/* eslint-disable consistent-return */
/* eslint-disable no-unused-vars */
export default function cleanSet(inputSet, startString) {
  if (!(startString) || !(startString instanceof String)) {
    return '';
  }
  const retString = '';
  function findString(element) {
    if (element.startsWith(startString)) {
      return retString.concat(element, '-');
    }
  }
  inputSet.forEach(findString);
  return retString.replace(startString, '');
}
