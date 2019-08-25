import React from 'react';
// import {Route, Link, BrowserRouter as Router, Redirect} from 'react-router-dom';
import './views/index.css';
import './views/simulation.css';

class NumSims extends React.Component {
  render() {
    return (
      <div className="simulation-form">
        <h3>Enter Number of Simulations</h3>
        <input className='input' type='text' /><br />
        <button className='back-button' onClick={() => this.props.next(-1)}>Back</button>
        <button className='form-button' onClick={() => this.props.next(1)}>Simulate</button>
      </div>
    );
  }
}

export default NumSims;
