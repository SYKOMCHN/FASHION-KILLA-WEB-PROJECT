let menPage = document.getElementById("main_men");
let womenPage = document.getElementById("main_women");
let youthPage = document.getElementById("main_youth");
let dealsPage = document.getElementById("main_deals");
let stylePage = document.getElementById("main_style");
let endPage = document.getElementById("main-end");
let menSelect = document.getElementById("men_select");
let styleSelect = document.getElementById("styles_select");
let womenSelect = document.getElementById("women_select");
let youthSelect = document.getElementById("youth_select");
let dealsSelect = document.getElementById("deals_select");
let endSelect = document.getElementById("end_select");
let menTitle = document.createElement("div");
let womenTitle = document.createElement("div");
let youthTitle = document.createElement("div");
let dealsTitle = document.createElement("div");
let styleTitle = document.createElement("div");
let endTitle = document.createElement("div");

//[men js content]---------------------------------------------------------------------------------------]

menTitle.textContent = "MEN";
    menTitle.style.position = "absolute";
    menTitle.style.top = "50%";
    menTitle.style.left = "50%";
    menTitle.style.transform = "translate(-50%, -50%)";
    menTitle.style.fontFamily = "sans-serif";
    menTitle.style.fontWeight = "bold";
    menTitle.style.fontSize = "10rem";  
    menTitle.style.color = "rgb(247, 246, 243)";
    menTitle.style.filter = "drop-shadow(0 0 1px rgb(255, 249, 227))";
    menTitle.style.zIndex = "10";

menSelect.appendChild(menTitle);

menTitle.addEventListener("mouseenter", () => {
    menPage.style.cursor = "pointer";
    menPage.style.transition = "filter 0.3s, transform 0.3s"; 
    menPage.style.filter = "grayscale(100%)";
    menPage.style.transform = "scale(0.95)";

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
    menPage.style.transition = "filter 0.3s, transform 0.3s"; 
    menPage.style.filter = "grayscale(100%)";
    menPage.style.transform = "scale(0.95)";
});

