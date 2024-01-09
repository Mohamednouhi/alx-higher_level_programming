#!/usr/bin/node

const number = Math.floor(Number(process.argv[2]));

console.log(!isNaN(number) ? `My number: ${number}` : "Not a number");
