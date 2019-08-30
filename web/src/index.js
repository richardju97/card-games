import React from 'react';
import ReactDOM from 'react-dom';
import './views/index.css';
import Simulation from './simulation.js';

class Home extends React.Component {
  render() {
    return (
      <div className='content'>
        <NavBar />
        <Instructions />
        <Simulation />
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
        <strong>Probability: </strong>Hits if probability of losing (calculated based on player's hand) is below a specified threshold<br />
        <strong>Perceptron: </strong>A variation of Probability Bot where the probability of losing is calculated based on a linear combination
                                    of multiple variables such as the dealer's hand and other players' hands<br />
        <strong>Basic Strategy: </strong>Based on strategy found <a className='link' href='https://bicyclecards.com/how-to-play/blackjack/?fbclid=IwAR21VaLpNnnYp5r5rDQkKJS-54RE7q-M8L9iMl0qawLGep0X4eR3bRdvC10' target='_blank' rel='noopener noreferrer'>here</a>
      </p>
    </div>
  )
}

ReactDOM.render(
  <Home />,
  document.getElementById('root')
);
