#!/usr/bin/node
const args = process.argv.slice(2);
function compareNum (a, b) {
  return a - b;
}
const n = args.length;
if (n === 0 || n === 1) {
  console.log(0);
} else {
  console.log(args.sort(compareNum)[n - 2]);
}
