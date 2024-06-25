import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const CustomerDetail = () => {
    const { id } = useParams();
    const [customer, setCustomer] = useState(null);

    useEffect(() => {
        axios.get(`/accounts/api/customers/${id}/`)
            .then(response => setCustomer(response.data))
            .catch(error => console.error(error));
    }, [id]);

    if (!customer) return <div>Loading...</div>;

    return (
        <div>
            <h1>Customer Detail</h1>
            <p>Name: {customer.first_name} {customer.last_name}</p>
            <p>Phone: {customer.phone_number}</p>
            <p>Address: {customer.address}</p>
        </div>
    );
};

export default CustomerDetail;