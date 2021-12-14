#!/usr/bin/node
const x = process.argv.slice(2);
if (parseInt(x[0])) {
  let str = '';
  for (let j = 0; j < x; j++) {
    str += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
