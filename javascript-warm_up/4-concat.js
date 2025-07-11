#!/usr/bin/node

const { argv } = require('node:process');

try {
  console.log(`${argv[2]} is ${argv[3]}`);
} catch (error) {
  console.log(error);
}
