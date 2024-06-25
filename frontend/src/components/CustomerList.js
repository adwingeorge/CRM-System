import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);

    useEffect(() => {
        axios.get('/accounts/api/customers/')
            .then(response => setCustomers(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Customer List</h1>
            <ul>
                {customers.map(customer => (
                    <li key={customer.id}>
                        {customer.first_name} {customer.last_name}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CustomerList;