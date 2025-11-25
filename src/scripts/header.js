let header = document.getElementById("header");
let dropdown = document.createElement("div");
let toggleDropdown = false;

//[menu js content]---------------------------------------------------------------------------------------]
let menu = document.getElementById("fa-solid fa-bars");

    menu.addEventListener("mouseenter", () => {
        menu.style.cursor = "pointer";
        menu.style.color = "orange";
    });

    menu.addEventListener("mouseleave", () => {
        menu.style.color = "rgb(255, 249, 227)";
    });

    menu.addEventListener("click", () => {
        console.log("menu click works");

        if(toggleDropdown == false) {
            dropdown.className = "dropdown_content";
            dropdown.id = "dropdown_content";
            dropdown.style.position = "absolute";
            dropdown.textContent = "Dropdown Menu Content Located";
            dropdown.style.width = "150px";
            dropdown.style.height = "100vh";
            dropdown.style.left = "10px";
            dropdown.style.backgroundColor = "rgb(255, 249, 227)";
            toggleDropdown = true;
            header.appendChild(dropdown);
        }
        else {
            console.log("menu closed");
            toggleDropdown = false;
            header.removeChild(dropdown);
        }
    });


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
        console.log("hovered");
        cart.style.cursor = "pointer";
        cart.style.color = "orange";
    });

    cart.addEventListener("mouseleave", () => {
        cart.style.color = "rgb(255, 249, 227)";
    });

