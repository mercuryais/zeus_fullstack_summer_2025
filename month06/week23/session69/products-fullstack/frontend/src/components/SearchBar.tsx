import { useState } from "react";
interface SearchBarProps {
  onSearch: (query: string) => void;
}
const  SearchBar= ({ onSearch }: SearchBarProps) => {
  const [query, setQuery] = useState("");
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(query);
  };
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setQuery(value);
    // Бичиж байх үед хайх (debounce хийж болно)
    if (value.length >= 2 || value.length === 0) {
      onSearch(value);
    }
  };
  
  return (
    <form className="search-bar" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Бүтээгдэхүүн хайх..."
        value={query}
        onChange={handleChange}
      />
      <button type="submit">Хайх</button>
    </form>
  );
};
export default SearchBar;
