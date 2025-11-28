interface NavigationBar {
  logoUrl: string;
  name: string;
  menuHome: string;
  menuShop: string;
  menuAbout: string;
  menuContact: string;
  widthLogo: number;
  heightLogo: number;
  accountIcon: string;
  searchIcon: string;
  likedIcon: string;
  cartIcon: string;
  widthIcon: number;
  heightIcon: number;
}

// function parameter
function Profile(props: NavigationBar) {
  return (
    <>
      <div className="nav">
        <div className="nav_contents">
          <div className="logo">
            <img src={props.logoUrl} />
            <a href="#">{props.name}</a>
          </div>
          <div className="menus">
            <ul>
              <li>{props.menuHome}</li>
              <li>{props.menuShop}</li>
              <li>{props.menuAbout}</li>
              <li>{props.menuContact}</li>
            </ul>
          </div>
          <div className="icons">
            <ul>
              <li>
                <img src={props.accountIcon} className="nav-icon-1"/>
              </li>
              <li>
                <img src={props.searchIcon} className="nav-icon-2"/>
              </li>
              <li>
                <img src={props.likedIcon} className="nav-icon-3"/>
              </li>
              <li>
                <img src={props.cartIcon} className="nav-icon-4"/>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </>
  );
}

export default Profile;
