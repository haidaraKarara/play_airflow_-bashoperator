// specify that a http API is queried
const http = require('http');

// define the API to query
const options = {
    hostname: 'api.open-notify.org',
    port: 80,
    path: '/iss-now',
    method: 'GET',
};

const req = http.request(options, res => {
    // log the status code of the API response
    console.log(`statusCode: ${res.statusCode}`);

    // write the result of the GET request to stdout
    res.on('data', d => {
        process.stdout.write(d);
    });
});

// in case of an error print the error statement to the console
req.on('error', error => {
    console.error(error);
});

req.end();