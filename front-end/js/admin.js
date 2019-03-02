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