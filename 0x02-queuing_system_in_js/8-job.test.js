const expect = require('chai').expect;
const createPushNotificationsJobs = require('./8-job');
const kue = require('kue');

const que = kue.createQueue();

describe('functionality that deals with kue', () => {
    before(() => que.testMode.enter());
    afterEach(() => que.testMode.clear());
    after(() => que.testMode.exit());
    
    it('enques a job validating correct data', () => {
        const list = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '1234567890',
                message: 'This is test job 2'
            }
        ];
        createPushNotificationsJobs(list, que);
        expect(que.testMode.jobs.length).to.equal(2);
        expect(que.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(que.testMode.jobs[0].data).to.eql({
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        });
        expect(que.testMode.jobs[1].data).to.eql({
            phoneNumber: '1234567890',
            message: 'This is test job 2'
        });
    })
});
