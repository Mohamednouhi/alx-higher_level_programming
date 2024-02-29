#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (isNaN(args[0]) || args.length <= 1) {
    console.log('0');
} else {
    const uniqueArgs = [...new Set(args)];
    const sorted = uniqueArgs.sort((a, b) => b - a);
    console.log(sorted[1]);
}

