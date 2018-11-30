var canvas = document.getElementById("maze");
var context = canvas.getContext("2d");
context.globalCompositeOperation = 'screen';

context.strokeStyle = "#fff"

var keyMap = 0;
var keys = {
  '65':1,         // left
  '87':2,         // up
  '68':4,         // right
  '83':8,          // down
  
  '82':16,        // Red button
  '71':32,        // green button
  '66':64         // Red button
}

var tileSize = 20;
var rows = 240/tileSize;
var columns = 320/tileSize;

var paddingR = {x: tileSize, y: tileSize};
var paddingG = {x: tileSize, y: tileSize};
var paddingB = {x: tileSize, y: tileSize};

var matrixR = [];
var matrixB = [];
var matrixG = [];
var colors = {
  "000": "#222",
  "001": "#0000ff",
  "010": "#00ff00",
  "100": "#ff0000",
  "011": "#66ffff",
  "101": "#ff66ff",
  "110": "#ffff66",
  "111": "#ffffff"
};

var activeR = false;
var activeG = false;
var activeB = false;

var maze = [
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,4,0,0,4,0,0,0,4,0,0],
  [0,1,1,4,4,4,5,4,4,0,4,4,0,0],
  [0,1,1,1,5,7,5,5,0,6,0,4,0,0],
  [0,4,5,4,5,2,3,7,2,2,0,4,0,0],
  [0,0,1,0,4,3,1,5,1,3,0,4,0,0],
  [0,0,1,1,5,7,7,4,6,6,4,4,0,0],
  [0,0,3,0,4,2,1,3,0,2,2,0,0,0],
  [0,0,3,2,2,2,2,0,2,2,2,0,0,0],
  [0,0,1,0,0,2,0,0,0,2,0,0,0,0]
];

var redButton = document.getElementById("red");
redButton.onclick = toggleRedChannel;

var greenButton = document.getElementById("green");
greenButton.onclick = toggleGreenChannel; 

var blueButton = document.getElementById("blue");
blueButton.onclick = toggleBlueChannel; 

function toggleRedChannel(){
  activeR = !activeR;
  redButton.className = activeR?"on":"off";
}
function toggleGreenChannel(){
  activeG = !activeG;
  greenButton.className = activeG?"on":"off";
}
function toggleBlueChannel() {
  activeB = !activeB;
  blueButton.className = activeB?"on":"off";
}

var buttonChannels = [0,0,0]
function checkToggleChannels(){
  if(keyMap&keys['82'] ){
    if(buttonChannels[0]==0){
      buttonChannels[0] = 1;
      toggleRedChannel();
    }
  } else {
    buttonChannels[0] = 0;
  }

  if(keyMap&keys['71'] ){
    if(buttonChannels[1]==0){
      buttonChannels[1] = 1;
      toggleGreenChannel();
    }
  } else {
    buttonChannels[1] = 0;
  }

  if(keyMap&keys['66'] ){
    if(buttonChannels[2]==0){
      buttonChannels[2] = 1;
      toggleBlueChannel();
    }
  } else {
    buttonChannels[2] = 0;
  }
}

for(var j = 0; j<rows-2; j++) {
  matrixR.push([]);
  matrixG.push([]);
  matrixB.push([]);
  for(var i = 0; i<columns-2; i++){
    var mazeValue = maze[j][i];
    var r = 0;
    var g = 0;
    var b = 0;
    r = mazeValue>>2;
    g = (mazeValue&2)>>1;
    b = mazeValue&1;
    matrixR[j].push({
      i: i,
      j: j,
      color: getColorCode(["000","100"][r])
    });
    matrixG[j].push({
      i: i,
      j: j,
      color: getColorCode(["000","010"][g])
    });
    matrixB[j].push({
      i: i,
      j: j,
      color: getColorCode(["000","001"][b])
    });
  }
}

