export interface Category {
    id: number;
    name: string;
    description: string;
    created_at: string;
}
export interface Product {
    id: number;
    name: string;
    description: string;
    price: string;
    stock: number;
    category: number;
    category_name: string;
    image: string | null;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}
export interface ProductStats {
    total_products: number;
    active_products: number;
    total_categories: number;
    out_of_stock: number;
}
export interface ProductFilters {
    category?: number;
    search?: string;
    min_price?: number;
    max_price?: number;
}