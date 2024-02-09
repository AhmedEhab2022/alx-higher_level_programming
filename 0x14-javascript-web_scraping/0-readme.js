#!/usr/bin/node

const file = require("fs");
const content = file.readFile("cisfun", "utf-8", (err, content) => {
  if (err) {
    console.log(err);
  } else {
	console.log(content);
  }
});
