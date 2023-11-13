#!/usr/bin/node

const argv = process.argv;
const myNumber = parseInt(argv[2]);

if (myNumber) {
  console.log('My number: ' + myNumber);
} else {
  console.log('Not a number');
}
