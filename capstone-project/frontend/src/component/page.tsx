import type { pageInter } from "../types";
function Page(props: pageInter) {
    return (
        <>
        <div className="page">
            <img className="page-background"
            width={1440}
            src={props.pageImg} />
            <div className="home-page">
                <img 
                width={77}
                height={77}
                src={props.logoPic}
                />
                <h3>{props.currentPage}</h3>
                <a href="#">Home </a>
                <img 
                className="arrowPic"
                width={20}
                height={20}
                src={props.arrow} />
                <p>{props.currentPage}</p>
            </div>
        </div>
        </>
    )
}
export default Page;