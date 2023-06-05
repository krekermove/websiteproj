var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");

var character = new Image();
var cactus = new Image();
var bg = new Image();

character.src = pathToCharacter;
cactus.src = pathToCactus;
bg.src = pathToBg;

function draw(){
    ctx.drawImage(bg, 0, 0);
    ctx.drawImage(character, 0, 150, 200, 200);

    ctx.drawImage(cactus, 150, 0)

    requestAnimationFrame(draw);
}

bg.onload = draw;



var gap = 90;

// При нажатии на какую-либо кнопку
document.addEventListener("keydown", moveUp);

function moveUp() {
 yPos -= 120;
 fly.play();
}

// Создание блоков
var cactus = [];

cactus[0] = {
 x : cvs.width,
 y : 0
}

var score = 0;
// Позиция капибары
var xPos = 10;
var yPos = 150;
var grav = 1.5;

function draw() {
     ctx.drawImage(bg, 0, 0);

     for(var i = 0; i < cactus.length; i++) {
     ctx.drawImage(cactus, cactus[i].x, cactus[i].y);

     cactus[i].x--;

     if(cactus[i].x == 125) {
     cactus.push({
     x : cvs.width,
     y : Math.floor(Math.random() * cactus.height) - cactus.height
     });
     }

     // Отслеживание прикосновений
     if(xPos + character.width >= cactus[i].x
     && xPos <= cactus[i].x + cactus.width
     && (yPos <= cactus[i].y + cactus.height
     || yPos + character.height >= cactus[i].y + cactus.height + gap)) {
     location.reload(); // Перезагрузка страницы
     }

     if(pipe[i].x == 5) {
     score++;
     score_audio.play();
     }
     }

     ctx.drawImage(fg, 0, cvs.height - fg.height);
     ctx.drawImage(bird, xPos, yPos);

     yPos += grav;

     ctx.fillStyle = "#000";
     ctx.font = "24px Verdana";
     ctx.fillText("Счет: " + score, 10, cvs.height - 20);

     requestAnimationFrame(draw);
}

pipeBottom.onload = draw;