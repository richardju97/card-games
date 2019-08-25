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
          <div className='simulation-form'>
            <BotType />
            <NumSims />
          </div>
        </div>
        <ProgressBar />
      </div>
    );
  }
}

class BotType extends React.Component {
  render() {
    return (
      <div>
        <h3>Select Bot Type</h3>
        <select className='input select'>
          <option value='none'></option>
          <option value='greedy'>Greedy</option>
          <option value='probability'>Probability</option>
          <option value='perceptron'>Perceptron</option>
          <option value='basic strategy'>Basic Strategy</option>
        </select><br />
        <button className='form-button'>Next</button>
      </div>
    );
  }
}

class NumSims extends React.Component {
  render() {
    return (
      <div>
        <h3>Enter Number of Simulations</h3>
        <input className='input' type='text' /><br />
        <button className='form-button'>Simulate</button>
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
