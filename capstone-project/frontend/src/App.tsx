import Header from "./component/header.tsx"
import Footer from "./component/footer.tsx"
import Banner from "./component/banner.tsx"
import Page from "./component/page.tsx"
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
      <Footer/>
    </>
  )
}

export default App
