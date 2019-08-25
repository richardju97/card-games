import React from 'react';
import ReactDOM from 'react-dom';
import "./views/index.css";

class Home extends React.Component {
  render() {
    return (
      <NavBar />
    );
  }
}

function NavBar(props) {
  return (
    <div class="navbar">
      <h1>Blackjack Bot</h1>
      <div class="nav-links">
        <button>View Code</button>
        <button>Authors</button>
      </div>
    </div>
  );
}

ReactDOM.render(
  <Home />,
  document.getElementById('root')
);
