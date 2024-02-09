#!/usr/bin/node

const filename = process.argv[2];
const file = require('fs');
file.readFile(filename, 'utf-8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
