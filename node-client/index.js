const raspi = require('raspi');
const gpio = require('raspi-gpio');
const SoftPWM = require('raspi-soft-pwm').SoftPWM;
const socketCluster = require('socketcluster-client');

const {outPins, pwmPins} = require('./pins');

const drive = require('./drive');


function initGPIO(outPins, pwmPins) {
  const outputs = {};
  Object.keys(outPins).forEach(key => {
    outputs[key] = new gpio.DigitalOutput(`GPIO${outPins[key]}`);
  });
  const pwms = {};
  Object.keys(pwmPins).forEach(key => {
    pwms[key] = new SoftPWM({pin: `GPIO${pwmPins[key]}`, range: 100});
  });
  return {outputs, pwms};
}


function main() {
  const {outputs, pwms} = initGPIO(outPins, pwmPins);
  pwms.aSpeed.write(70);
  pwms.bSpeed.write(70);

  const socket = socketCluster.connect({hostname: 'Dans-MacBook-Pro-2.local', port: '9494'});
  socket.on('connect', () => console.log('connected!'));

  const driveChannel = socket.subscribe('drive');

  driveChannel.watch((data) => {
    console.log('drive channel action!');
    console.log(data);
    if (data && data.msg && drive[data.msg]) {
      drive[data.msg](outputs);
    }
  });
}

raspi.init(main);






