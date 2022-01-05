const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question('Welcome to Holberton School, what is your name?\n', (name) => {
  console.log(`Your name is: ${name}!`);
});

process.on('beforeExit', () => {
  readline.write('This important software is now closing');
});
