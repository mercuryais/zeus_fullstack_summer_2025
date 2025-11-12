type TimeOfDay = "morning" | "afternoon" | "evening";
type GreetingCallback = (name: string, timeOfDay: TimeOfDay) => string;
function greetPerson(
name: string,
timeOfDay: TimeOfDay,
callback: GreetingCallback
): void {
    const greetings = callback(name, timeOfDay)
    console.log (greetings)
}
function createGreeting(name: string, timeOfDay: TimeOfDay): string {
    if (timeOfDay === "morning") {
        return `Өглөөний мэнд, ${name}`
    } else if (timeOfDay === "afternoon") {
        return `Өдрийн мэнд, ${name}`
    } else if (timeOfDay === "evening") {
        return `Оройн мэнд, ${name}`
    } else {
        return (`Hello ${name}`)
    }

}


greetPerson("Батбаяр", "morning", createGreeting);
greetPerson("Сарнай", "afternoon", createGreeting);
greetPerson("Дорж", "evening", createGreeting);


type GreetingType = "formal" | "casual" | "friendly";
function greetUser(name: string, greetingType: GreetingType, callback: (message: string) => void
): void {
    var massage: string = "";
    if(greetingType === "formal") {
        massage = `Сайн байна уу, ${name}`
    } else if (greetingType ==="casual") {
        massage = `Юу байна, ${name}`
    } else if (greetingType === "friendly") {
        massage = `Хэлло ${name}`
    }
    callback(massage)
}
greetUser("Сарнай", "formal", (message: string): void => {
console.log(message);
});