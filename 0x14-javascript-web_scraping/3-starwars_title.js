#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];
const url_api = 'https://swapi-api.alx-tools.com/api/films/${movie_id}';


request.get(url_api, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const data = JSON.parse(body);
        console.log(data.title);
    }
});
