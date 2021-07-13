export default function getResponseFromAPI() {
    let p = new Promise((resolve, reject) => {
        if (1 === 1) {
            resolve('Success');
        } else {
            reject('Failure');
        }
    })
    return p;
}