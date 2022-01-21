const redis = require('redis');

const sub = redis.createClient();
sub.on('error', (err) => console.log('Redis client not connected to the server:', err));
sub.on('ready', () => console.log('Redis client connected to the server'));

sub.on('message', (channel, message) => {
    console.log('literally anything');
    if (message === 'KILL_SERVER') {
        sub.unsubscribe('holberton school channel');
        sub.quit();
    }
    console.log(message);
});

sub.subscribe('holberton school channel');
