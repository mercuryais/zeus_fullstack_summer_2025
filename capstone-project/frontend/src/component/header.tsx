interface NavigationBar {
  logoPic: string;
  accountIcon: string;
  searchIcon: string;
  likedIcon: string;
  cartIcon: string;
}

function Header(props: NavigationBar) {
  return (
    <>
      <div className="nav">
        <div className="nav-items">
          <div className="group-1">
            <div className="logo">
              <img width={50} height={32} src={props.logoPic} />
              <a href="#">Furniro</a>
            </div>
          </div>
          <div className="group-2">
            <ul>
              <li>
                <a href="#">Home</a>
              </li>
              <li>
                <a href="#">Shop</a>
              </li>
              <li>
                <a href="#">About</a>
              </li>
              <li>
                <a href="#">Contact</a>
              </li>
            </ul>
          </div>
          <div className="group-3">
            <div className="icons">
              <ul>
                <li>
                  <img width={23.33} height={18.67} src={props.accountIcon} />
                </li>
                <li>
                  <img width={22.17} height={22.17} src={props.searchIcon} />
                </li>
                <li>
                  <img width={23.33} height={20.81} src={props.likedIcon} />
                </li>
                <li>
                  <img width={24.53} height={22.06} src={props.cartIcon} />
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Header;
