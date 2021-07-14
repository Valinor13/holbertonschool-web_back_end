export default function signUpUser(firstName, lastName) {
  const p = new Promise((resolve) => {
    resolve({ firstName, lastName });
  });
  return p;
}
