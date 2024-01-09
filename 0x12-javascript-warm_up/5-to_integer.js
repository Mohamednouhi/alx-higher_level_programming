#!/usr/bin/node

const arg = process.argv[2];
const num = parseInt(arg);

console.log(!isNaN(num) ? `My number: ${num}` : "Not a number");
