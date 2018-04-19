// console.log(add(3, 3,2,3,4,5,67,8,9));
//
//
//
// function add() {
//     console.log(arguments);
//     let total = 0;
//     for (let i=0; i < arguments.length; i++) {
//         total += arguments[i];
//     }
//     return total;
// }

// function add(a, b=1) {
//     return a + b;
// }

//
// let addvariable = function (a, b) {
//     return a + b;
// };
// console.log(addvariable(3, 3));

// let number = add(20, 40);
// console.log(number + 1 + 1);
// if (isNaN(parseInt('100lkdfj20askjdg'))) {
//     console.log('Not a number')
// } else {
//     console.log('It\'s a number!')
//     console.log(parseInt('100lkdfj20askjdg'))
// }

function perform_operation(arr, f) {
  for (let i=0; i<arr.length; ++i) {
    arr[i] = f(arr[i]);
  }
}

let nums = [1, 2, 3];
let nums2 = [1, 2, 3];

perform_operation(nums, function(x) {
  return x*x;
});

function mult10(number) {
    return number * 10
}
perform_operation(nums2, mult10);
console.log(nums); // [1, 4, 9]
console.log(nums2); // [1, 4, 9]