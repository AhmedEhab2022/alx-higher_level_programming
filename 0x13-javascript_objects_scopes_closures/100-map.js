#!/usr/bin/node

const list = require('./100-data').list;

let i = -1;
const newList = list.map((num) => {
  i++;
  return num * i;
});

console.log(list);
console.log(newList);
