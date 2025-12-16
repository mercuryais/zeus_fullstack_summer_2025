import { useState, useEffect } from "react";
import type { Product, Category } from "../types";
import { getProducts, getCategories } from "../services/api";

const ProductsPage = () => {
  // State-үүд
  const [products, setProducts] = useState<Product[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Анх ачаалах үед categories болон stats авах
  useEffect(() => {
    const fetchInitialData = async () => {
      try {
        const [productData, categoryData] = await Promise.all([
          getProducts(),
          getCategories(),
        ]);
        setProducts(productData);
        setCategories(categoryData);
      } catch (err) {
        console.error("Initial data fetch error:", err);
        setError(err instanceof Error ? err.message : String(err));
      } finally {
        setLoading(false);
      }
    };
    fetchInitialData();
  }, []);
  if (loading) return <div>Түр хүлээнэ үү...</div>;
  if (error) return <div>{error}</div>;
  return (
    <div className="products-page">
      <header className="page-header">
        <h1>Our Products</h1>
      </header>
      <section>
        <ul>
          {products.map((product) => (
            <div className="product-card">
              <li key={product.id}>
                <img src={product.image} width={285} height={301} />
                <div className="text-content">
                  <div className="sale">{product.sale}%</div> 
                  <div className="name">{product.name}</div>
                  <div className="description">{product.description}</div>
                  <div className="price">Rp {product.price}</div>
                </div>

              </li>
            </div>
          ))}
        </ul>
      </section>
    </div>
  );
};
export default ProductsPage;
