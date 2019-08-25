import React from 'react';
import './views/index.css';
import './views/simulation.css';

class Simulation extends React.Component {
  render() {
    return (
      <div>
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
        <ProgressBar />
      </div>
    );
  }
}

class ProgressBar extends React.Component {
  //tutorial: https://www.youtube.com/watch?v=DYevj6UGNWA
  render() {
    return (
      <div className='progress-bar'>
        <ul className='steps'>
          <li className='visited'>1</li>
          <li>2</li>
          <li>3</li>
        </ul>
        <div className='line'></div>
      </div>
    );
  }
}

export default Simulation;
