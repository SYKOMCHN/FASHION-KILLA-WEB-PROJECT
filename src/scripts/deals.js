let timer1 = document.getElementById("timer1");
let timer2 = document.getElementById("timer2");

let randomInt1 = Math.floor(Math.random() * 36000) + 1;
let randomInt2 = Math.floor(Math.random() * 36000) + 1;

let interval = setInterval(() => {
    // Countdown for timer 1
    if (randomInt1 > 0) {
        let hours1 = Math.floor(randomInt1 / 3600);
        let minutes1 = Math.floor((randomInt1 % 3600) / 60);
        let seconds1 = randomInt1 % 60;

        timer1.textContent = "DEAL EXPIRES IN: " + hours1 + ':' + minutes1 + ':' + seconds1;
        --randomInt1;
    }
    else {
        timer1.textContent = "DEAL EXPIRED";
    }

    // Countdown for timer 2
    if (randomInt2 > 0) {
        let hours2 = Math.floor(randomInt2 / 3600);
        let minutes2 = Math.floor((randomInt2 % 3600) / 60);
        let seconds2 = randomInt2 % 60;

        timer2.textContent = "DEAL EXPIRES IN: " + hours2 + ':' + minutes2 + ':' + seconds2;
        --randomInt2;
    }
    else {
        timer2.textContent = "DEAL EXPIRED";
    }

    // Exit loop if both timers are done
    if (randomInt1 <= 0 && randomInt2 <= 0) {
        clearInterval(interval);
    }
}, 1000);