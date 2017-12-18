import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  componentDidMount() {
    this.getUsers();
  }

  getUsers() {
    const url = 'http://192.168.99.100/users';

    // axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    axios.get(url)
    // .then((res) => { this.setState({ users: res.data.data.users }); })
    .then((res) => { console.log({ users: res.data.data.users }); })
    .catch((err) => { console.log(err); })
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React by Yuki in the docker Hello</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
