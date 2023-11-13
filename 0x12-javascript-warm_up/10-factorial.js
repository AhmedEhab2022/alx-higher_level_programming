#!/usr/bin/node

const argv = process.argv;
const n = parseInt(argv[2]);

function fac (n) {
  if (!n || n === 1) {
    return 1;
  }
  return n * fac(n - 1);
}

console.log(fac(n));
