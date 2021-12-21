#!/usr/bin/node
exports.esrever = function (list) {
  const normArray = [];
  let j = 0;
  for (let i = (list.length - 1); i >= 0; i--) {
    normArray[j] = list[i];
    j++;
  }
  return normArray;
};
