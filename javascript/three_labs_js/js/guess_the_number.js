// user_guess_count = 0
let user_guess_count = 0;


// computer_guess = random.randrange(1, 11)
let computer_guess = Math.floor(Math.random() * 10) + 1;
console.log(computer_guess);
//

let playing = true;
let user_guess;
while (user_guess_count < 7) {
    user_guess = prompt('What is your guess?');
    user_guess_count ++;

    if (user_guess > computer_guess) {
        console.log('You guessed too high!')
    } else if (user_guess < computer_guess) {
        console.log('You guessed too low!')
    } else {
        console.log(`YOU GUESSED IT!! YAY!!! you guessed it in ${user_guess_count}`)
        break
    }
}
// while True:
//     user_guess = int(input('What number do you guess?: '))
//     user_guess_count = user_guess_count + 1
//     if user_guess > computer_guess:
//         print('You guessed too high!')
//     elif user_guess < computer_guess:
//         print('You guessed too low!')
//     else:
//         print('YOU GUESSED IT!! YAY!!! you guessed it in {}'.format(user_guess_count))
//         break