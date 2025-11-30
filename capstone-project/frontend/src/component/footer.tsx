function Footer() {
  return (
    <>
      <footer className="footer">
        <div className="footer-content">
          <div className="footer-upper">
            <div className="hq-location">
              <h3>Funiro.</h3>
              <p>400 University Drive Suite 200 Coral Gables,<br /> FL 33134 USA</p>
            </div>
            <div className="links">
              <ul>
                <li>
                  <p>Links</p>
                </li>
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
            <div className="help">
              <ul>
                <li>
                  <p>Help</p>
                </li>
                <li>
                  <a href="#">Payment Options</a>
                </li>
                <li>
                  <a href="#">Returns</a>
                </li>
                <li>
                  <a href="#">Privacy Policies</a>
                </li>
              </ul>
            </div>
            <div className="news-letter">
              <p>Newsletter</p>
              <div className="email-subscribe">
                <form action="subscribe">
                  <input type="email" placeholder="Enter Your Email Address" />
                  <button type="submit">SUBSCRIBE</button>
                </form>
              </div>
            </div>
          </div>
          <div className="footer-copyright">
            <p>2023 furino. All rights reverved</p>
          </div>
        </div>
      </footer>
    </>
  );
}
export default Footer;