menPage.addEventListener("mouseleave", () => {
    menPage.style.filter = "grayscale(0%)";
    menPage.style.transform = "scale(1)";
    menPage.style.transition = "filter 0.3s, transform 0.3s"; 
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
    womenTitle.style.left = "50%";
    womenTitle.style.transform = "translate(-50%, -50%)";
    womenTitle.style.fontFamily = "sans-serif";
    womenTitle.style.fontWeight = "bold";
    womenTitle.style.fontSize = "10rem";  
    womenTitle.style.color = "rgb(247, 246, 243)";
    womenTitle.style.filter = "drop-shadow(0 0 1px rgb(255, 249, 227))";
    womenTitle.style.zIndex = "10";

womenSelect.appendChild(womenTitle);

womenTitle.addEventListener("mouseenter", () => {
    womenPage.style.cursor = "pointer";
    womenPage.style.transition = "filter 0.3s, transform 0.3s"; 
    womenPage.style.filter = "grayscale(100%)";
    womenPage.style.transform = "scale(0.95)";

});

womenTitle.addEventListener("click", () => {
    console.log("women page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "women.html";
        } else {
            window.location.href = "src/pages/women.html";
        }
});

womenPage.addEventListener("mouseenter", () => {
    womenPage.style.cursor = "pointer";
    womenPage.style.transition = "filter 0.3s, transform 0.3s"; 
    womenPage.style.filter = "grayscale(100%)";
    womenPage.style.transform = "scale(0.95)";
});

womenPage.addEventListener("mouseleave", () => {
    womenPage.style.filter = "grayscale(0%)";
    womenPage.style.transform = "scale(1)";
    womenPage.style.transition = "filter 0.3s, transform 0.3s"; 
});

womenPage.addEventListener("click", () => {
        console.log("women page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "women.html";
        } else {
            window.location.href = "src/pages/women.html";
        }
    });

//[youth js content]---------------------------------------------------]
youthTitle.textContent = "YOUTH";
    youthTitle.style.position = "absolute";
    youthTitle.style.top = "50%";
    youthTitle.style.left = "50%";
    youthTitle.style.transform = "translate(-50%, -50%)";
    youthTitle.style.fontFamily = "sans-serif";
    youthTitle.style.fontWeight = "bold";
    youthTitle.style.fontSize = "10rem";  
    youthTitle.style.color = "rgb(247, 246, 243)";
    youthTitle.style.filter = "drop-shadow(0 0 1px rgb(255, 249, 227))";
    youthTitle.style.zIndex = "10";

youthSelect.appendChild(youthTitle);

youthTitle.addEventListener("mouseenter", () => {
    youthPage.style.cursor = "pointer";
    youthPage.style.transition = "filter 0.3s, transform 0.3s"; 
    youthPage.style.filter = "grayscale(100%)";
    youthPage.style.transform = "scale(0.95)";

});

youthTitle.addEventListener("click", () => {
    console.log("youth link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "youth.html";
        } else {
            window.location.href = "src/pages/youth.html";
        }
});

youthPage.addEventListener("mouseenter", () => {
    youthPage.style.cursor = "pointer";
    youthPage.style.transition = "filter 0.3s, transform 0.3s"; 
    youthPage.style.filter = "grayscale(100%)";
    youthPage.style.transform = "scale(0.95)";
});

youthPage.addEventListener("mouseleave", () => {
    youthPage.style.filter = "grayscale(0%)";
    youthPage.style.transform = "scale(1)";
    youthPage.style.transition = "filter 0.3s, transform 0.3s"; 
});

youthPage.addEventListener("click", () => {
        console.log("youth page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "youth.html";
        } else {
            window.location.href = "src/pages/youth.html";
        }
    });

//[deals js content]---------------------------------------------------]
dealsTitle.textContent = "DEALS";
    dealsTitle.style.position = "absolute";
    dealsTitle.style.top = "50%";
    dealsTitle.style.left = "50%";
    dealsTitle.style.transform = "translate(-50%, -50%)";
    dealsTitle.style.fontFamily = "sans-serif";
    dealsTitle.style.fontWeight = "bold";
    dealsTitle.style.fontSize = "10rem";  
    dealsTitle.style.color = "rgb(247, 246, 243)";
    dealsTitle.style.filter = "drop-shadow(0 0 1px rgb(255, 249, 227))";
    dealsTitle.style.zIndex = "10";

dealsSelect.appendChild(dealsTitle);

dealsTitle.addEventListener("mouseenter", () => {
    dealsPage.style.cursor = "pointer";
    dealsPage.style.transition = "filter 0.3s, transform 0.3s"; 
    dealsPage.style.filter = "grayscale(100%)";
    dealsPage.style.transform = "scale(0.95)";

});

dealsTitle.addEventListener("click", () => {
    console.log("deals link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "deals.html";
        } else {
            window.location.href = "src/pages/deals.html";
        }
});

dealsPage.addEventListener("mouseenter", () => {
    dealsPage.style.cursor = "pointer";
    dealsPage.style.transition = "filter 0.3s, transform 0.3s"; 
    dealsPage.style.filter = "grayscale(100%)";
    dealsPage.style.transform = "scale(0.95)";
});

dealsPage.addEventListener("mouseleave", () => {
    dealsPage.style.filter = "grayscale(0%)";
    dealsPage.style.transform = "scale(1)";
    dealsPage.style.transition = "filter 0.3s, transform 0.3s"; 
});

dealsPage.addEventListener("click", () => {
        console.log("deal page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "youth.html";
        } else {
            window.location.href = "src/pages/youth.html";
        }
    });

//[styles js content]---------------------------------------------------]
styleTitle.textContent = "STYLES";
    styleTitle.style.position = "absolute";
    styleTitle.style.top = "50%";
    styleTitle.style.left = "50%";
    styleTitle.style.transform = "translate(-50%, -50%)";
    styleTitle.style.fontFamily = "sans-serif";
    styleTitle.style.fontWeight = "bold";
    styleTitle.style.fontSize = "10rem";  
    styleTitle.style.color = "rgb(247, 246, 243)";
    styleTitle.style.filter = "drop-shadow(0 0 1px rgb(255, 249, 227))";
    styleTitle.style.zIndex = "10";

styleSelect.appendChild(styleTitle);

styleTitle.addEventListener("mouseenter", () => {
    stylePage.style.cursor = "pointer";
    stylePage.style.transition = "filter 0.3s, transform 0.3s"; 
    stylePage.style.filter = "grayscale(100%)";
    stylePage.style.transform = "scale(0.95)";

});

styleTitle.addEventListener("click", () => {
    console.log("style link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "deals.html";
        } else {
            window.location.href = "src/pages/deals.html";
        }
});

stylePage.addEventListener("mouseenter", () => {
    stylePage.style.cursor = "pointer";
    stylePage.style.transition = "filter 0.3s, transform 0.3s"; 
    stylePage.style.filter = "grayscale(100%)";
    stylePage.style.transform = "scale(0.95)";
});

stylePage.addEventListener("mouseleave", () => {
    stylePage.style.filter = "grayscale(0%)";
    stylePage.style.transform = "scale(1)";
    stylePage.style.transition = "filter 0.3s, transform 0.3s"; 
});

stylePage.addEventListener("click", () => {
        console.log("styles page link clicked");
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "collection.html";
        } else {
            window.location.href = "src/pages/collection.html";
        }
    });

 
//[styles js content]---------------------------------------------------]
endTitle.textContent = "THANKS FOR VISITING!";
    endTitle.style.position = "absolute";
    endTitle.style.top = "50%";
    endTitle.style.left = "50%";
    endTitle.style.transform = "translate(-50%, -50%)";
    endTitle.style.fontFamily = "sans-serif";
    endTitle.style.fontWeight = "bold";
    endTitle.style.fontSize = "8rem";  
    endTitle.style.color = "rgb(247, 246, 243)";
    endTitle.style.filter = "drop-shadow(0 0 1px rgb(255, 249, 227))";
    endTitle.style.zIndex = "10";

endSelect.appendChild(endTitle);




