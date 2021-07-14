import * as utils from './utils';

export default function handleProfileSignup() {
  const pic = utils.uploadPhoto();
  const user = utils.createUser();
  pic.then((pictures) => {
    process.stdout.write(pictures.body.concat(' '));
  });
  user.then((users) => {
    console.log(users.firstName, users.lastName);
  });
}
