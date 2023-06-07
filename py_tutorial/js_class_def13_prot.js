#!/usr/bin/node
/*
const coolBehavior = {
  toggle: function (enabled) {
    this.enabled = enabled;
    if (this.enabled) {
      console.log('Yes');
    }
  }
};
coolBehavior.toggle('enabled');
*/

const coolBehavior = {
  toggle: function (enabled) {
    this.enabled = enabled;
	return this.enabled;
    },
};

coolBehavior.enable = coolBehavior.toggle.bind(coolBehavior, false);
/*
console.log(coolBehavior.enable());
*/
const tr = coolBehavior.enable();
while (tr) {
  console.log("Yeah");
}
