#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

function completedTasks (data, userId) {
  let completed = 0;
  for (let i = 0; i < data.length; i++) {
    if (data[i].userId === userId && data[i].completed === true) {
      completed++;
    }
  }
  return completed;
}

const dict = {};

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const usersTasks = JSON.parse(body);
  for (let i = 1; i <= 10; i++) {
    const value = completedTasks(usersTasks, i);
    dict[i] = value;
  }
  console.log(dict);
});
