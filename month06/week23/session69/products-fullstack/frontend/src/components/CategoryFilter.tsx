import type { Category } from "../types";
interface CategoryFilterProps {
  categories: Category[];
  selectedCategory: number | null;
  onSelectCategory: (categoryId: number | null) => void;
}
const CategoryFilter = ({
  categories,
  selectedCategory,
  onSelectCategory,
}: CategoryFilterProps) => {
  return (
    <div className="category-filter">
      <h3>Ангилал</h3>
      <div className="category-buttons">
        <button
          className={`category-btn ${
            selectedCategory === null ? "active" : ""
          }`}
          onClick={() => onSelectCategory(null)}
        >
          Бүгд
        </button>
        {categories && categories.map((category) => (
          <button
            key={category.id}
            className={`category-btn ${
              selectedCategory === category.id ? "active" : ""
            }`}
            onClick={() => onSelectCategory(category.id)}
          >
            {category.name}
          </button>
        ))}
      </div>
    </div>
  );
};
export default CategoryFilter;
