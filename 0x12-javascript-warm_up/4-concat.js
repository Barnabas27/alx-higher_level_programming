#!/usr/bin/node
const args = process.argv.slice(2);
if (!args[0]) {
  args[0] = 'undefined';
}
if (!args[1]) {
  args[1] = ' undefined';
}
console.log(args[0] + ' is ' + args[1]);
