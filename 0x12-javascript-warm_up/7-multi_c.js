#!/usr/bin/node

const argv = process.argv;
const x = parseInt(argv[2]);

if (x) {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
