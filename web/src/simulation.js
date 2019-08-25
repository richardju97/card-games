import React from 'react';
import './views/index.css';
import './views/simulation.css';

class Simulation extends React.Component {
  render() {
    return (
      <div className='paragraph'>
        <h2>Simulation</h2>
        <p> Select a type of bot and the number of games to be simulated. </p>
        <form className='simulation-form'>
          Bot Type:
          <select className='input'>
            <option value='greedy'>Greedy</option>
            <option value='probability'>Probability</option>
            <option value='perceptron'>Perceptron</option>
            <option value='basic strategy'>Basic Strategy</option>
          </select>
          <br />

          Number of simulations:
          <input className='input' type='text' />
          <br />

          <button>Simulate</button>
        </form>
      </div>
    );
  }
}

export default Simulation;
