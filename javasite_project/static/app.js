function changeText(id) {
    id.innerHTML = "you have changed this text with an 'onclick' event";
}

function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}

function checkCookies() {
    let text = ""
    if (navigator.cookiesEnabled == true) {
        text = "cookies are enabled";
    } else {
        text = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = text;
}

function mOver(obj) {
    obj.innerHTML = "<br> HELLO";
}

function mOut(obj) {
    obj.innerHTML = "";
}


function sendAlert() {
    alert(location.hostname);
}

// function for toggling a different colour scheme (in this case a dark mode)
// mainBox/ Text are setting variables in js based on class names in the html
// button is used for determining the text that appears on the button 'light or 
// dark mode' to indicate it will change to the opposite theme
function darkMode() {
    let element = document.body;
    let mainBox = document.getElementsByClassName("main-box");
    let mainText = document.getElementsByClassName("main-text");
    let state = localStorage.getItem("state");
    let button = document.getElementById("mode-button");

// dark-mode, dark-modeb and dark-modec refer to diff sections in css for being
// able to set different colours/ themes/ styles on different parts 
// (js variables from the html classes above)
    element.classList.toggle("dark-mode");
    for (const box of mainBox) {
        box.classList.toggle("dark-modeb");
    }
    for (const text of mainText) {
        text.classList.toggle("dark-modec");
    }

// checks the state (the last variable set at the top) of the current theme
// to store this information in local storage, to remember the user setting
// this updates everytime the user presses the dark mode button
    if (state !=="dark") {
        localStorage.setItem("state", "dark");
        button.textContent='Light Mode';
    } else {
        localStorage.setItem("state", "light");
        button.textContent='Dark Mode';
    }
}

// similar code to above in this case, it's now checking for if there is state
// in the local storage through .getItem()
function darkCheck() {
    let element = document.body;
    let mainBox = document.getElementsByClassName("main-box");
    let mainText = document.getElementsByClassName("main-text");
    let state = localStorage.getItem("state");
    let button = document.getElementById("mode-button");

    if (state =="dark") {
        element.classList.toggle("dark-mode");
        button.textContent='Light Mode';

        for (const box of mainBox) {
            box.classList.toggle("dark-modeb");
        }
        for (const text of mainText) {
            text.classList.toggle("dark-modec");
        }
    } else {
        button.textContent='Dark Mode';
    }
}
