import type { BannerInter } from "../types";
function Banner(props: BannerInter) {
  return (
    <>
      <div className="banner">
        <img
          className="bannerPic"
          width={1440}
          height={712}
          src={props.bannerUrl}
        />
        <div className="banner-ad">
          <div className="banner-ad-content">
            <p>New Arrival</p>
            <h3>Discover Our <br /> New Collection</h3>
            <p className="lorem">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste
              quasi esse ad, asperiores odit explicabo?
            </p>
            <button>BUY NOW</button>
          </div>
        </div>
      </div>
    </>
  );
}
export default Banner;
