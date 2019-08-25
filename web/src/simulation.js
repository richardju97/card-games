import React from 'react';
import {Route, Link, BrowserRouter as Router, Redirect} from 'react-router-dom';
import './views/index.css';
import './views/simulation.css';

import BotType from './bot-type.js';
import NumSims from './num-sims.js';

class Simulation extends React.Component {
  constructor(props) {
    super(props);
    this.updateStep.bind(this);
    this.state = {
      formStep: 1,
      stepMap: {1: <BotType next={this.updateStep.bind(this)}/>, 2: <NumSims next={this.updateStep.bind(this)}/>},
    }
  }

  updateStep() {
    this.setState({formStep: this.state.formStep + 1});
  }

  render() {
    return (
      <div>
        <div className='paragraph'>
          <h2>Simulation</h2>
          <p> Select a type of bot and the number of games to be simulated. </p>
          {this.state.stepMap[this.state.formStep]}
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
