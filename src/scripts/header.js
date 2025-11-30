let header = document.getElementById("header");
let menuDrop = document.createElement("div");
let cartDrop = document.createElement("div");
let toggleDropdown = false;
let toggleCart = false;


//[menu js content]---------------------------------------------------------------------------------------]
let menu = document.getElementById("menu_bar");


    menu.addEventListener("mouseenter", () => {
        menu.style.cursor = "pointer";
        menu.style.color = "rgb(194,41,12)";
    });


    menu.addEventListener("mouseleave", () => {
        menu.style.color = "rgb(255, 249, 227)";
    });


    menu.addEventListener("click", () => {
        console.log("menu click works");
        dropdownMenu();
    });


//[dropdown menu js content]---------------------------------------------------------------------------------------
function dropdownMenu() {
         if(toggleDropdown == false) {
           
            menuDrop.style.position = "absolute";
            menuDrop.style.width = "100vw";
            menuDrop.style.height = "100vh";
            menuDrop.style.backgroundColor = "rgba(86, 84, 72, 0.5)";
            toggleDropdown = true;
            header.appendChild(menuDrop);
            //
            let menuList = document.createElement("div");
            menuList.style.height = " 100vh";
            menuList.style.width = "25vw";
            menuList.style.margin = "0";
            menuList.style.backgroundColor = "rgb(28,28,28)";
            menuList.style.paddingTop = "30px";
            menuList.style.paddingLeft = "55px";
            menuList.style.paddingRight = "55px";
            menuDrop.appendChild(menuList);
            //
            let menuItems = ["HOME","", "MEN","","WOMEN","","YOUTH","","DEALS","","STYLES","","CHECKOUT","","ABOUT","","HELP"];


            for(let i = 0; i < menuItems.length; i++) {
                let listItem = document.createElement("div");
                listItem.textContent = menuItems[i];
                if (menuItems[i] != "") {
                    listItem.style.color = "rgb(28,28,28)";
                    listItem.style.fontSize = "1.25vw";
                    listItem.style.fontWeight = "bold";
                    listItem.style.backgroundColor = "rgb(255, 249, 227)";
                    listItem.style.boxShadow = "0px 5px rgba(255, 249, 227, 0.75)";
                    listItem.style.padding = "10px";
                    listItem.style.cursor = "pointer";


                    listItem.addEventListener("mouseenter", () => {
                        listItem.style.backgroundColor = "rgb(194,41,12)";
                         listItem.style.boxShadow = "0px 5px rgba(194,41,12, 0.75)";
                    });
                    listItem.addEventListener("mouseleave", () => {
                        listItem.style.backgroundColor = "rgb(255, 249, 227)";
                        listItem.style.boxShadow = "0px 5px rgba(255, 249, 227, 0.75)";
                    });


                    listItem.addEventListener("click", () => {
                        listItem.style.boxShadow = "0px 0px rgba(194,41,12, 0.75)";
                        if(menuItems[i] == "HOME") {
                            if(window.location.href.endsWith("index.html")) {
                                window.location.href = "index.html";
                            } else {
                                window.location.href = "../../index.html";
                            }  
                        }else if(menuItems[i] == "MEN") {
                           if(window.location.href.indexOf("src/pages") > -1) {
                                window.location.href = "men.html";
                            } else {
                                window.location.href = "src/pages/men.html";
                            }
                        }else if(menuItems[i] == "WOMEN") {
                            if(window.location.href.indexOf("src/pages") > -1) {
                                window.location.href = "women.html";
                            }else {
                                 window.location.href = "src/pages/women.html";
                            }
                        }else if(menuItems[i] == "YOUTH") {
                            if(window.location.href.indexOf("src/pages") > -1) {
                                window.location.href = "youth.html";
                            }else {
                                window.location.href = "src/pages/youth.html";
                            }
                        }else if(menuItems[i] == "DEALS") {
                            if(window.location.href.indexOf("src/pages") > -1) {
                                window.location.href = "deals.html";
                            }else {
                                window.location.href = "src/pages/deals.html";
                            }
                        }else if(menuItems[i] == "STYLES") {
                            if(window.location.href.indexOf("src/pages") > -1) {
                                window.location.href = "collection.html";
                            }else{
                                window.location.href = "src/pages/collection.html";
                            }
                        }else if(menuItems[i] == "CHECKOUT") {
                            if(window.location.href.indexOf("src/pages") > -1) {
                                window.location.href = "checkout.html";
                            }else{
                                window.location.href = "src/pages/checkout.html";
                            }
                        }else if(menuItems[i] == "ABOUT") {
                            if(window.location.href.indexOf("src/pages") > -1) {
                                window.location.href = "about.html";
                            }else{
                                window.location.href = "src/pages/about.html";
                            }
                        }else if(menuItems[i] == "HELP") {
                            if(window.location.href.indexOf("src/pages") > -1) {
                                window.location.href = "help.html";
                            }else{
                                window.location.href = "src/pages/help.html";
                            }
                        }


                    });
                    menuList.appendChild(listItem);
                }
                else {
                    let spacer = document.createElement("div");
                    spacer.style.height = "22.5px";
                    menuList.appendChild(spacer);
                }
            }

        }
        else {
            console.log("menu closed");
            toggleDropdown = false;
            header.removeChild(menuDrop);
        }
}


