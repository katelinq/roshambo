var gameData = { 
    "data": {
        "ai_choice": 0,
        "input": "scissors",
        "losses": 0,
        "outcome": "",
        "wins": 0
    }
}

async function callGame() {
    console.log("init", gameData)
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
        return response.json();
        })
        .then(function (data) {
            gameData = data;
            console.log("after", gameData)
        })

        .catch(function (err) {
            console.log(err);
        });
}

callGame()