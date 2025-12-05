interface browseInter {
    diningPic: string;
    livingPic: string;
    bedroomPic: string;
}

function Browse(props: browseInter) {
    return <>
        <div className="browse">
            <div className="browse-content">
                <div className="browse-title">
                    <h1>Browse The Range</h1>
                    <p>Lorem ipsum sit amet, consectetur adipiscing elit.</p>
                </div>
                <div className="browse-parts">
                    <div className="dining-part">
                        <img src={props.diningPic} />
                        <h3>Dining</h3>
                    </div>
                    <div className="living-part">
                        <img src={props.livingPic} />
                        <h3>Living</h3>
                    </div>
                    <div className="bedroom-part">
                        <img src={props.bedroomPic} />
                        <h3>Bedroom</h3>
                    </div>
                </div>
            </div>
        </div>
    </>
}
export default Browse;