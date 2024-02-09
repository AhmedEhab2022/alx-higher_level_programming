#!/usr/bin/node

const request = require('request');
const file = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  file.writeFile(filePath, body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
