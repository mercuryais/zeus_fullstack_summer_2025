import axios from 'axios';
import type { Category, Product, ProductStats, ProductFilters } from '../types';
// Axios instance үүсгэх
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api',
    headers: {
        'Content-Type': 'application/json',
    },
});

// ============ Category API ============
export const getCategories = async (): Promise<Category[]> => {
    const response = await api.get<Category[]>('/categories/');
    return response.data;
};
export const getCategoryById = async (id: number): Promise<Category> => {
    const response = await api.get<Category>(`/categories/${id}/`);
    return response.data;
};

// ============ Product API ============
export const getProducts = async (filters?: ProductFilters):
Promise<Product[]> => {
    const params = new URLSearchParams();
    if (filters?.category) {    
        params.append('category', filters.category.toString());
    }
    if (filters?.search) {
        params.append('search', filters.search);
    }
    if (filters?.min_price) {
        params.append('min_price', filters.min_price.toString());
    }
    if (filters?.max_price) {
        params.append('max_price', filters.max_price.toString());
    }
    const response = await api.get<Product[]>(`/products/?
        ${params.toString()}`);
    return response.data;
    };
export const getProductById = async (id: number): Promise<Product> => {
    const response = await api.get<Product>(`/products/${id}/`);
    return response.data;
};
export const createProduct = async (product: Partial<Product>):
Promise<Product> => {
    const response = await api.post<Product>('/products/create/', product);
    return response.data;
};
export const updateProduct = async (id: number, product:
Partial<Product>): Promise<Product> => {
    const response = await api.put<Product>(`/products/${id}/`, product);  
    return response.data;
};
export const deleteProduct = async (id: number): Promise<void> => {
    await api.delete(`/products/${id}/`);
};
// ============ Stats API ============
export const getProductStats = async (): Promise<ProductStats> => {
    const response = await api.get<ProductStats>('/stats/');
    return response.data;   
};
export default api;