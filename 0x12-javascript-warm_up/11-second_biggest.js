#!/usr/bin/node

const argv = process.argv;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let secBig = -Infinity;
  let firstBig = -Infinity;
  for (let i = 2; i < argv.length; i++) {
    const n = parseInt(argv[i]);
    if (n > firstBig) {
      secBig = firstBig;
      firstBig = n;
    } else if (n < firstBig && n > secBig) {
      secBig = n;
    }
  }
  console.log(secBig);
}
