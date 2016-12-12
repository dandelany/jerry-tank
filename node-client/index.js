const socketCluster = require('socketcluster-client');

const socket = socketCluster.connect({hostname: 'Dans-MacBook-Pro-2.local', port: '8000'});

socket.on('connect', (data, res) => {
  console.log('connected', data, res);
});

socket.emit('sampleClientEvent', {message: 'Event from Jerry Tank!'});

