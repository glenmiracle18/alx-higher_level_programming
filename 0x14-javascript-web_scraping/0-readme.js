#!/ust/bin/node

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'uft-8', (error, content) => {
	if (error) {
		console.log(error);
	} else {
		console.log(content);
	}
});
