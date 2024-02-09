#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

let count = 0;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body);
  for (const result of films.results) {
    if (result.characters.includes(characterUrl)) {
      count++;
    }
  }
  console.log(count);
});
