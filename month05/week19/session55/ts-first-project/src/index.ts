interface Greeting {
  message: string;
  name: string;
}

function greet(greeting: Greeting): void {
  console.log(`${greeting.message}, ${greeting.name}!`);
}

const myGreeting: Greeting = {
  message: "Сайн байна уу",
  name: "TypeScript"
};

greet(myGreeting);