import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const retArr = [];
  const promArr = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  const p = Promise.all(promArr);
  console.log(p);
  retArr.push(p);
  return retArr;
}
