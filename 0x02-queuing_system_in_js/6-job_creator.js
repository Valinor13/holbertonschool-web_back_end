const kue = require('kue')

const que = kue.createQueue();
const data = {
  phoneNumber: '8675309',
  message: 'Oh, you don\'t know me, but you make me so happy',
};
const job = que.create('push_notification_code', data).save(() => console.log(`Notification job created: ${job.id}`));

job.on('complete', () => console.log('Notification job completed')).on('failed', () => console.log('Notification job failed'));
