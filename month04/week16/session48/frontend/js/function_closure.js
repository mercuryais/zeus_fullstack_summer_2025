console.log('Function Closure');

let a = 6;
let b = 7;

console.log(a);
console.log(b);

(function(){
    let a = 10;
    let b = 20;
})();
console.log(a);