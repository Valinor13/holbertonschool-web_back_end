import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .catch(() => console.log('Signup system offline'))
    .then((values) => console.log(`${values[0].body} ${values[1].firstName} ${values[1].lastName}`));
}
