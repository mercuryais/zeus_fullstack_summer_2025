interface ButtonProps {
    text: string;
    color?: string; // optional
}
function Button({ text, color = "blue"}: ButtonProps) {
    //  Object destructure
    // const ( text, color ) = props;
    return (
        <button 
        style={{
            backgroundColor: color,
            color: "white",
            padding: "10px 20px",
        }}
    >
           {text} 
        </button>
    )
}

export default Button;