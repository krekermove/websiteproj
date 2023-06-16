var level = 3;
var door = 1;
var Flag = false;

function changeLevel(max) {
  level = max;
}

function chooseDoor(max) {
  door = Math.round(Math.random() * max);
}

function someDoor(id) {
  if(Flag){
    return;
  }
  if(id == door){
    document.getElementById("textM").textContent = 'LOSE!'
    document.getElementById(id).classList.add('lose');
  }
  else{
    document.getElementById("textM").textContent = 'WIN!ник'
    var win = Math.round(Math.random() * 2)+1;
    document.getElementById(id).classList.add(`win_${win}`);
  }
  Flag = true;
  setTimeout(function() {
    document.location.href = casinoRedirect;
  }, 4000)
}

function play(min, max) {
  document.getElementById("play").style = 'display: none;';
  document.getElementById("listDoor").style = 'display: none;';
  chooseDoor(level-1);
  for (let i = 0; i < level; i++){
    let newDoor = document.createElement('div');
    newDoor.id = i;
    newDoor.classList.add('door');
    newDoor.style = `left: ${500+i*300}px`;
    newDoor.addEventListener("click", () => someDoor(newDoor.id));
    document.getElementById("game").appendChild(newDoor);
  }
}