function draw() {
  context.clearRect(0, 0, 320, 240);

    context.save()
    var rx = Math.floor((~~paddingR.x)/5)*5;
    var ry = Math.floor((~~paddingR.y)/5)*5;
    context.translate(rx, ry);
    context.fillStyle = colors["100"];
    for(var j = 0; j<matrixR.length; j++){
      for(var i = 0; i<matrixR[j].length; i++){
        drawMatrixElement(matrixR[j][i]);
      }
    }
    context.restore();

    context.save()
    var gx = Math.floor((~~paddingG.x)/5)*5;
    var gy = Math.floor((~~paddingG.y)/5)*5;
    context.translate(gx, gy);
    context.fillStyle = colors["010"];
    for(var j = 0; j<matrixG.length; j++){
      for(var i = 0; i<matrixG[j].length; i++){    
        drawMatrixElement(matrixG[j][i]);      
      }
    }
    context.restore();

    context.save()
    var bx = Math.floor((~~paddingB.x)/5)*5;
    var by = Math.floor((~~paddingB.y)/5)*5;
    context.translate(bx, by);
    context.fillStyle = colors["001"];
    for(var j = 0; j<matrixB.length; j++){
      for(var i = 0; i<matrixB[j].length; i++){
        drawMatrixElement(matrixB[j][i]);
      }
    }
    context.restore()
  
}
 
function drawMatrixElement(element) {
  if(element.color!="000"){    
    context.fillRect(tileSize*element.i, tileSize*element.j, tileSize, tileSize);
  }
}

function updateElementColor(element, delta){
  element.timeout -= delta;
  if(element.timeout<=0){
    element.color = getColorCode(~~(Math.random()*8));
    element.timeout = 100;
  }
  
}

function getColorCode(value){
  var binary = value.toString(2);
  if(binary.length<3){
    binary = "0" + binary;
  }
  if(binary.length<3){
    binary = "0" + binary;
  }
  return binary;
}

function update(delta, time) {
  checkToggleChannels()
  move(delta)
  checkSolution();
}

var lastTime = 0;
function loop(time) {
  var delta = time - lastTime;
  lastTime = time;
  update(delta, time);
  draw();
  requestAnimationFrame(loop);
}

loop(0);

console.log("updated")

document.onkeydown = function(e){
  var key = e.keyCode|| e.which;
  console.log(key);
  if(keys[key]){
    keyMap|=keys[key];
    e.preventDefault();
  }
}

document.onkeyup = function(e){
  var key = e.keyCode ? e.keyCode : e.which;
  if(keyMap&keys[key]){
    keyMap^=keys[key];
    e.preventDefault();
  }
}

function move(delta) {
  var x = 0;
  var y = 0
  if(keyMap&keys['65']){
     x -= delta*0.1;  
  }
  if(keyMap&keys['68']){
    x += delta*0.1;  
  }
  if(keyMap&keys['87']){
     y -= delta*0.1;  
  }
  if(keyMap&keys['83']){
    y += delta*0.1;  
  }
  if(activeR){
    paddingR.x += x;
    paddingR.y += y;
  }
    if(activeG){
    paddingG.x += x;
    paddingG.y += y;
  }
    if(activeB){
    paddingB.x += x;
    paddingB.y += y;
  }
}

function checkSolution() {
  var rx = Math.floor((~~paddingR.x)/5)*5;
  var ry = Math.floor((~~paddingR.y)/5)*5;
  var gx = Math.floor((~~paddingG.x)/5)*5;
  var gy = Math.floor((~~paddingG.y)/5)*5;
  var bx = Math.floor((~~paddingB.x)/5)*5;
  var by = Math.floor((~~paddingB.y)/5)*5;
  
  var a = (gx - rx) == 40;
  var b = (gy - ry) == -80;
  var c = (bx - rx) == 100;
  var d = (by - ry) == -20;
  if (a && b && c && d) {
    console.log("WIN");
    document.getElementById("win").className = "";
  }
}