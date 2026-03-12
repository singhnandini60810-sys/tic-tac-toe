<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Tic Tac Toe for Kids</title>

<style>
body {
    margin: 0;
    height: 100vh;
    background: linear-gradient(135deg, #ffecd2, #fcb69f);
    font-family: "Comic Sans MS", Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    background: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    width: 330px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

h1 {
    color: #ff6f61;
    margin-bottom: 10px;
}

#status {
    font-size: 20px;
    margin: 15px 0;
    color: #444;
}

.board {
    display: grid;
    grid-template-columns: repeat(3, 90px);
    gap: 10px;
    justify-content: center;
    margin: 20px 0;
}

.cell {
    width: 90px;
    height: 90px;
    font-size: 40px;
    border-radius: 15px;
    border: none;
    background: #cce7ff;
    cursor: pointer;
    transition: transform 0.2s, background 0.2s;
}

.cell:hover {
    transform: scale(1.05);
    background: #b3dcff;
}

.cell:disabled {
    cursor: default;
}

button.main-btn {
    padding: 10px 20px;
    font-size: 18px;
    border-radius: 25px;
    border: none;
    cursor: pointer;
    margin-top: 10px;
    background: #ff6f61;
    color: white;
}

button.main-btn:hover {
    background: #ff3d2e;
}

.hidden {
    display: none;
}

.win {
    color: #2ecc71;
    font-size: 22px;
}

.draw {
    color: #f39c12;
    font-size: 22px;
}
</style>
</head>

<body>

<div class="container">
    <h1>🎮 Tic Tac Toe 🎮</h1>

    <div id="status">Click Start to Play!</div>

    <div class="board hidden" id="board">
        <button class="cell" onclick="play(0)"></button>
        <button class="cell" onclick="play(1)"></button>
        <button class="cell" onclick="play(2)"></button>
        <button class="cell" onclick="play(3)"></button>
        <button class="cell" onclick="play(4)"></button>
        <button class="cell" onclick="play(5)"></button>
        <button class="cell" onclick="play(6)"></button>
        <button class="cell" onclick="play(7)"></button>
        <button class="cell" onclick="play(8)"></button>
    </div>

    <button class="main-btn" id="startBtn" onclick="startGame()">Start Game</button>
    <button class="main-btn hidden" id="playAgainBtn" onclick="resetGame()">Play Again</button>
</div>

<script>
let board = ["","","","","","","","",""];
let currentPlayer = "X";
let active = false;

const winPatterns = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
];

function startGame() {
    active = true;
    document.getElementById("board").classList.remove("hidden");
    document.getElementById("startBtn").classList.add("hidden");
    document.getElementById("status").innerText = "Player X's Turn 😊";
}

function play(index) {
    if (!active || board[index] !== "") return;

    board[index] = currentPlayer;
    const cell = document.getElementsByClassName("cell")[index];
    cell.innerText = currentPlayer;
    cell.disabled = true;
    cell.style.background = currentPlayer === "X" ? "#ffb3ba" : "#baffc9";

    if (checkWin()) {
        document.getElementById("status").innerHTML =
            `<span class="win">🎉 Player ${currentPlayer} Wins! 🎉</span>`;
        endGame();
        return;
    }

    if (!board.includes("")) {
        document.getElementById("status").innerHTML =
            `<span class="draw">😲 It's a Draw!</span>`;
        endGame();
        return;
    }

    currentPlayer = currentPlayer === "X" ? "O" : "X";
    document.getElementById("status").innerText =
        `Player ${currentPlayer}'s Turn 😊`;
}

function checkWin() {
    return winPatterns.some(p =>
        p.every(i => board[i] === currentPlayer)
    );
}

function endGame() {
    active = false;
    document.getElementById("playAgainBtn").classList.remove("hidden");
}

function resetGame() {
    board = ["","","","","","","","",""];
    currentPlayer = "X";
    active = true;

    const cells = document.getElementsByClassName("cell");
    for (let cell of cells) {
        cell.innerText = "";
        cell.disabled = false;
        cell.style.background = "#cce7ff";
    }

    document.getElementById("status").innerText = "Player X's Turn 😊";
    document.getElementById("playAgainBtn").classList.add("hidden");
}
</script>

</body>
</html>
