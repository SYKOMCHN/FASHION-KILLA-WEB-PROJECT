//[menu js content]---------------------------------------------------------------------------------------]
let menu = document.getElementById("fa-solid fa-bars");

    menu.addEventListener("mouseenter", () => {
        menu.style.cursor = "pointer";
        menu.style.color = "orange";
    });

    menu.addEventListener("mouseleave", () => {
        menu.style.color = "rgb(255, 249, 227)";
    });

   // menu.addEventListener("click", () => {
    //    let dropdown = document.createElementID("dropdown-content");
        
    //});

//[title js content]---------------------------------------------------------------------------------------]
let title = document.querySelector("h1");

    title.addEventListener("mouseenter", () => {
        title.style.cursor = "pointer";
    });

    title.addEventListener("mouseleave", () => {
        title.style.cursor = "default";
    });

    title.addEventListener("click", () => {
        window.location.href = "index.html";
    });

//[help button js content]---------------------------------------------------------------------------------------]

let help = document.getElementById("fa-regular fa-circle-question");

    help.addEventListener("mouseenter", () => {
        help.style.cursor = "pointer";
        help.style.color = "orange";
    });

    help.addEventListener("mouseleave", () => {
        help.style.color = "rgb(255, 249, 227)";
    });

    help.addEventListener("click", () => {
        window.location.href = "src/pages/help.html";
    });

//[cart button js content]---------------------------------------------------------------------------------------]

let cart = document.getElementById("fa-solid fa-cart-shopping");

    cart.addEventListener("mouseenter", () => {
        cart.style.cursor = "pointer";
        cart.style.color = "orange";
    });

    cart.addEventListener("mouseleave", () => {
        cart.style.color = "rgb(255, 249, 227)";
    });

