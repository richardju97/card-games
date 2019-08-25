import React from 'react';
import './views/index.css';
import './views/simulation.css';

class EndSim extends React.Component {
  render() {
    return (
      <div className='simulation-form'>
        <h3>Simulation Complete!</h3>
        <button className='back-button' onClick={() => this.props.next(-1)}>Back</button>
        <button className='form-button' onClick={() => this.props.next(-2)}>Restart</button>
      </div>
    )
  }
}

export default EndSim;
