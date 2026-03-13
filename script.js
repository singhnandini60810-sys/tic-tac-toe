let board=["","","","","","","","",""];
let currentPlayer="X";
let gameActive=false;

let xScore=0;
let oScore=0;

let vsComputer=false;

const winPatterns=[
[0,1,2],
[3,4,5],
[6,7,8],
[0,3,6],
[1,4,7],
[2,5,8],
[0,4,8],
[2,4,6]
];

function startGame(){

let mode=document.getElementById("mode").value;
vsComputer = mode === "ai";

gameActive=true;
document.getElementById("status").innerText="Player X Turn";

}

function play(index){

if(!gameActive || board[index]!="") return;

makeMove(index,currentPlayer);

if(checkWin(currentPlayer)){

updateScore(currentPlayer);
highlightWin(currentPlayer);

document.getElementById("status").innerText=currentPlayer+" Wins!";
gameActive=false;
return;

}

if(!board.includes("")){

document.getElementById("status").innerText="Draw!";
gameActive=false;
return;

}

switchPlayer();

if(vsComputer && currentPlayer==="O" && gameActive){
setTimeout(computerMove,400);
}

}

function makeMove(index,player){

board[index]=player;

let cell=document.getElementsByClassName("cell")[index];
cell.innerText=player;
cell.disabled=true;

}

function switchPlayer(){

currentPlayer=currentPlayer==="X"?"O":"X";
document.getElementById("status").innerText="Player "+currentPlayer+" Turn";

}

function checkWin(player){

return winPatterns.some(pattern =>
pattern.every(i => board[i]===player)
);

}

function highlightWin(player){

for(let pattern of winPatterns){

if(pattern.every(i=>board[i]===player)){

pattern.forEach(i=>{
document.getElementsByClassName("cell")[i].classList.add("win");
});

}

}

}

function computerMove(){

let empty=board
.map((v,i)=>v==""?i:null)
.filter(v=>v!==null);

let move=empty[Math.floor(Math.random()*empty.length)];

play(move);

}

function updateScore(player){

if(player==="X"){
xScore++;
document.getElementById("xScore").innerText=xScore;
}else{
oScore++;
document.getElementById("oScore").innerText=oScore;
}

}

function resetGame(){

board=["","","","","","","","",""];
currentPlayer="X";
gameActive=true;

let cells=document.getElementsByClassName("cell");

for(let cell of cells){
cell.innerText="";
cell.disabled=false;
cell.classList.remove("win");
}

document.getElementById("status").innerText="Player X Turn";

}
