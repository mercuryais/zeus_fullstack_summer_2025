console.log('JS Objects');

(function() {
    let firstName = 'Khangaikhuu';
    let lastName = 'Uvgunkhuu';
    let age = 43;
    let weight = 80.5;
})();

(function() {
    let firstName = 'Bold-Erdne';
    let lastName = 'Enkhtsetseg';
    let age = 24;
    let weight = 73.0;
})();

let khangaikhuu = {
    firstName: 'Khangakhuu',
    lastName: 'Uvgunkhuu',
    age: 43,
    weight: 80.5
};

console.log(khangaikhuu);

let boldErdene = {
    firstName: 'Erdne',
    lastName: 'Enkhtsetseg',
    age: 24,
    weight: 73.0
};

console.log(boldErdene);

let bugatti = {
    horsePower: 1000,
    brand: 'Bugatti',
    model: 'Veyron 16.4',
    producedYear: 2015
}
console.log(bugatti)
const porsche = {
    horsePower: 388,
    brand: 'Porsche',
    model: '911',
    producedYear: 1963
}
console.log(porsche)
let audi = {
    horsePower: 335,
    brand: 'Audi',
    model: 'Q8',
    producedYear: 2017
}
console.log(audi)

// object properties -> horsePower, brand, model, producedYear
// object values -> 113.8, Audi, A3, 2016

// object access properties
console.log(audi.horsePower);
console.log(audi.model);
console.log(audi.brand);
console.log(audi.brand);

// object access properties 
console.log(porsche['horsePower']);
console.log(porsche['model'])
console.log(porsche['brand'])
console.log(porsche['producedYear'])

const dotaTwoTroll = {
    'ultimate-ability': 'Berserker',
    'health-generation': '2hp per second',
    'stun': '1 second per 5 hit'
}

console.log(dotaTwoTroll["ultimate-ability"])

// Change value of the property using dot notation
audi.producedYear = 2018;
console.log(audi);

dotaTwoTroll['stun'] = '2 seconds per 5 punch';
console.log(dotaTwoTroll)

console.log(boldErdene);
boldErdene.skill = ['Python', 'Javascript', 'CSS', 'HTML', 'Database'];
console.log(boldErdene);

let movie = {
    title: 'Inception',
    director: 'Christopher Nolan',
    year: 2010
}
console.log(movie);

let person = {};
person.name = 'Batsuuri';
person.age = 20;
person.address = 'Earth'
console.log(person)

let computer = {
    brand: 'Asus',
    model: 'i7'
}
delete movie.year;
console.log(movie);

if (movie.genre == "undefined") {
    movie.genre = 'drama';
}
else {
    console.log('Baina')
}
console.log(movie.hello)

console.log(computer.brand);
console.log(computer['model']);

computer['brand'] = 'HP';
console.log(computer['brand']);

let fruits = {
    'apple': 3,
    'banana': 5,
    'orange': 2
}

for (let fruit in fruits) {
    console.log(`Fruit: ${fruit}, Quantity: ${fruits[fruit]}`)
}


const personInfo = {
name: "Bob",
age: 25,
email: "bob@example.com",
};
function logInfo(information) {
    for (let info in information) {
        console.log(`${info}: ${information[info]}`)
    }
}
logInfo(personInfo);

const studentGrades = {
    math: 90,
    science: 85,
    history: 88,
};
function calculateAverage(grades) {
    times = 0;
    score = 0;
    for(let grade in grades){
        score += grades[grade];
        times++;
    }
    return score / times;
}
const averageGrade = calculateAverage(studentGrades);
console.log("Average Grade: ", averageGrade);

const numbers = [1, 2, 3];
const doubled = numbers.map(num => num * 2);

console.log(doubled); // [2, 4, 6]
console.log(numbers); // [1, 2, 3] (original unchanged)


const nums = [1, 2, 3, 4];

const squares = nums.map(num => num * num);

console.log(squares); // [1, 4, 9, 16]



const factorial = n => n <= 1 ? 1 : n * factorial(n - 1);

console.log(factorial(5)); // 120
