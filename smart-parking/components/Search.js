import React from "react";

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

const Search = props => {
    return (
        <div className="input-group" style={searchStyle}>
            <div className="input-group-prepend" >
                <p className="lead" style={subtitle}>Search your plate number: </p>
            </div>
            <input type="text" className="form-control" style={inputStyle} />
        </div>
    );
};

export default Search;