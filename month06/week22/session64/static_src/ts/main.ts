console.log("TypeScript-ээс мэндчилье! 🚀 ");

function funcA(){
  setTimeout(() => {
    console.log('A');
  }, 3000);
}
function funcB(){
  setTimeout(() => {
    console.log('B');
  }, 2000);
}
function funcC(){
  setTimeout(() => {
    console.log('C');
  }, 1000);
}
/// Callback control functions
type simpleCallBack = () => void;
/// Step 1: Simulates mixing better (takes 1.5 seconds)
function makeBetter (callback: simpleCallBack) {
  console.log("1.Mixing the better...");
  setTimeout(()=> {
    console.log("    -> Better is ready");
    callback();
  }, 1500);
}
/// Step 2: Simulates cooking the pancake (takes 2 seconds)
function cookPancake (callback: simpleCallBack) {
  console.log("2. Pouring better on the griddle...");
  setTimeout(() => {
    console.log("    -> Pancake is cooked!");
    callback();
  }, 2000);
}
/// Step 3: Simulates adding syrup (takes 0.5 sseconds)
function addSyrup (callback: simpleCallBack) {
  console.log("3. Adding maple syrup...");
  setTimeout(() => {
    console.log("   -> Pancake is ready to eat!");
    callback();
  }, 500);
}

// Promise
let myPromise = new Promise<void>((resolve, reject) => {
  const isApproved = true;
  if(isApproved) {
    console.log("Ok")
    resolve();
  } else {
    console.log("Fail")
    reject();
  }
})
console.log(myPromise);
function main() {
  // funcA();
  // funcB();
  // funcC();

  /// Make pancake
  console.log("Let's make pancakes!");
  /// Start step 1
  makeBetter(() => {
    /// Step 2
    cookPancake(() => {
      /// Step 3
      addSyrup(() => {
        console.log("\n All done. Enjoy your breakfast!");
      }); // End of add Syrup
    }); // End of cooking pancake
  }); // End of make Better
  // Promise
  console.log(myPromise);
  myPromise
    .then(() => {
      console.log("Next");
    })
    .catch(() => {
      console.log("Failed Promise");
    })
}
document.addEventListener("DOMContentLoaded", main);
