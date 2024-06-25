import React, { useState } from 'react';
import axios from 'axios';

const CreateCustomer = () => {
    const [customer, setCustomer] = useState({
        first_name: '',
        last_name: '',
        phone_number: '',
        address: ''
    });

    const handleChange = (e) => {
        setCustomer({
            ...customer,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/accounts/api/customers/create/', customer)
            .then(response => console.log(response))
            .catch(error => console.error(error));
    };

    return (
        <div>
            <h1>Create Customer</h1>
            <form onSubmit={handleSubmit}>
                <input name="first_name" value={customer.first_name} onChange={handleChange} placeholder="First Name" required />
                <input name="last_name" value={customer.last_name} onChange={handleChange} placeholder="Last Name" required />
                <input name="phone_number" value={customer.phone_number} onChange={handleChange} placeholder="Phone Number" required />
                <input name="address" value={customer.address} onChange={handleChange} placeholder="Address" required />
                <button type="submit">Create</button>
            </form>
        </div>
    );
};

export default CreateCustomer;