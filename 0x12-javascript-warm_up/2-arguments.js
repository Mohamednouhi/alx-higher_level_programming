#!/usr/bin/node

const arguments = process.argv.length - 2;
console.log(arguments === 0 ? 'No argument' : arguments === 1 ? 'Argument found' : 'Arguments found');
