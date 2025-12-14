import type { shareInter } from "../types";
function Share(props: shareInter) {
  return (
    <>
      <div
        className="share"
        style={{ position: "relative", overflow: "hidden", height: 780, margin: "80px 0"}}
      >
        <div className="share-title" style={{textAlign: "center"}}>
          <h5
            style={{
              color: "#616161",
              fontWeight: 600,
              fontSize: 20,
              lineHeight: "150%",
            }}
          >
            Share your setup with
          </h5>
          <h2
            style={{
              fontWeight: 700,
              fontSize: 40,
              lineHeight: "120%",
              color: "#3a3a3a",
            }}
          >
            #FuniroFurniture
          </h2>
        </div>

        <div className="imgs" style={{ overflow: "hidden" }}>
          <img
            style={{
              position: "absolute",
              top: 50,
              left: -200,
            }}
            width={274}
            height={382}
            src={props.shareImg1}
          />
          <img
            style={{
              position: "absolute",
              top: 120,
              left: 90,
            }}
            width={451}
            height={312}
            src={props.shareImg2}
          />

          <img
            style={{
              position: "absolute",
              left: 555,
              top: 200,
            }}
            width={295}
            height={392}
            src={props.shareImg3}
          />

          <img
            style={{
              position: "absolute",
              top: 145,
              left: 865,
            }}
            width={290}
            height={348}
            src={props.shareImg4}
          />

          <img
            style={{
              position: "absolute",
              top: 58,
              right: -155,
            }}
            width={425}
            height={433}
            src={props.shareImg5}
          />

          <img
            style={{
              position: "absolute",
              top: 445,
              left: -200,
            }}
            width={381}
            height={323}
            src={props.shareImg6}
          />

          <img
            style={{
              position: "absolute",
              top: 445,
              left: 197,
            }}
            width={344}
            height={242}
            src={props.shareImg7}
          />

          <img
            style={{
              position: "absolute",
              top: 505,
              right: 397,
            }}
            width={178}
            height={242}
            src={props.shareImg8}
          />

          <img
            style={{
              position: "absolute",
              top: 505,
              right: 125,
            }}
            width={258}
            height={196}
            src={props.shareImg9}
          />
        </div>
      </div>
    </>
  );
}
export default Share;
