import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promArr = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  const retArr = [];
  Promise.allSettled(promArr)
    .then((values) => retArr.push(values));
  return retArr;
}
