import React from "react";
import styled from "styled-components";
import { Col, Row } from 'react-bootstrap';

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
const UserImg = {
    height: "95px",
    borderRadius: "30px",
    marginLeft: "15px"
};
const PlateImg = styled.img`
    height: 230px;
    transform: scale(1);
    transition: transform 0.5s ease;
    :hover {
        transform: scale(1.5);
    }
`

const PlateCard = props => {
    return (
        <div className="card text-center" style={PlateCardStyle}>
            <div style={Overf}>
                <PlateImg
                    src={props.photo}
                    alt="myPlate"
                    className="card-img-top"
                />
            </div>
            <div className="card-body text-dark" style={PlateCardBody}>
                <Row>
                    <Col xs={4}>
                        <img src={props.userPhoto} style={UserImg} />
                    </Col>
                    <Col xs={8}>
                        <h4 className="card-title"># {props.license}</h4>
                        <p className="card-text text-seconday">{props.date}</p>
                    </Col>
                </Row>
            </div>
        </div>
    );
};

export default PlateCard;