//[title js content]---------------------------------------------------------------------------------------]


let title = document.querySelector("h1");


    title.addEventListener("mouseenter", () => {
        title.style.cursor = "pointer";
        title.style.color = "rgb(194,41,12)";
    });


    title.addEventListener("mouseleave", () => {
        title.style.cursor = "default";
        title.style.color = "rgb(255, 249, 227)";


    });


    title.addEventListener("click", () => {
        if(window.location.href.endsWith("index.html")) {
            window.location.href = "index.html";
        } else {
            window.location.href = "../../index.html";
        }  
    });


//[help button js content]---------------------------------------------------------------------------------------]

let help = document.getElementById("help_button");


    help.addEventListener("mouseenter", () => {
        help.style.cursor = "pointer";
        help.style.color = "rgb(194,41,12)";
    });


    help.addEventListener("mouseleave", () => {
        help.style.color = "rgb(255, 249, 227)";
    });


    help.addEventListener("click", () => {
        if(window.location.href.indexOf("src/pages") > -1) {
            window.location.href = "help.html";
        }else{
            window.location.href = "src/pages/help.html";
        }
    });


//[cart button js content]---------------------------------------------------------------------------------------]

let cart = document.getElementById("shop_cart");


    cart.addEventListener("mouseenter", () => {
        console.log("hovered");
        cart.style.cursor = "pointer";
        cart.style.color = "rgb(194,41,12)";
    });


    cart.addEventListener("mouseleave", () => {
        cart.style.color = "rgb(255, 249, 227)";
    });


    cart.addEventListener("click", () => {
        dropCart();
    });


function dropCart(){


    if(toggleCart == false) {
        console.log("cart opened");


        cartDrop.style.position = "absolute";
        cartDrop.style.right = "0vw";
        cartDrop.style.width = "20vw";
        cartDrop.style.height = "40vh";
        cartDrop.style.padding = "20px";
        cartDrop.style.backgroundColor = "rgb(28,28,28)";
        cartDrop.style.margin = "0";
        cartDrop.style.justifyContent = "center";
        toggleCart = true;
        header.appendChild(cartDrop);


        let cartPage = document.createElement("div");
        cartPage.style.position = "absolute";
        cartPage.style.width = "20vw";
        cartPage.style.height = "40vh";
        cartPage.style.backgroundColor = "rgb(255, 249, 227)";
        cartDrop.appendChild(cartPage);


        //CART CONTENT HERE -
        
        // helper that fetches and renders the cart contents
        function refreshCart() {
            fetch("/cart_contents").then(r => r.text()).then(html => {
                cartPage.innerHTML = html;

                // attach remove handlers 
                cartPage.querySelectorAll(".cart-remove").forEach(btn => {
                    // use onclick to overwrite any existing listener
                    btn.onclick = function (e) {
                        const id = this.dataset.id;
                        fetch("/remove_from_cart/" + id, { method: "POST" })
                            .then(() => {
                                // re-render after removal
                                refreshCart();
                            });
                    };
                });

                // attach checkout button
                const checkout = cartPage.querySelector("#checkout_btn");
                if (checkout) {
                    checkout.onclick = () => {
                        if (window.location.href.indexOf("src/pages") > -1) {
                            window.location.href = "checkout.html";
                        } else {
                            window.location.href = "src/pages/checkout.html";
                        }
                    };
                }
            });
        }

        // make refreshCart callable from other scripts
        window.refreshCart = refreshCart;

        // initial render
        refreshCart();


    }
    else {
        console.log("cart closed");
        toggleCart = false;
        header.removeChild(cartDrop);
    }  


}

// search bar functionality
(function () {
    const searchInput = document.querySelector(".search_input");

    // the magnifying glass inside the search bar
    const searchIcon = document.querySelector(".search_bar .fa-magnifying-glass") || document.querySelector(".search_bar i.fa-magnifying-glass");

    function goSearch() {
        if (!searchInput) return;
        const q = (searchInput.value || "").trim();
        // Flask renders the results
        window.location.href = "/search?q=" + encodeURIComponent(q);
    }

    if (searchInput) {
        searchInput.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault();
                goSearch();
            }
        });
    }

    if (searchIcon) {
        searchIcon.style.cursor = "pointer";
        searchIcon.addEventListener("click", (e) => {
            e.preventDefault();
            goSearch();
        });
    }
})();


