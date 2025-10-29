let ner: string = "Batsuuri";
let nas: number = 20;
let isOyutan: boolean = false;

let count: number = 10;
function add(numone: number, numtwo: number): number {
    return numone + numtwo
}   
function logMessage(message: string): void {
    console.log(message)
}
let hobbies: string[] = ["Game", "Music", "Movie"];
interface Person {
    name: string,
    age: number, 
    email?: string
}
const user: Person = {
    name: "Batsuuri",
    age: 20,
    email: "ahahahah@gmai.com"
}
function greetUser(who: Person): void {
    console.log(`Сайн уу ${who.name} та ${who.age} настай.`);
}
const greetUserOne = (whoone: Person) : void => console.log(`Сайн уу ${whoone.name} та ${whoone.age} настай.`);

let id: string | number = 10;
id = "Hi";

type UserID = string | number;
function findUserById(id: UserID): string {

  if (typeof id === 'number') {   
    return `Хэрэглэгчийг ID: ${id} (Тоо) ашиглан хайж байна...`;
  } else if (typeof id === 'string') {
    return `Хэрэглэгчийг ID: "${id}" (Текст) ашиглан хайж байна...`;
  } else {
    return "Хэрэглэгчийн ID-ийн төрөл тодорхойгүй байна.";
  }
}