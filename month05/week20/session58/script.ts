const outputDiv = document.querySelector<HTMLDivElement>("#output")
const myButton = document.querySelector<HTMLButtonElement>("#my-button")

if (myButton && outputDiv) {
    myButton.addEventListener('click', (event: MouseEvent) => {
        console.log('Button clicked', event)
        outputDiv.textContent = "Button clicked";
    })
} else {
    console.log("Error during button click.")
}
const myInput = document.querySelector<HTMLInputElement>("#my-input")
if (myInput && outputDiv) {
    myInput.addEventListener('input', (event: Event) => {
        const target = event.target as HTMLInputElement;

        outputDiv.textContent = `You wrote : ${target.value}`
    })
}

const myForm = document.querySelector<HTMLFormElement>("#my-form");
if (myForm && myInput && outputDiv) {
    myForm.addEventListener('submit', (event: SubmitEvent) => {
        event.preventDefault();
        console.log('Form sent');
        outputDiv.textContent = `Form sent: ${myInput.value}`;
        myInput.value = '';
    })
}