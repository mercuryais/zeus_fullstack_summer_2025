import type { Product } from "../types";
import ProductCard from "./ProductCard";
interface ProductListProps {
  products: Product[];
  loading: boolean;
  error: string | null;
}
const ProductList = ({ products, loading, error }: ProductListProps) => {
    console.log(products);
  if (loading) {
    return <div className="loading">Уншиж байна...</div>;
  }
  if (error) {
    return <div className="error">Алдаа: {error}</div>;
  }
  if (products.length === 0) {
    return <div className="no-products">Бүтээгдэхүүн олдсонгүй</div>;
  }
  return (
    <div className="product-grid">
      {products && products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};
export default ProductList;
