import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const retArr = [];
  const userProm = signUpUser(firstName, lastName);
  const picProm = uploadPhoto(fileName);
  userProm.then((user) => {
    console.log(user);
  });
  picProm.then((pics) => {
    console.log(pics);
  });
  return retArr;
}
