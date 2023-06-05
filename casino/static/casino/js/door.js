var level = 1
var door = 1

function changeLevel(max) {
  level = max;
}

function chooseDoor(max) {
  door = Math.round(Math.random() * max);
}

function itIsRealDoor() {
  alert("WIN");
  document.location.href = casinoRedirect;
}

function fakeDoor() {
  alert("LOSE")
  document.location.href = casinoRedirect;
}

function play(min, max) {
  document.getElementById("play").style = 'display: none;';
  chooseDoor(level-1);
  alert(door);
  for (let i = 0; i < level; i++){
    let newDoor = document.createElement('div');
    newDoor.classList.add('door');
    newDoor.style = `left: ${300+i*100}px`
    newDoor.addEventListener("click", (i==door) ? fakeDoor : itIsRealDoor );
    document.getElementById("game").appendChild(newDoor);
  }
}
