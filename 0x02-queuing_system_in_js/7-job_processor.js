const kue = require('kue');

const que = kue.createQueue();
const blacklist = [
    '4153518780',
    '4153518781'
];

function sendNotification(phoneNumber, message, job, done) {
    if (blacklist.indexOf(phoneNumber) > -1) {
        job.progress(0);
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    } else {
        job.progress(50);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        done();
    }
};

que.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
