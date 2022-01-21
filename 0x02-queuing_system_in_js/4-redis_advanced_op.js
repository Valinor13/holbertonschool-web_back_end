const redis = require('redis');

const client = redis.createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('ready', () => console.log('Redis client connected to the server'));

client.hmset('HolbertonSchools', 'Tulsa', 50, 'New Haven', 80, 'San Fran', 20, 'Bogota', 20, 'Cali', 40, 'Paris', 2, redis.print);
client.hgetall('HolbertonSchools', (err, data) => console.log(data));
