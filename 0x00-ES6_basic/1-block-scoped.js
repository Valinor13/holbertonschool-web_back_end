/* eslint-disable linebreak-style */
/* eslint-disable no-use-before-define */
export default function taskBlock(trueOrFalse) {
  if (trueOrFalse) {
    task = true;
    task2 = false;
  }

  let task = false;
  let task2 = true;
  return [task, task2];
}
