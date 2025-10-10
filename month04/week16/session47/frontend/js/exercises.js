console.group('EX 01');

for (let i = 1; i < 21; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        console.log('Three Five');
    } else if (i % 3 == 0) {
        console.log('Three');
    } else if (i % 5 == 0) {
        console.log('Five');
    } else {
        console.log(i)
    }
}

function printPattern(a) {
    for (let i = 1; i < a+1; i++) {
        console.log("* ".repeat(i))
    }
}
printPattern(5)

console.log(isEven(4));
function isEven(a) {
    if (a % 2 == 0){
        return true
    } else {
        return false
    }
}

console.log(sumDigits(833));
function sumDigits(a) {
    let sum = 0;
    for (let digit of String(a)) {
        sum += parseInt(digit)
    }
    return sum
}

console.log(isPrime(2))
function isPrime(a) {
    if (a == 0 || a == 1) {
        return false
    }
    for (let i = 0; i < a; i++){
        if (i > 1) {
            if (a % i == 0) {
                return false
            }
        }
    }
    return true
}

console.log(factorial(5));
function factorial(a) {
    result = 1;
    for (let i = 1; i < a + 1; i++){
        result *= i;
    }
    return result
}

function fibonacci(n) {
    let num1 = 0;
    let num2 = 1;

    for (let i = 0; i < n; i++) {
        console.log(num1);
        let next = num1 + num2;
        num1 = num2;
        num2 = next;
    }
}
fibonacci(5);
