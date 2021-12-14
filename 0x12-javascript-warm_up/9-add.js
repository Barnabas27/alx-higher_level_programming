#!/usr/bin/node
const args = process.argv.slice(2);
function add (a, b) {
  console.log(a + b);
}
const a = parseInt(args[0]);
const b = parseInt(args[1]);
add(a, b);
