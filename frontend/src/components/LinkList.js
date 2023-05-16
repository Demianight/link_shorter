import axios from "axios";
import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.css";

class LinkList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      currentLinks: [],
    };
  }

  componentDidMount = () => {
    axios.get("http://127.0.0.1:8000/links/").then((response) => {
      this.setState({ currentLinks: response.data });
    });
  };

  render() {
    let links = this.state.currentLinks.map((item) => (
      <li
        className="list-group-item"
        style={{ backgroundColor: "#eee" }}
        key={item.id}
      >
        {item.name}'s link: <a href={item.original_url}>{item.fake_url}</a>
        <button
          className="btn"
          style={{ backgroundColor: "pink", marginLeft: "2%" }}
          onClick={() => {
            navigator.clipboard.writeText(item.fake_url);
          }}
        >
          Copy
        </button>
      </li>
    ));

    return (
      <div>
        <ul className="list-group" style={{ gap: "5px" }}>
          {links}
        </ul>
      </div>
    );
  }
}

export default LinkList;
