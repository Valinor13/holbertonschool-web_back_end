const kue = require('kue')

const que = kue.createQueue();
const data = {
  phoneNumber: String,
  message: String,
};
const job = que.create('push_notification_code', data, () => console.log(`Notification job created: ${job.id}`));

job.on('complete', () => console.log('Notification job completed')).on('failed', () => console.log('Notification job failed'));
