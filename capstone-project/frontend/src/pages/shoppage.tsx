import Header from "../component/header.tsx";
import Footer from "../component/footer.tsx";
import Page from "../component/page.tsx";
import ProductsPage from "../component/product_card.tsx";
import PFeatures from "../component/product_features.tsx";
function Shop() {
  return (
    <>
      <Header
        logoPic="/imgs/logo.png"
        accountIcon="/imgs/account.png"
        searchIcon="/imgs/search.png"
        likedIcon="/imgs/liked.png"
        cartIcon="/imgs/cart.png"
      />
      <Page
        arrow="/imgs/arrow.png"
        logoPic="/imgs/logo.png"
        currentPage="Shop"
        pageImg="imgs/shop.jpg"
      />

      <ProductsPage />
      <PFeatures
        trophyIcon="/imgs/product-features_trophy.png"
        guarenteeIcon="/imgs/product-features_guarentee.png"
        shippingIcon="/imgs/product-features_shipping.png"
        supportIcon="/imgs/product-features_customer_support.png"
      />
      <Footer />
    </>
  );
}

export default Shop;
