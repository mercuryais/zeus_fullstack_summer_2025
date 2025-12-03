import { useState, useEffect } from "react";
import type { Product, Category, ProductStats } from "../types";
import { getProducts, getCategories, getProductStats } from "../services/api";
import ProductList from "../components/ProductList";
import CategoryFilter from "../components/CategoryFilter";

import SearchBar from "../components/SearchBar";
const ProductsPage = () => {
  // State-үүд
  const [products, setProducts] = useState<Product[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [stats, setStats] = useState<ProductStats | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  // Filter state-үүд
  const [selectedCategory, setSelectedCategory] = useState<number | null>(null);
  const [searchQuery, setSearchQuery] = useState("");
  // Анх ачаалах үед categories болон stats авах
  useEffect(() => {
    const fetchInitialData = async () => {
      try {
        const [categoriesData, statsData] = await Promise.all([
          getCategories(),
          getProductStats(),
        ]);
        console.log(categoriesData);
        setCategories(categoriesData.results);
        setStats(statsData);
      } catch (err) {
        console.error("Initial data fetch error:", err);
      }
    };
    fetchInitialData();
  }, []);
  // Filter өөрчлөгдөх бүрт products авах
  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      setError(null);
      try {
        const data = await getProducts({
          category: selectedCategory || undefined,
          search: searchQuery || undefined,
        });
        console.log(data);
        setProducts(data.results);
      } catch (err) {
        setError("Бүтээгдэхүүнүүдийг ачаалахад алдаа гарлаа");
        console.error("Products fetch error:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, [selectedCategory, searchQuery]);
  // Category сонгох handler
  const handleCategorySelect = (categoryId: number | null) => {
    setSelectedCategory(categoryId);
  };
  // Search handler
  const handleSearch = (query: string) => {
    setSearchQuery(query);
  };
  return (
    <div className="products-page">
      <header className="page-header">
        <h1>Бүтээгдэхүүнүүд</h1>
        {/* Статистик */}
        {stats && (
          <div className="stats-bar">
            <div className="stat-item">
              <span className="stat-value">{stats.total_products}</span>
              <span className="stat-label">Нийт</span>
            </div>
            <div className="stat-item">
              <span className="stat-value">{stats.active_products}</span>
              <span className="stat-label">Идэвхтэй</span>
            </div>
            <div className="stat-item">
              <span className="stat-value">{stats.total_categories}</span>
              <span className="stat-label">Ангилал</span>
            </div>
            <div className="stat-item">
              <span className="stat-value">{stats.out_of_stock}</span>
              <span className="stat-label">Дууссан</span>
            </div>
          </div>
        )}
      </header>
      <div className="page-content">
        {/* Sidebar: Filters */}
        <aside className="sidebar">
          <SearchBar onSearch={handleSearch} />
          <CategoryFilter
            categories={categories}
            selectedCategory={selectedCategory}
            onSelectCategory={handleCategorySelect}
          />
        </aside>
        {/* Main: Product List */}
        <main className="main-content">
          <div className="results-info">
            <p>{products.length} бүтээгдэхүүн олдлоо</p>
          </div>
          <ProductList products={products} loading={loading} error={error} />
        </main>
      </div>
    </div>
  );
};
export default ProductsPage;
