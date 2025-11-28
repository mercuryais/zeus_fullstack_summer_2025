import NavigationBar from "./component/header.tsx"

function App() {

  return (
    <>  
    <NavigationBar 
      widthLogo={50}
      heightLogo={32}
      heightIcon={28}
      widthIcon={28}
      logoUrl="./public/imgs/logo.png"
      name="Furnio"
      menuHome="Home"
      menuAbout="About"
      menuContact="Contact"
      menuShop="Shop"
      accountIcon="./public/imgs/account.png"
      searchIcon="./public/imgs/search.png"
      likedIcon="./public/imgs/liked.png"
      cartIcon="./public/imgs/cart.png"
      />
    </>
  )
}

export default App
