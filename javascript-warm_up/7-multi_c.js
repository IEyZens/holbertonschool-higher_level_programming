#!/usr/bin/node

const { argv } = require('node:process');
const string = 'C is fun';
const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log(string);
  }
}
