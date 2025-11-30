let menPage = document.getElementById("main_men");
let womenPage = document.getElementById("main_women");
let menSelect = document.getElementById("men_select");
let womenSelect = document.getElementById("women_select");
let menTitle = document.createElement("div");
let womenTitle = document.createElement("div");

//[men js content]---------------------------------------------------------------------------------------]

menTitle.textContent = "MEN";
    menTitle.style.position = "absolute";
    menTitle.style.top = "50%";
    menTitle.style.left = "40%";
    menTitle.style.transform = "translate(-40%, -0%)";
    menTitle.style.fontFamily = "sans-serif";
    menTitle.style.fontWeight = "bold";
    menTitle.style.fontSize = "10rem";  
    menTitle.style.color = "rgb(28,28,28)";
    menTitle.style.filter = "drop-shadow(0 0 1px rgb(255, 249, 227))";
    menTitle.style.zIndex = "10";

menSelect.appendChild(menTitle);

menTitle.addEventListener("mouseenter", () => {
    menPage.style.cursor = "pointer";
    menPage.style.transition = "filter 0.3s"; 
    menPage.style.filter = "grayscale(100%)";

});

menTitle.addEventListener("click", () => {
    console.log("men page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "men.html";
        } else {
            window.location.href = "src/pages/men.html";
        }
});

menPage.addEventListener("mouseenter", () => {
    menPage.style.cursor = "pointer";
    menPage.style.transition = "filter 0.3s"; 
    menPage.style.filter = "grayscale(100%)";

});


menPage.addEventListener("mouseleave", () => {
        menPage.style.filter = "grayscale(0%)";
        menPage.style.transition = "filter 0.3s"; 

    });

menPage.addEventListener("click", () => {
        console.log("men page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "men.html";
        } else {
            window.location.href = "src/pages/men.html";
        }
    });


//[women js content]---------------------------------------------------------------------------------------]

womenTitle.textContent = "WOMEN";
    womenTitle.style.position = "absolute";
    womenTitle.style.top = "50%";
    womenTitle.style.left = "28%";
    womenTitle.style.transform = "translate(-40%, -0%)";
    womenTitle.style.fontFamily = "sans-serif";
    womenTitle.style.fontWeight = "bold";
    womenTitle.style.fontSize = "10rem";  
    womenTitle.style.color = "rgb(28,28,28)";
    womenTitle.style.filter = "drop-shadow(0 0 1px rgb(255, 249, 227))";
    womenTitle.style.zIndex = "10";

womenSelect.appendChild(womenTitle);

womenTitle.addEventListener("mouseenter", () => {
    womenPage.style.cursor = "pointer";
    womenPage.style.transition = "filter 0.3s"; 
    womenPage.style.filter = "grayscale(100%)";

});

womenTitle.addEventListener("click", () => {
    console.log("men page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "women.html";
        } else {
            window.location.href = "src/pages/women.html";
        }
});

womenPage.addEventListener("mouseenter", () => {
    womenPage.style.cursor = "pointer";
    womenPage.style.transition = "filter 0.3s"; 
    womenPage.style.filter = "grayscale(100%)";

});


womenPage.addEventListener("mouseleave", () => {
        womenPage.style.filter = "grayscale(0%)";
        womenPage.style.transition = "filter 0.3s"; 

    });

womenPage.addEventListener("click", () => {
        console.log("men page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "women.html";
        } else {
            window.location.href = "src/pages/women.html";
        }
    });