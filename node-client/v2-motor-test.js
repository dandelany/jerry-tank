var raspi = require('raspi');
var gpio = require('raspi-gpio');
var SoftPWM = require('raspi-soft-pwm').SoftPWM;

const outPins = {
  'enable': 14, // STBY
  'aForward': 15, // AIN1
  'aReverse': 18, // AIN2
  'bForward': 4, // BIN1 (backwards?)
  'bReverse': 3 // BIN2
};

const pwmPins = {
  'aSpeed': 17, // PWMA
  'bSpeed': 2, // PWMB
};

//
// GPIO.output(pins['a_forward'], 0);
// GPIO.output(pins['a_reverse'], 0);
// GPIO.output(pins['b_forward'], 0);
// GPIO.output(pins['b_reverse'], 0);
//
// def drive_forward(pins):
// GPIO.output(pins['a_forward'], 1);
// GPIO.output(pins['b_forward'], 1);
//
// def drive_reverse(pins):
// GPIO.output(pins['a_reverse'], 1);
// GPIO.output(pins['b_reverse'], 1);
//
// def drive_left_spin(pins):
// GPIO.output(pins['a_forward'], 1);
// GPIO.output(pins['b_reverse'], 1);
//
// def drive_right_spin(pins):
// GPIO.output(pins['b_forward'], 1);

function driveStop(outputs) {
  outputs.aForward.write(gpio.LOW);
  outputs.aReverse.write(gpio.LOW);
  outputs.bForward.write(gpio.LOW);
  outputs.bReverse.write(gpio.LOW);
}
function driveForward(outputs) {
  outputs.aReverse.write(gpio.LOW);
  outputs.bReverse.write(gpio.LOW);
  outputs.aForward.write(gpio.HIGH);
  outputs.bForward.write(gpio.HIGH);
}

raspi.init(function() {
  const outputs = {};
  Object.keys(outPins).forEach(key => {
    outputs[key] = new gpio.DigitalOutput(`GPIO${outPins[key]}`);
  });
  const pwms = {};
  Object.keys(pwmPins).forEach(key => {
    pwms[key] = new SoftPWM(`GPIO${pwmPins[key]}`);
  });

  pwms.aSpeed.write(60);
  pwms.bSpeed.write(60);

  outputs.enable.write(GPIO.HIGH);

  driveForward(outputs);
  setTimeout(() => {
    driveStop(outputs);
    outputs.enable.write(GPIO.LOW);
  }, 1000);
});