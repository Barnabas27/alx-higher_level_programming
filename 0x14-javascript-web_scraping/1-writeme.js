#!/usr/bin/node
/* script that wirtes a string to a file*/

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, 'utf-8', (err, d) => {
  if (err) {
    console.log(err);
  }
}
);