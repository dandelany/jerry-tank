const gpio = require('raspi-gpio');

module.exports = {
  stop: (outputs) => {
    outputs.aForward.write(gpio.LOW);
    outputs.aReverse.write(gpio.LOW);
    outputs.bForward.write(gpio.LOW);
    outputs.bReverse.write(gpio.LOW);
  },
  forward: (outputs) => {
    outputs.aReverse.write(gpio.LOW);
    outputs.bReverse.write(gpio.LOW);
    outputs.aForward.write(gpio.HIGH);
    outputs.bForward.write(gpio.HIGH);
  },
  reverse: (outputs) => {
    outputs.aForward.write(gpio.LOW);
    outputs.bForward.write(gpio.LOW);
    outputs.aReverse.write(gpio.HIGH);
    outputs.bReverse.write(gpio.HIGH);
  },
  right: (outputs) => {
    outputs.aForward.write(gpio.LOW);
    outputs.bReverse.write(gpio.LOW);
    outputs.aReverse.write(gpio.HIGH);
    outputs.bForward.write(gpio.HIGH);
  },
  left: (outputs) => {
    outputs.aReverse.write(gpio.LOW);
    outputs.bForward.write(gpio.LOW);
    outputs.aForward.write(gpio.HIGH);
    outputs.bReverse.write(gpio.HIGH);
  }
};