var level = 3
var door = 1

function changeLevel(max) {
  level = max;
}

function chooseDoor(max) {
  door = Math.round(Math.random() * max);
}

function someDoor(id) {
  if(id == door){
    document.getElementById("textMessage").textContent = 'LOSE!'
    document.getElementById(id).classList.add('lose');
  }
  else{
    document.getElementById("textMessage").textContent = 'WIN!'
    document.getElementById(id).classList.add('win');
  }
  setTimeout(function() {
    document.location.href = casinoRedirect;
  }, 3000)
}

function play(min, max) {
  document.getElementById("play").style = 'display: none;';
  document.getElementById("listDoor").style = 'display: none;';
  chooseDoor(level-1);
  alert(door);
  for (let i = 0; i < level; i++){
    let newDoor = document.createElement('div');
    newDoor.id = i;
    newDoor.classList.add('door');
    newDoor.style = `left: ${300+i*300}px`;
    newDoor.addEventListener("click", () => someDoor(newDoor.id));
    document.getElementById("game").appendChild(newDoor);
  }
}
