import React from 'react';
import ReactDOM from 'react-dom';

class Home extends React.Component {
  render() {
    return <h>Hello world</h>
  }
}

ReactDOM.render(
  <Home />,
  document.getElementById('root')
);
