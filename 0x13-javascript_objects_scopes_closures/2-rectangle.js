#!/usr/bin/node

module.exports = class Rectangle {
	constructor (w, h) {
		if(w>0 && h>0) {
			this.height = h;
			this.weight = w;
		} else {
			this.height = undefined;
			this.width = undefined;
		}
	}
};
