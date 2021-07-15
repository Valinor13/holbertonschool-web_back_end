/* eslint-disable no-param-reassign */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promArr = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  return Promise.allSettled(promArr).then((results) => results);
}
