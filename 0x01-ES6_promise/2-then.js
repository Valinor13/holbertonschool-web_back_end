export default function handleResponseFromAPI(promise) {
  return promise
    .then(console.log('Got a response from the API'), { status: 200, body: 'success' })
    .catch(new Error());
}
