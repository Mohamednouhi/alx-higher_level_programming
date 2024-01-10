#!/usr/bin/node
module.exports = class Square extends require ('./5-square?js') {
	super();
	charPrint(c) {
		if (c!== undefined) {
			for(let i =0; i<this.heigth; i++) {
				for (let j=0; j<this.width; j++) {
					console.log('X');
				}
			}
		} else {
			this.print();
		}
	}
};
