// const supportedKeys = ['A', 'S', 'D', 'F', 'G', 'H', 'J'];
//
// function chkKey(arr, e) {
//     for (let i = 0; i < arr.length; i++) {
//         if (`Key${arr[i]}` === e.code) {
//             return console.log(`The '${arr[i]}' key is pressed.`);
//         }
//     }
//     return console.log('Pressed not supported key.');
// }
//
// window.addEventListener('keydown', function (e) {
//     chkKey(supportedKeys, e);
// })

// "use strict"
//
// document.addEventListener("keypress", handleKeyPress);
//
// function handleKeyPress(e) {
//     const keys = ['A', 'S', 'D', 'F', 'G', 'H', 'J'];
//     const keyPressed = e.key.toUpperCase();
//     if (keys.includes(keyPressed)) {
//         createSoundObject(keyPressed).play();
//     }
// }
//
// function createSoundObject(keyPressed) {
//     const audio = new Audio(`white_keys/${keyPressed}.mp3`);
//     return audio;
// }

if (typeof document !== "undefined") {
    document.addEventListener("keydown", (event) => {
        const keysArr = document.querySelectorAll("kbd");
        const contentArr = [];
        keysArr.forEach(e => contentArr.push(e.textContent));
        contentArr.includes(event.key.toUpperCase()) ?
            contentArr.forEach(e => {
                if(event.key.toUpperCase() === `${e}`) {
                    let aud = new Audio(`../audio/${e}.mp3`);
                    aud.play();
                }
            })
            : console.log(`Wrong '${event.key}' key is pressed.`);
    })
}
