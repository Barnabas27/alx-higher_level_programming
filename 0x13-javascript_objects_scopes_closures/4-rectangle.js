#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let sides = '';
    for (let j = 0; j < this.width; j++) {
      sides += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(sides);
    }
  }

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
