#!/usr/bin/node

const argv = process.argv;
const size = parseInt(argv[2]);

if (size) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
