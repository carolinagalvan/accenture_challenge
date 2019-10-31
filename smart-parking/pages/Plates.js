import React from "react";
import styled from "styled-components";
import PlateCard from "../components/PlateCard";
import { Container, Row, Col } from "react-bootstrap";

const StyledRow = styled(Row)`
  padding: 50px;
  margin: auto;
  box-sizing: border-box;
  min-width: 300px;
`;

const subtitle = {
    fontSize: "30px",
    marigin: "auto"
};

const inputStyle = {
    border: "0px",
    borderRadius: "10px",
    background: "#d4e9ff",
    maxWidth: "300px",
    marginLeft: "5px"
};

const searchStyle = {
    marginLeft: "60px",
    marginTop: "40px"
};

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
    constructor(props) {
        super(props);

        this.state = {
            plates: plates,
            result: plates,
        }

        this.filterList = this.filterList.bind(this);
    }

    componentWillReceiveProps(nextProps) {
        this.setState({
            plates: nextProps.plates,
        });

    }

    filterList(event) {
        let value = event.target.value;
        let plates = this.state.plates, result = [];
        result = plates.filter((plate) => {
            return plate.license.search(value) != -1;
        });
        this.setState({ result: result });
    }

    render() {
        const plateList = this.state.result.map((plate) => {
            return <Col className="col-md-4">
                <PlateCard
                    license={plate.license}
                    date={plate.date}
                    photo={plate.photo}
                />
            </Col>;
        });

        return (
            <Container>
                <div className="input-group" style={searchStyle}>
                    <div className="input-group-prepend" >
                        <p className="lead" style={subtitle}>Search your plate number: </p>
                    </div>
                    <input value={this.state.input} type="text" className="form-control" style={inputStyle} onChange={this.filterList} />
                </div>
                <StyledRow>
                    {plateList}
                </StyledRow>
            </Container>
        );
    }
}