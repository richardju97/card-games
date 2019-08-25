import React from 'react';
import ReactDOM from 'react-dom';
import './views/index.css';

class Simulation extends React.Component {
  render() {
    return (
      <div className='paragraph'>
        <h2>Simulation</h2>
        <p> Select a type of bot and the number of games to be simulated.
        </p>
      </div>
    );
  }
}

export default Simulation;
