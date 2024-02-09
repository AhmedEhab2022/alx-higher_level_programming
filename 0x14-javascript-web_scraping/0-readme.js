#!/usr/bin/node

filename = process.argv[1];
const file = require("fs");
const content = file.readFile(filename, "utf-8", (err, content) => {
  if (err) {
    console.log(err);
  } else {
	console.log(content);
  }
});
