interface pFeatures {
  trophyIcon: string;
  guarenteeIcon: string;
  shippingIcon: string;
  supportIcon: string;
}
function PFeatures(props: pFeatures) {
  return (
    <>
      <div
        className="pfeatures"
        style={{
          height: 270,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          backgroundColor: "#faf3ea"
        }}
      >
        <div
          className="pfeatures-content"
          style={{
            width: 1334,
            height: 70,
            display: "flex",
            justifyContent: "space-between"
          }}
        >
          <div className="high-quality">
            <img 
            src={props.trophyIcon} 
            width={52.77}
            height={60}/>
            <div className="text-part">
              <h4>High Quality</h4>
              <p>crafter from top materials</p>
            </div>
          </div>
          <div className="warranty-protection">
            <img src={props.guarenteeIcon}
            width={60}
            height={58.13} />
            <div className="text-part">
              <h4>Warranty Protection</h4>
              <p>Over 2 years</p>
            </div>
          </div>
          <div className="free-shipping">
            <img src={props.shippingIcon} 
            width={60}
            height={55.97}/>
            <div className="text-part">
              <h4>Free Shipping</h4>
              <p>Order over 150 $</p>
            </div>
          </div>
          <div className="support-247">
            <img src={props.supportIcon} 
            width={52.94}
            height={60}/>
            <div className="text-part">
              <h4>24/7 Support</h4>
              <p>Dedicated support</p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
export default PFeatures;
