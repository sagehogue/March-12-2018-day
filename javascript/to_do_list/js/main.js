document.querySelector('#submit').addEventListener('click', function (e) {
    doTheThing(document.querySelector('#toDoInput').value);
});

document.querySelector('#toDoInput').addEventListener('keyup', function (e) {
    if (e.keyCode === 13) {
        // console.log(this.value)
        doTheThing(this.value)
    }
});

function generateListItem(item) {
    return `<tr><td>${item}</td><td><button class="delete">Delete</button></td></tr>`
}

function attachListItem(html) {
    document.querySelector('#toDoList').innerHTML += html;
}

function doTheThing(item) {
    attachListItem(generateListItem(item));
    document.querySelector('#toDoInput').value = '';
}

document.querySelector("body").addEventListener('click', function (e) {
    if (e.target.className === 'delete') {
        e.target.parentElement.parentElement.remove();
    }
});