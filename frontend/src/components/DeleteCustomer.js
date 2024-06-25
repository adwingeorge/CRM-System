import React from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const DeleteCustomer = ({ customerId }) => {
  const navigate = useNavigate();

  const handleDelete = async () => {
    try {
      await axios.delete(`/api/customers/${customerId}/`);
      // handle successful deletion
      navigate('/customers');
    } catch (error) {
      // handle error
      console.error(error);
    }
  };

  return <button onClick={handleDelete}>Delete</button>;
};

export default DeleteCustomer;