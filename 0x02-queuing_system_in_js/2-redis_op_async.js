const redis = require('redis');

const client = redis.createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  await client.get(schoolName, (err, data) => console.log(data));
}

(async () => {
  await displaySchoolValue('Holberton');
})();
setNewSchool('HolbertonSanFrancisco', '100');
(async () => {
  await displaySchoolValue('HolbertonSanFrancisco');
})();
