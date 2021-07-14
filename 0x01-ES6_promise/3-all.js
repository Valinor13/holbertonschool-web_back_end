import * as utils from './utils';

export default function handleProfileSignup() {
  const pic = utils.uploadPhoto();
  const user = utils.createUser();
  console.log(pic + user);
}
