function greetPerson(name, timeOfDay, callback) {
    var greetings = callback(name, timeOfDay);
    console.log(greetings);
}
function createGreeting(name, timeOfDay) {
    if (timeOfDay === "morning") {
        return "\u04E8\u0433\u043B\u04E9\u04E9\u043D\u0438\u0439 \u043C\u044D\u043D\u0434, ".concat(name);
    }
    else if (timeOfDay === "afternoon") {
        return "\u04E8\u0434\u0440\u0438\u0439\u043D \u043C\u044D\u043D\u0434, ".concat(name);
    }
    else if (timeOfDay === "evening") {
        return "\u041E\u0440\u043E\u0439\u043D \u043C\u044D\u043D\u0434, ".concat(name);
    }
    else {
        return ("Hello ".concat(name));
    }
}
greetPerson("Батбаяр", "morning", createGreeting);
greetPerson("Сарнай", "afternoon", createGreeting);
greetPerson("Дорж", "evening", createGreeting);
function greetUser(name, greetingType, callback) {
    var massage = "";
    if (greetingType === "formal") {
        massage = "\u0421\u0430\u0439\u043D \u0431\u0430\u0439\u043D\u0430 \u0443\u0443, ".concat(name);
    }
    else if (greetingType === "casual") {
        massage = "\u042E\u0443 \u0431\u0430\u0439\u043D\u0430, ".concat(name);
    }
    else if (greetingType === "friendly") {
        massage = "\u0425\u044D\u043B\u043B\u043E ".concat(name);
    }
    callback(massage);
}
greetUser("Сарнай", "formal", function (message) {
    console.log(message);
});
