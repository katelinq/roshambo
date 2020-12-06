// Haylee Quarles
// 12/05/2020
const choices = {
    1: "Opponent chose Rock...",
    2: "Opponent chose Paper...",
    3: "Opponent chose Scissors..."
}

var gameData = { 
    "data": {
        "ai_choice": 0,
        "input": "",
        "losses": 0,
        "outcome": "",
        "wins": 0
    }
}

function setHTML(id, html) {
    document.getElementById(id).innerHTML = html 
    if(id == 'error' && html !== '') {
        setHTML('outcome', '')
    }
}
function buildHTML() {
    return (
        "<p>" + choices[gameData.data.ai_choice] + "</p>" + 
        (gameData.data.outcome == 'win' ? "<p>You Won!</p>" : (gameData.data.outcome == 'lose' ? "<p>You Lost!</p>" : "<p>It was a draw!</p>")) +
        "<p>Wins: " + gameData.data.wins + "</p>" + 
        "<p>Losses: " + gameData.data.losses + "</p>"
    )
}

function callGame() {
    var input  = document.getElementById('input').value;
    if (input !== '' && input !== null) {
        gameData.data.input = input
        var url = "https://katelinq-roshambo-api.herokuapp.com/game";
        var testUrl = "http://127.0.0.1:5000/game"
    
        fetch(url, {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            headers: {
              'Content-Type': 'application/json'
              // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: JSON.stringify(gameData) // body data type must match "Content-Type" header
          })
            .then(function (response) {
                if (!response.ok) {
                    response.json().then(function(object) {
                        setHTML('error', object.message)
                      })
                }
                else {
                    response.json().then(function(data) {
                        gameData = data;
                        setHTML('error', '')
                        setHTML('outcome', buildHTML())
                    })
                }
            })
            .catch(function (err) {
                console.log(err);
            });
    }
    else {                        
        setHTML('error', 'Please enter a guess.')
    }
    
}
document.getElementById('play-btn').addEventListener("click", callGame); 
