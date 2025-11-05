interface Product {
    id: number,
    title: string,
    price: number,
    images: string[],
}
interface APIResponse {
    products: Product[]
}
async function fetchProducts(): Promise<Product[]> {
    const api_url ='https://dummyjson.com/products';
    try {
        const response = await fetch(api_url)
        if (!response.ok) {
            throw new Error(`HTTP Error! Status: ${response.status}`);
            
        } 
        const data = await response.json() as APIResponse
        return data.products;
    } catch (error){
        console.log('Could not fetch the API url', error);
        return []
    }
}

function displayProducts (products: Product[]): void {
    const productList = document.getElementById('product-list')
    if (!productList) return;
    productList.innerHTML = '';
    products.map((product) => {
        const li = document.createElement('li');
        li.textContent = `${product.title} - `;
        const priceStrong = document.createElement('strong');
        priceStrong.textContent = `${product.price}`;
        const images = document.createElement('img');
        images.src = `${product.images[0]}`

        li.appendChild(priceStrong);
        productList.appendChild(li)
        li.appendChild(images)

    });
}
async function main() {
    const products = await fetchProducts()
    console.log(products)
    displayProducts(products)
}

document.addEventListener('DOMContentLoaded', main)