interface CardProps {
    children: React.ReactNode;
}

function Card({children} : CardProps) {
    return(
        <div 
        style={{
            border: "2px solid #ddd",
            borderRadius: "8px",
            padding: "20px", 
            margin: "10px",
        }}
    >
        {children}
        </div>
    )
}

export default Card;