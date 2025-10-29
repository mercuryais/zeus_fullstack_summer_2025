const hone = document.querySelector('h1') as HTMLElement;
if (hone) {
    hone.textContent = "Element is selected";
} else {
    console.log("Element is null");
}
const inputElement = document.querySelector('#name-input') as HTMLInputElement;