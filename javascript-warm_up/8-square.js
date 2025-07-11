#!/usr/bin/node

const { argv } = require('node:process');
const char = 'X';
const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let line = '';
    for (let j = 0; j < number; j++) {
      line += char;
    }
    console.log(line);
  }
}
