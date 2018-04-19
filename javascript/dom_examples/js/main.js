// document.querySelector('#mainTitle').addEventListener('mouseover', function (e) {
//     document.querySelector('#mainTitle').style.backgroundColor = '#F84567'
// });
//
// document.querySelector('#mainTitle').addEventListener('mouseout', function (e) {
//     document.querySelector('#mainTitle').style.backgroundColor = null
// });
// let color;
//
// function getColor(e) {
//     color = document.querySelector('#colorPicker').value;
// }
//
// document.querySelector('#submit').addEventListener('click', function (event) {
//     getColor();
//     document.body.style.backgroundColor = color
// });

document.querySelector('#submit').addEventListener('click', function (event) {
    let color = document.querySelector('#colorPicker').value;
    if (color) {
        document.body.style.backgroundColor = document.querySelector('#colorPicker').value;
    }
});