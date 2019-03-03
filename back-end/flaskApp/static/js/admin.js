function setUploadFile() {
    var element = document.getElementById("csv-div");
    element.style.display = "block";
    document.getElementById("events-div").style.display = "none";
    document.getElementById("upload").classList.add("active");
    document.getElementById("events").classList.remove("active");
}

function sendCsv() {
    // Make post request
    document.getElementById("csv-div").style.display = "none";
    document.getElementById("events-div").style.display = "block";
    document.getElementById("events").classList.add("active");
    document.getElementById("upload").classList.remove("active");
}

function displayEvents() {
    document.getElementById("csv-div").style.display = "none";
    document.getElementById("events-div").style.display = "block";
    document.getElementById("events").classList.add("active");
    document.getElementById("upload").classList.remove("active");
}

function createCard (title, speaker, location, time, uid) {
    var outterDiv = document.createElement("div");
    var card = document.createElement("div");
    var cardContent = document.createElement("div");
    var cardTitle = document.createElement("span");
    var speak = document.createElement("p");
    var loc = document.createElement("p");
    var date = document.createElement("p");
    var cardAction = document.createElement("div");
    var qrlink = document.createElement("a");
    var fform = document.createElement("a");
    var feed = document.createElement ("a");

    outterDiv.className += "col s6 m4 offset-m1";
    card.className += "card";
    cardContent.className += "card-content";
    cardTitle.className += "card-title";
    cardTitle.innerText += title;
    cardAction.className += "card-action";
    speak.innerHTML = speaker;
    loc.innerText = location;
    date.innerText = time;
    qrlink.innerText = "QR";
    qrlink.href = "qr?uid="+uid+"&title="+title+"&speaker="+speaker+"&location="+location;
    fform.innerText = "Form";
    fform.href = "feedback/"+uid;
    feed.innerText = "Feedback";
    feed.href = "";


    cardAction.appendChild (qrlink);
    cardAction.appendChild (fform);
    cardAction.appendChild (feed);
    cardContent.appendChild (cardTitle);
    cardContent.appendChild (speak);
    cardContent.appendChild (loc);
    cardContent.appendChild (date);
    card.appendChild (cardContent);
    card.appendChild (cardAction);
    outterDiv.appendChild (card);

    document.getElementById("events-div").appendChild(outterDiv);
}

var getJSON = function(url) {
    var data = null;

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
    if (this.readyState === 4) {
        var json = this.responseText;
    
        json = JSON.parse(json);
        console.log(json);

        for (var uid in json){
            console.log(uid);
            console.log(json[uid]);
            let title = json[uid][0];
            let loc = json[uid][1];
            let date = json[uid][2];
            let speaker = json[uid][3];

            createCard (title, speaker, loc, date, uid);

            // createCard("na lcs lit", "mike mee", "my house", "any", "123");
            // createCard("lck sux", "nick bruh", "korea", "never", "093");
            // createCard("LEC lit", "rando lando", "neverland", "12:12", "10294");
        }
    }
    });

    xhr.open("GET", url);
    xhr.setRequestHeader("Cache-Control", "no-cache");
    xhr.setRequestHeader("Postman-Token", "f929304d-328e-4c92-a0e1-12c49f2824b6");

    xhr.send(data);
}

getJSON("http://localhost:5000/events");

