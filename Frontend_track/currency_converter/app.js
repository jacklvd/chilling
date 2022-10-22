//Write your code here
const currencies = {
    USD: 1.0,
    JPY: 113.5,
    EUR: 0.89,
    RUB: 74.36,
    GBP: 0.75
};

const input = require('sync-input');

function intro() {
    console.log("Welcome to Currency Converter!");
    for (const currency in currencies) {
        console.log(`1 USD equals ${currencies[currency]} ${currency}`);
    }
}


function convert() {
    console.log(`What do you want to convert?`);
    let from = input("From: ").toUpperCase();
    if (currencies[from] === undefined) {
        console.log("Unknown currency");
        return;
    }
    let to = input("To: ").toUpperCase();
    if (currencies[to] === undefined) {
        console.log("Unknown currency");
    } else {
        const amount = Number(input("Amount: "));
        if (isNaN(amount)) {
            console.log("The amount has to be a number");
        } else if (amount < 1) {
            console.log("The amount cannot be less than 1");
        } else {
            const converted = (amount / currencies[from] * currencies[to]).toFixed(4);
            console.log(`Result: ${amount} ${from} equals ${converted} ${to}`);
        }
    }
}


function command() {
    let run = true;
    let user = 0;
    while (run) {
        while (true) {
            console.log(`What do you want to do?`);
            console.log(`1-Convert currencies 2-Exit program`);
            user = parseInt(input());
            if (user === 1 || user === 2) {
                break;
            }
            console.log(`Unknown input`);
        }
        if (user === 1) {
            convert();
        }
        else if (user === 2) {
            console.log(`Have a nice day!`);
            run = false;
        }
    }
}


function main() {
    intro();
    command();
}

main();