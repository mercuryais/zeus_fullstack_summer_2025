interface ProductCardProps {
    title: string;
    price: number;
    description: string;
    imageUrl: string;
    inStock: boolean;
}

function ProductCard ({title, price, description, imageUrl, inStock}: ProductCardProps) {
    return (
        <div 
        style={{
            border: '1px solid #ccc',
            borderRadius: '12px',
            padding: '16px',
            maxWidth: '300px',
            margin: '10px'
        }}
    >
        <img 
            src={imageUrl}
            alt={title}
            style={{width: '100%', borderRadius: '8px'}}
            />
        <h3>{title}</h3>
        <p style={{color: "#666"}}>{description}</p>
        <p style={{fontSize: "24px", fontWeight: "bold", color: "#007bff"}}>
            {price}
        </p>
        <p style={{color: inStock ? "green": "red"}}>
            {inStock? "In stock": "Out of stock"}
        </p>
    </div>
    )
}

export default ProductCard;