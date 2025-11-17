function makeBetter(): Promise<void> {
    console.log("!. Mixing the better");

    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(".   -. Batter is ready!");
            resolve();
        }, 1500);
    });
}

function cookPancakes(): Promise<void> {
    console.log("2. Pouring batter on the griddle...");

    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const burned = Math.random() > 0.5;

            if (burned) {
                console.log(".   -> Oh no! You burned the pancake");
                reject("Pancake is burned");
            } else {
                console.log(".   -> Pancake is cooked");
                resolve();
            }
        }, 2000);
    })
}
function addSyrup(): Promise<void> {
    console.log("3. Adding mapple syrup....");
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(".      -> Pancake is ready to eat!");
            resolve();
        }, 500);
    })
}
console.log("Let's make a pancakes (with .catch");
makeBetter()
    .then(() => {
        return cookPancakes();
    })
    .then(() => {
        return addSyrup();
    })
    .then(() => {
        console.log("\n All done. Enjoy your breakfast!");
    })
    .catch((error) => {
        console.log("\n Breakfast failed!");
        console.log(error);
    })
console.log("This message kigs immediately");
async function makeBreakFast() {
    try {
        console.log("Let's make a pancakes (with async/await!")
        await makeBetter();

        await cookPancakes();

        await addSyrup();

        console.log("\n All done. Enjoy your breakfast!");
    } catch (error) {
        console.log("\n Breakfast failed!");
        console.log(error);
    }
}
makeBreakFast();