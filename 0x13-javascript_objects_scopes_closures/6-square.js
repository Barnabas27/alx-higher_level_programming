#!/usr/bin/node
const Sq = require('./5-square');
module.exports = class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    let sides = '';
    for (let j = 0; j < this.width; j++) {
     sides += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(sides);
    }
  }
};
