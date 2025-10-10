console.log("Coffee Shop");

console.log("------------------------");
console.log("Hello, Dorj");
console.log("See you soon.");
console.log("------------------------");

console.log("------------------------");
console.log("Hello, Sarah");
console.log("See you soon.");
console.log("------------------------");

console.log("------------------------");
console.log("Hello, Tuga");
console.log("See you soon.");
console.log("------------------------");

// Solution
function greetings(name) {
  console.log("------------------------");
  console.log(`Hello ${name}`);
  console.log("See you soon.");
  console.log("------------------------");
}
greetings("Dorj");
greetings("Sarah");
greetings("Tuga");

function quadratEquation(x, y) {
  return x * x + 2 * x * y + y * y;
}

let result = quadratEquation(4, 5);
console.log(result);
