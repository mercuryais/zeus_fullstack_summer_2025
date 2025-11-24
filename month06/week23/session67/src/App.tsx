import Profile from "./components/Profile";
import Button from "./components/Button";
import Card from "./components/Card";
import ProductCard from "./components/ProductCard";

function App() {
  // jsx - javascript xml
  const element = <h1>Hello!</h1>;

  // react fragment
  // Ганцхан root element буюу div, or empty <><>
  // <br/> <img/> close all the tags
  // Has to type className insted of class attribute
  // Always write js inside {}
  return (
    <div className="" id="">

      <div style={{display: 'flex', flexWrap: 'wrap'}}>
        <ProductCard
          title="Laptop"
          price={2500000}
          description="High spec, powerful modern computer"
          imageUrl="https://plus.unsplash.com/premium_photo-1681302427948-2fd0eca629b1?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bGFwdG9wfGVufDB8fDB8fHww"
          inStock={true}
        />
        <ProductCard
          title="Smartphone"
          price={1500000}
          description="Useless is phone"
          imageUrl="https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c21hcnRwaG9uZXxlbnwwfHwwfHx8MA%3D%3D"
          inStock={false}
        />

      </div>
      <Card>
          <h2>Гарчиг</h2>
          <p>Энэ бол картын доторх текст байна.</p>
      </Card>

      <Card>
        <h3>Өөр карт</h3>
        <ul>
          <li>Зүйл 1</li>
          <li>Зүйл 2</li>
        </ul>
      </Card>
    {element}
    <Button text="Click"/>
    <Button text="Click" color="red" />
    <Profile name="Khangaikhuu" age={43} profession="Software Engineer" width={200} height={200} imgUrl="https://images.unsplash.com/photo-1763374547831-03b23e6ec337?q=80&w=1287&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"/>
    <Profile name="Maral" age={20} profession="Student" width={200} height={200} imgUrl="https://images.unsplash.com/photo-1745988371720-f4c31df5e059?q=80&w=1287&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"/>
    <Profile name="Batsuuri" age={20} profession="Bad Student" width={200} height={200} imgUrl="https://images.unsplash.com/photo-1734640132289-b0f47bad7dd1?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDZ8fHxlbnwwfHx8fHw%3D"/>
    <Profile name="Boldoo" age={20} profession="Student" width={200} height={200} imgUrl="https://images.unsplash.com/photo-1608470052465-9f4ec665c84c?q=80&w=1287&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"/>
    </div>
  )
}

export default App;