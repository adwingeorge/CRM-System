import logo from './logo.svg';
import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import Profile from './components/Profile';
import CustomerList from './components/CustomerList';
import CustomerDetail from './components/CustomerDetail';
import CreateCustomer from './components/CreateCustomer';
import UpdateCustomer from './components/UpdateCustomer';


function App() {
  return (
      <Router>
          <div>
              <Switch>
                  <Route path="/login" component={Login} />
                  <Route path="/signup" component={Signup} />
                  <Route path="/profile" component={Profile} />
                  <Route path="/customers" component={CustomerList} exact />
                  <Route path="/customers/:id" component={CustomerDetail} />
                  <Route path="/create-customer" component={CreateCustomer} />
                  <Route path="/update-customer/:id" component={UpdateCustomer} />
                  <Route path="/" component={Login} />
              </Switch>
          </div>
      </Router>
  );
}

export default App;