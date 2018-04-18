// Breakfast: 7AM - 9AM
// Lunch: 12PM - 2PM
// Dinner: 7PM - 9PM
// Hammer: 10PM - 4AM

// time = input('What time is it (HH:AM/PM)?: ')
let time = prompt('What time is it (HH:AM/PM)?');
// console.log(time);


// time_split = time.split(':')
let time_split = time.split(':');
// console.log(time_split);


// hour = int(time_split[0])
let hour = parseInt(time_split[0]);
// console.log(hour);


// meridian = time_split[1].lower()
let meridian = time_split[1].toLowerCase();
// console.log(meridian);


//
//
// if hour in range(7, 10):
//     if meridian == 'am':
//         print("It's Breakfast!")
//     else:
//         print("It's Dinner!")
// elif hour in [12, 1, 2] and meridian == 'pm':
//     print("It's Lunch!")
// elif hour in range(10, 12) and meridian == 'pm' or (hour == 12 or hour in range(1, 5)) and meridian == 'am':
//     print("It's Hammer TIME!")


if ([7, 8, 9].indexOf(hour) > -1) {
    if (meridian === 'am') {
        console.log("It's Breakfast!")
    } else {
        console.log("It's Dinner!")
    }
} else if ([12, 1, 2].indexOf(hour) > -1 && meridian === 'pm') {
    console.log("It's Lunch!")
} else if (hour >= 10 && hour < 12 && meridian === 'pm' || (hour === 12 || [1, 2, 3, 4].indexOf(hour) > -1) && meridian === 'am') {
    console.log("It's Hammer TIME!")
}
