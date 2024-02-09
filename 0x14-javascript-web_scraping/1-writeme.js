#!/usr/bin/node

const filename = process.argv[2];
const data = process.argv[3];
const file = require('fs');
file.writeFile(filename, data, (err) => {
  if (err) {
    console.log(err);
  }
});
