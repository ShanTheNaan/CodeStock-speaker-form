function login_with_email() {
    let email = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    firebase.auth().signInWithEmailAndPassword(email, password)
    .catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    if (errorCode === 'auth/wrong-password') {
        alert('Wrong password.');
    } else {
        alert(errorMessage);
    }
    console.log(error);
    });
}

function createUser () {
    let email = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    firebase.auth().createUserWithEmailAndPassword(email, password)
    .catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    if (errorCode == 'auth/weak-password') {
        alert('The password is too weak.');
    } else {
        alert(errorMessage);
    }
    console.log(error);
    });
}

firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
        localStorage.setItem('uid', user.getIdToken());
        window.location = 'admin.html';
    } 
});
