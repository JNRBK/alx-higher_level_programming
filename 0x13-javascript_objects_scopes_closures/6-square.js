#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c) {
        console.log('C'.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
