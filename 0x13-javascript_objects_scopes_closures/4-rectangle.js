#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          console.log('X');
        }
      }
    }
  }

  rotate() {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double() {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}
