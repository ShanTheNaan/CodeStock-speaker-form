function setUploadFile() {
    var element = document.getElementById("csv-div");
    element.style.display = "block";
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

    createCard("na lcs lit", "mike mee", "my house", "any", "123");
    createCard("lck sux", "nick bruh", "korea", "never", "093");
    createCard("LEC lit", "rando lando", "neverland", "12:12", "10294");
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

    outterDiv.className += "col s6 m4 offset-m1";
    card.className += "card";
    cardContent.className += "card-content";
    cardTitle.className += "card-title";
    cardTitle.innerText += title;
    cardAction.className += "card-action";
    speak.innerHTML = speaker;
    loc.innerText = location;
    date.innerText = time;
    qrlink.innerText = "QR-Code";
    qrlink.href = "qrCode.html?uid="+uid+"&title="+title+"&speaker="+speaker+"&location="+location;
    fform.innerText = "Feedback Form";

    cardAction.appendChild (qrlink);
    cardAction.appendChild (fform);
    cardContent.appendChild (cardTitle);
    cardContent.appendChild (speak);
    cardContent.appendChild (loc);
    cardContent.appendChild (date);
    card.appendChild (cardContent);
    card.appendChild (cardAction);
    outterDiv.appendChild (card);

    document.getElementById("events-div").appendChild(outterDiv);
}

