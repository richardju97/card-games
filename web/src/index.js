import React from 'react';
import ReactDOM from 'react-dom';
import './views/index.css';

class Home extends React.Component {
  render() {
    return (
      <NavBar />
    );
  }
}

function NavBar(props) {
  return (
    <div className='navbar'>
      <h1>Blackjack Bot</h1>
      <div className='nav-links'>
        <button><a href='https://github.com/richardju97/card-games' target="_blank" rel="noopener noreferrer">View Code</a></button>
        <button>Authors</button>
      </div>
    </div>
  );
}

ReactDOM.render(
  <Home />,
  document.getElementById('root')
);
