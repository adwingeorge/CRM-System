import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from './components/Signup';
import Login from './components/Login';
import Profile from './components/Profile';
import CustomerList from './components/CustomerList';
import CustomerDetail from './components/CustomerDetail';
import CreateCustomer from './components/CreateCustomer';
import UpdateCustomer from './components/UpdateCustomer';
import DeleteCustomer from './components/DeleteCustomer';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/customers" element={<CustomerList />} />
        <Route path="/customers/:id" element={<CustomerDetail />} />
        <Route path="/create-customer" element={<CreateCustomer />} />
        <Route path="/update-customer/:id" element={<UpdateCustomer />} />
        <Route path="/delete-customer/:id" element={<DeleteCustomer />} />
      </Routes>
    </Router>
  );
}

export default App;