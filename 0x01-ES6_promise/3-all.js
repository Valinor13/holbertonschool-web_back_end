import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promArr = [uploadPhoto(), createUser()];
  Promise.all(promArr)
    .then((values) => console.log(`${values[0].body} ${values[1].firstName} ${values[1].lastName}`))
    .catch(() => console.error('Signup system offline'));
}