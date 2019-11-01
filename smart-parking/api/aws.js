var AWS = require('aws-sdk');

export default class AwsBuckets {
    constructor() {
        // Create unique bucket name
        this.bucketName = 'accchallenge123';
        // Create name for uploaded object key
        this.keyName = 'us-east-2';
    }
    listObjects() {
        return new Promise((resolve, reject) => {
            var params = {
                Bucket: this.bucketName,
                MaxKeys: 1000,
            };
            var s3 = new AWS.S3();
            s3.listObjects(params, function (err, data) {
                if (err) {
                    console.log(err, err.stack);
                } else {
                    console.log(data);
                    resolve(data);
                }
            });
        });
    }
}