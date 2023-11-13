#!/usr/bin/node

const argv = process.argv;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let secBig = parseInt(argv[2]);
  let firstBig;
  for (let i = 3; i < argv.length; i++) {
    const n = parseInt(argv[i]);
    if (n > secBig && !firstBig) {
      firstBig = n;
    } else if (firstBig && n > firstBig) {
      secBig = firstBig;
      firstBig = n;
    } else if (n > secBig) {
      secBig = n;
    }
  }
  console.log(secBig);
}
