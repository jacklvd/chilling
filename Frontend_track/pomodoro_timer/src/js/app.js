// variables

let workTitle = document.getElementById('work');
let breakTitle = document.getElementById('break');

let workTime = 25;
let breakTime = 5;

let seconds = '00';

// display

window.onload = () => {
    document.getElementById('minutes').innerHTML = 0;
    document.getElementById('seconds').innerHTML = seconds;
    document.querySelector('#session').innerHTML = workTime;
    document.querySelector('#break-time').innerHTML = breakTime;

    workTitle.classList.add('active');
}

// start timer

function start() {
    // change button
    document.getElementById('start').style.display = 'none';
    document.getElementById('reset').style.display = 'block';

    // change the time
    seconds = 59;

    let workMinutes = workTime - 1;
    let breakMinutes = breakTime - 1;

    breakCount = 0;

    // countdown
    let timeFunction = () => {

        // change the display

        document.getElementById('minutes').innerHTML = workMinutes;
        document.getElementById('seconds').innerHTML = seconds;

        // start
        seconds = seconds - 1;

        if (seconds === 0) {
            workMinutes = workMinutes - 1;
            if (workMinutes === -1) {
                if (breakCount % 2 === 0) {
                    // start break
                    workMinutes = breakMinutes;
                    breakCount++;

                    // change the panel 
                    workTitle.classList.remove('active');
                    breakTitle.classList.add('active');

                } else {
                    // continue work
                    workMinutes = workTime;
                    breakCount++;

                    breakTitle.classList.remove('active');
                    workTitle.classList.add('active');
                }
            }
            seconds = 59;
        }
    }

    // start countdown
    setInterval(timeFunction, 1000); // 1000 = 1s
}

const plusSesstion = document.querySelector("#session-increment");
const minusSesstion = document.querySelector("#session-decrement");
const session = document.querySelector("#session");

const plusBreak = document.querySelector("#break-increment");
const minusBreak = document.querySelector("#break-decrement");
const breakLength = document.querySelector("#break-time");

plusSesstion.addEventListener("click", () => {
    workTime++;
    workTime = (workTime < 10) ? "0" + workTime : workTime;
    session.innerHTML = workTime;
});

minusSesstion.addEventListener("click", () => {
    if (workTime > 1) {
        workTime--;
        workTime = (workTime < 10) ? "0" + workTime : workTime;
        session.innerHTML = workTime;
    }
});

plusBreak.addEventListener("click", () => {
    breakTime++;
    breakTime = (workTime < 10) ? "0" + breakTime : breakTime;
    breakLength.innerHTML = breakTime;
});

minusBreak.addEventListener("click", () => {
    if (breakTime > 1) {
        breakTime--;
        breakTime = (breakTime < 10) ? "0" + breakTime : breakTime;
        breakLength.innerHTML = breakTime;
    }
});

// stop.addEventListener('click', function() {
// 	clearInterval();
// });