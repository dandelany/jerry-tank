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


const socketCluster = require('socketcluster-client');

const socket = socketCluster.connect({hostname: 'Dans-MacBook-Pro-2.local', port: '9494'});

socket.on('connect', (data, res) => {
  console.log('connected', data, res);
});

socket.emit('sampleClientEvent', {message: 'Event from Jerry Tank!'});

const driveChannel = socket.subscribe('drive');

driveChannel.watch((data) => {
  console.log('drive channel action!');
  console.log(data);
});