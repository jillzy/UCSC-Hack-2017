/**
 * Created by jy on 1/21/2017.
 */
var canChat;
var user;

function initChat(user) {
    // Get a Firebase Database ref
    var chatRef = firebase.database().ref("chat");

    // Create a Firechat instance
    var chat = new FirechatUI(chatRef, document.getElementById("firechat-wrapper"));

    // Set the Firechat user
    chat.setUser(user.uid, user.displayName);
}

function setFlag(){
    if (firebase.auth().currentUser) {
        canChat = true;
        console.log("should instantiate now");
    }
}

function startChat() {
    console.log("wtf");
    if (firebase.auth().currentUser && canChat) {
        initChat(user);
        console.log(user, " wants to start chat");
    }
}
function login() {

        user = firebase.auth().currentUser;

        if(user) {
            canChat = true;
            console.log("already logged in");
        } else {
            var provider = new firebase.auth.GoogleAuthProvider();
            firebase.auth().signInWithRedirect(provider).then(function(result) {

                    // This gives you a Google Access Token. You can use it to access the Google API.
                    var token = result.credential.accessToken;
                    // The signed-in user info.
                    var user = result.user;
                    console.log(user);
                    // ...
                }).catch(function(error) {
                // Handle Errors here.
                var errorCode = error.code;
                var errorMessage = error.message;
                console.log(errorCode);
                console.log(errorMessage);
                // The email of the user's account used.
                var email = error.email;
                // The firebase.auth.AuthCredential type that was used.
                var credential = error.credential;
                // ...
            });
        }
}

console.log("new instance");