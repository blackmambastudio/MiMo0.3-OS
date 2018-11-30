// WebSocket Setup
var domain = document.domain;
var port = location.port;
var socket = io.connect('http://' + domain + ':' + port);
var mimo_buttons = {
  'r': 'red',
  'g': 'green',
  'b': 'blue'
}

socket.on('connect', function() {
  socket.emit('connect2pi', {
    data: 'Let me in...'
  });
});

socket.on('serial', function(response) {
  if (typeof response.type !== 'undefined') {
    document.querySelector('.content > h3').innerText = 'Connected';
    // var data = document.createElement('p');
    // data.innerText = 'Button pressed: ' + response.button;
    var data = 'Button pressed: ' + mimo_buttons[response.button];
    // document.querySelector('.content > .data').appendChild(data);
    document.querySelector('.content > .data').innerText = data;

    if (response.button === 'r') {
      //toggleRedChannel();
    } 

    if (response.button === 'g') {
      //toggleGreenChannel();
    }

    if (response.button === 'b') {
      //toggleBlueChannel();
    }
  }
});