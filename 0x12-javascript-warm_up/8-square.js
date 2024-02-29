#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num) || num<=0) {
	console.log('Missing size');
} else {
	for (let i=0; i<num; i++) {
		console.log('X'.repeat(num));
	}
}
