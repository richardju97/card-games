import React from 'react';
import './views/index.css';
import './views/simulation.css';

class BotType extends React.Component {
  render() {
    return (
      <div className='simulation-form'>
        <h3>Select Bot Type</h3>
        <select className='input select'>
          <option value='none'></option>
          <option value='greedy'>Greedy</option>
          <option value='probability'>Probability</option>
          <option value='perceptron'>Perceptron</option>
          <option value='basic strategy'>Basic Strategy</option>
        </select><br />
        <button className='form-button' onClick={this.props.next}>Next</button>
      </div>
    );
  }
}

export default BotType;
