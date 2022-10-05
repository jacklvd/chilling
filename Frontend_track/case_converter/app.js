function formatTextArea(buttonId) {
    let text = document.getElementById('text-box');
    let words = text.value.toLocaleLowerCase().split(' ');
    let capitalize = function(string) {
        return string.charAt(0).toUpperCase() + string.substring(1);
    };

    let save = function download(filename, text) {
        let element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', filename);

        element.style.display = 'none';
        document.body.appendChild(element);

        element.click();

        document.body.removeChild(element);
    };

    let wordData;

    if (buttonId === 'upper-case') {
        text.value = text.value.toUpperCase();
    } else if (buttonId === 'lower-case') {
        text.value = text.value.toLowerCase();
    } else if (buttonId === 'proper-case') {
        wordData = words.map((value) => {
            return capitalize(value)
        });
        text.value = wordData.join(' ');
    } else if (buttonId === 'sentence-case') {
        wordData = words.map((value, index) => {
            if (index === 0) {
                return capitalize(value);
            }
            let lastWord = words[index - 1];
            if (lastWord.charAt(lastWord.length - 1) === '.') {
                return capitalize(value);
            }
            return value;
        });
        text.value = wordData.join(' ');
        console.log('Error');
    } else if (buttonId === 'save-text-file') {
        save('text.txt', text.value);
    } else {
        console.log('Error');
    }
}

document.getElementById('upper-case').addEventListener('click', function() {
    formatTextArea('upper-case');
})

document.getElementById('lower-case').addEventListener('click', function() {
    formatTextArea('lower-case');
})

document.getElementById('proper-case').addEventListener('click', function() {
    formatTextArea('proper-case');
})

document.getElementById('sentence-case').addEventListener('click', function() {
    formatTextArea('sentence-case');
})

document.getElementById('save-text-file').addEventListener('click', function() {
    formatTextArea('save-text-file');
})