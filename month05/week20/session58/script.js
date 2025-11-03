var outputDiv = document.querySelector("#output");
var myButton = document.querySelector("#my-button");
if (myButton && outputDiv) {
    myButton.addEventListener('click', function (event) {
        console.log('Button clicked', event);
        outputDiv.textContent = "Button clicked";
    });
}
else {
    console.log("Error during button click.");
}
var myInput = document.querySelector("#my-input");
if (myInput && outputDiv) {
    myInput.addEventListener('input', function (event) {
        var target = event.target;
        outputDiv.textContent = "You wrote : ".concat(target.value);
    });
}
var myForm = document.querySelector("#my-form");
if (myForm && myInput && outputDiv) {
    myForm.addEventListener('submit', function (event) {
        event.preventDefault();
        console.log('Form sent');
        outputDiv.textContent = "Form sent: ".concat(myInput.value);
        myInput.value = '';
    });
}
