export interface BannerInter {
  bannerUrl: string;
}
export interface browseInter {
  diningPic: string;
  livingPic: string;
  bedroomPic: string;
}
export interface NavigationBar {
  logoPic: string;
  accountIcon: string;
  searchIcon: string;
  likedIcon: string;
  cartIcon: string;
}
export interface pageInter {
  pageImg: string;
  currentPage: string;
  logoPic: string;
  arrow: string;
}
export interface pFeatures {
  trophyIcon: string;
  guarenteeIcon: string;
  shippingIcon: string;
  supportIcon: string;
}
export interface shareInter {
  shareImg1: string;
  shareImg2: string;
  shareImg3: string;
  shareImg4: string;
  shareImg5: string;
  shareImg6: string;
  shareImg7: string;
  shareImg8: string;
  shareImg9: string;
}

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
