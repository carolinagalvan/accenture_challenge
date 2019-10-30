import React from "react";
import styled from "styled-components";
import PlateCard from "../components/PlateCard";
import Search from '../components/Search'
import { Container, Row, Col } from "react-bootstrap";

const StyledRow = styled(Row)`
  padding: 50px;
  margin: auto;
  box-sizing: border-box;
  min-width: 300px;
`;

const plates = [
    {
        id: 1,
        license: "RTC083A",
        date: "October 30, 2019",
        photo: "/static/plate1.png"
    },
    {
        id: 2,
        license: "SJU4153",
        date: "October 29, 2019",
        photo: "/static/plate2.png"
    },
    {
        id: 3,
        license: "RNA513A",
        date: "October 30, 2019",
        photo: "/static/plate3.png"
    },
    {
        id: 4,
        license: "SST8420",
        date: "October 28, 2019",
        photo: "/static/plate4.png"
    }
];

export default class Plates extends React.Component {
    render() {
        return (
            <Container>
                <Search></Search>
                <StyledRow>
                    {plates.map(plate => {
                        return (
                            <Col className="col-md-4">
                                <PlateCard
                                    license={plate.license}
                                    date={plate.date}
                                    photo={plate.photo}
                                />
                            </Col>
                        );
                    })}
                </StyledRow>
            </Container>
        );
    }
}