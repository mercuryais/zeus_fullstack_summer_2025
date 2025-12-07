import Header from "./component/header.tsx"
import Footer from "./component/footer.tsx"
import Banner from "./component/banner.tsx"
import Page from "./component/page.tsx"
import Browse from "./component/browse.tsx"
import Share from "./component/share.tsx"
import PFeatures  from "./component/product_features.tsx"
function App() {

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
      currentPage="Cart" 
      pageImg="imgs/shop.jpg"/>
      <Banner bannerUrl="/imgs/banner.jpg"/>
      <Browse 
      diningPic="/imgs/browse_1.png"
      livingPic="/imgs/browse_2.png"
      bedroomPic="imgs/browse_3.png"
      />
      <Share 
      shareImg1="/imgs/share_1.png"
      shareImg2="/imgs/share_2.png"
      shareImg3="/imgs/share_3.png"
      shareImg4="/imgs/share_4.png"
      shareImg5="/imgs/share_5.png"
      shareImg6="/imgs/share_6.png"
      shareImg7="/imgs/share_7.png"
      shareImg8="/imgs/share_8.png"
      shareImg9="/imgs/share_9.png"/>
      <PFeatures 
      trophyIcon="/imgs/product-features_trophy.png"
      guarenteeIcon="/imgs/product-features_guarentee.png"
      shippingIcon="/imgs/product-features_shipping.png"
      supportIcon="/imgs/product-features_customer_support.png"
      />
      <Footer/>
    </>
  )
}

export default App
