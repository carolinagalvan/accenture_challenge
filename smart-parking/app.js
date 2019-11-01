const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const AWS = require('aws-sdk');
var s3 = new AWS.S3();
require('dotenv').config();
const next = require('./next');

const app = express();
// Put in place textbook middlewares for express.

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use('/', express.static(path.join(__dirname, 'public')));

const start = async port => {
    // Couple Next.js with our express server.
    // app and handle from "next" will now be available as req.app and req.handle.
    await next(app);

    // Normal routing, if you need it.
    // Use your SSR logic here.
    // Even if you don't do explicit routing the pages inside app/pages
    // will still get rendered as per their normal route.
    app.get('/main', (req, res) =>
        req.app.render(req, res, '/', {
            routeParam: req.params.routeParam,
        }),
    );

    app.get('/image/:imageId', function (req, res, next) {
        var params = { Bucket: 'accchalenge123', Key: req.params.imageId };
        s3.getObject(params, function (err, data) {
            res.writeHead(200, { 'Content-Type': 'image/png' });
            res.write(data.Body, 'binary');
            res.end(null, 'binary');
        });
    });

    app.listen(port);
};

// Start the express server.
start(9001);