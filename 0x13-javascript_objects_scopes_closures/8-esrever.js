#!/usr/bin/node

exports.esrever = function (list) {
  if (list) {
    const revList = [];
    for (let i = list.length; i >= 0; i--) {
      revList.push(list[i]);
    }
    return revList;
  }
};
