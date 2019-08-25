import React from 'react';
import ReactDOM from 'react-dom';
import './views/index.css';

class Home extends React.Component {
  render() {
    return (
      <div className='content'>
        <NavBar />
        <Instructions />
      </div>
    );
  }
}

function NavBar(props) {
  return (
    <div className='navbar'>
      <h1>Blackjack Bot</h1>
      <button><a href='https://github.com/richardju97/card-games' target='_blank' rel='noopener noreferrer'>View Code</a></button>
      <button>Authors</button>
    </div>
  );
}

function Instructions(props) {
  return (
    <div className='paragraph'>
      <h2>Bot Descriptions</h2>
      <p>
        <strong>Greedy: </strong>Always hits<br />
        <strong>Probability: </strong>Based on probability threshold of winning<br />
        <strong>Perceptron: </strong>Weighted decision making<br />
        <strong>Basic Strategy: </strong>Based on strategy found <a className='link' href='https://bicyclecards.com/how-to-play/blackjack/?fbclid=IwAR21VaLpNnnYp5r5rDQkKJS-54RE7q-M8L9iMl0qawLGep0X4eR3bRdvC10' target='_blank' rel='noopener noreferrer'>here</a>
      </p>
    </div>
  )
}

ReactDOM.render(
  <Home />,
  document.getElementById('root')
);
