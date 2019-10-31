import React from "react";

const PlateCardBody = {
    background: "radial-gradient(#e5e5e5e5, #ffff, #e5e5e5)",
    padding: "10px"
};
const PlateCardStyle = {
    boxSizing: "border-box",
    marginBottom: "50px",
};
const Overf = {
    overflow: "hidden"
};
const PlateImg = {
    height: "230px",
    transform: "scale(1)",
    transition: "transform 0.5s ease",
};

const PlateCard = props => {
    return (
        <div className="card text-center" style={PlateCardStyle}>
            <div style={Overf}>
                <img
                    src={props.photo}
                    alt="myPlate"
                    className="card-img-top"
                    style={PlateImg}
                />
            </div>
            <div className="card-body text-dark" style={PlateCardBody}>
                <h4 className="card-title"># {props.license}</h4>
                <p className="card-text text-seconday">{props.date}</p>
            </div>
        </div>
    );
};

export default PlateCard;
