import type { Product } from "../types";

interface ProductCardProps {
  product: Product;
}
const ProductCard = ({ product }: ProductCardProps) => {
  // Үнийг форматлах
  const formatPrice = (price: string) => {
    return new Intl.NumberFormat("mn-MN", {
      style: "currency",
      currency: "MNT",
      minimumFractionDigits: 0,
    }).format(Number(price));
  };
  return (
    <div className="product-card">
      <div className="product-image">
        {product.image ? (
          <img src={product.image} alt={product.name} />
        ) : (
          <div className="no-image">Зураггүй</div>
        )}
      </div>
      <div className="product-info">
        <span className="category-badge">{product.category_name}</span>
        <h3 className="product-name">{product.name}</h3>
        <p className="product-description">{product.description}</p>
        <div className="product-footer">
          <span className="product-price">{formatPrice(product.price)}</span>

          <span
            className={`stock ${
              product.stock > 0 ? "in-stock" : "out-of-stock"
            }`}
          >
            {product.stock > 0 ? `${product.stock} ширхэг` : "Дууссан"}
          </span>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
