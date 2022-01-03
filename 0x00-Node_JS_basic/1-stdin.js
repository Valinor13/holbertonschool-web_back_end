const process = require('process');

process.stdout.write('Welcome to Holberton School, what is your name?'), (name) => {
  console.log(`Your name is: ${name}!`);
  readline.close();
});

process.on('SIGINT', () => {
  console.log('This important software is now closing');
});
