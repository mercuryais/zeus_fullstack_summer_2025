interface ProfileProps {
    name: string;
    imgUrl: string;
    profession: string;
    age: number;
    width: number;
    height: number;
}

// function parameter
function Profile(props: ProfileProps) {
    console.log(props)
    return(
        <>  
            <h1>{props.name}</h1>   
            <img 
                width={props.width}
                height={props.height}
                src={props.imgUrl} /> 
            <p>
                <ul>Profession: {props.profession}</ul>
                <ul>Age: {props.age}</ul>
            </p>
        </>
    )
}

export default Profile;