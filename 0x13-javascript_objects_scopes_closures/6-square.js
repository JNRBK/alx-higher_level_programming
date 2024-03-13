#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
//   constructor (size) {
//     super(size);
//   }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c === 'C') {
        console.log('C'.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
