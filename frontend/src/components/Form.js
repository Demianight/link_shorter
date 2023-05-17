import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.css";
import axios from "axios";
import LinkList from "./LinkList";

class Form extends Component {
  constructor(props) {
    super(props);

    this.state = {
      original_url: "",
      name: "",
    };
  }

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  };

  handleSubmit = (e) => {
    axios
      .post("http://127.0.0.1:8000/links/", this.state)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => alert(error));
    e.preventDefault();
    alert("Please reload the page. Still in production....");
  };

  render() {
    const { original_url, name } = this.state;
    return (
      <>
        <form
          className="form-group d-flex justify-content-between pb-4"
          onSubmit={this.handleSubmit}
        >
          <input
            name="name"
            className="w-15"
            placeholder="Please insert your name"
            onChange={this.handleChange}
            value={name}
          />
          <input
            type="text"
            name="original_url"
            onChange={this.handleChange}
            value={original_url}
            placeholder="Insert your link"
            className="w-75"
          />
          <button
            className="btn btn-primary btn-square-md w-50 h-100"
            type="submit"
            style={{ backgroundColor: "grey", borderColor: "grey" }}
          >
            Submit
          </button>
        </form>
        <LinkList />
      </>
    );
  }
}

export default Form;
