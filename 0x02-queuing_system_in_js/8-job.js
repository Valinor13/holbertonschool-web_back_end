function createPushNotificationsJobs(jobs, queue) {
    if (typeof jobs !== 'array') {
        throw new Error('Jobs is not an array');
    }
    jobs.forEach(data => {
        let job = queue.create('push_notification_code_3', data).save((err) => {
            if (!err) {
              console.log(`Notification job created: #${job.id}`);
            }
          });
          job.on('complete', () => {
            console.log(`Notification job #${job.id} completed`)
          }).on('progress', (progress) => {
            console.log(`Notification job #${job.id} ${progress}% complete`)
          }).on('failed', (err) => {
            console.log(`Notification job #${job.id} failed: ${err}`)
          });
    });
};
