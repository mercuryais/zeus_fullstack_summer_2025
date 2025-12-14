import { useState, useEffect } from 'react';
import type { Product, Category } from '../types';
import { getProducts, getCategories } from '../services/api';


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
                console.error('Initial data fetch error:', err);
            }
        };
        fetchInitialData();
    }, []);
    if (loading) return <div>Түр хүлээнэ үү...</div>;
    if (error) return <div>{error}</div>;
    return (
    <div className="products-page">
      <header className="page-header">
        <h1>Бүтээгдэхүүнүүд</h1>
      </header>

      <section>
        <h2>Ангилалууд</h2>
        <ul>
          {categories.map(category => (
            <li key={category.id}>{category.name}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Бүтээгдэхүүнүүд</h2>
        <ul>
          {products.map(product => (
            <li key={product.id}>
              {product.name} - ${product.price}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
};
export default ProductsPage;