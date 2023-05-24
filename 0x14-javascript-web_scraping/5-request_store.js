#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, 'utf-8', (error, reponse, body) => {
    if (error) {
        console.log(error);
    } else {
        fs.writeFile(filepath, body, 'utf8', (error) => {
            if (error) {
                console.log(error);
            }
        })
    }
})
