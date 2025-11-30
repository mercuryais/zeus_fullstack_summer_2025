import Header from "./component/header.tsx"
import Footer from "./component/footer.tsx"

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
      <Footer/>
    </>
  )
}

export default App
