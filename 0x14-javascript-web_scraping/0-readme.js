#!/usr/bin/node

const request = require('request');

function readFile(filePath) {
	request(filePath, {encoding: 'utf-8'}, (err, response, body) => {
		if (err) {
			console.error(err);
			return;
		}
		console.log(body);
	});
}

if (process.argv.length !== 3) {
	console.error('Usage: 0-readme.js <file_url>')
	process.exit(1);
}

const fileUrl =process.argv[2];
readFile(fileUrl);
