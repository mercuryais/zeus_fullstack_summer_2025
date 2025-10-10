console.log('Remove code duplication');

let length1 = 10;
let width1 = 5;
let area1 = length1 * width1;
let perimeter1 = 2 * (length1 + width1);

console.log('========Rectangle 1 Result==========');
console.log(`Area: ${area1}`);
console.log(`Permieter: ${perimeter1}`);
console.log("");

let length2 = 20;
let width2 = 8;
let area2 = length2 * width2;
let perimeter2 = 2 * (length2 + width2);

console.log('========Rectangle 1 Result==========');
console.log(`Area: ${area2}`);
console.log(`Permieter: ${perimeter2}`);
console.log("");

let calculateAndPrintReactangle = function(length, width) {
    let area = length * width;
    let perimeter = 2 * (length + width);
    console.log(`========Rectangle Result==========`);
    console.log(`Area: ${area}`);
    console.log(`Permieter: ${perimeter}`);
    console.log("");
}
calculateAndPrintReactangle(10, 5);
calculateAndPrintReactangle(20, 8);