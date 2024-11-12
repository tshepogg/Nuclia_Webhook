// frontend/src/AbbyAssistant.js
import React, { useState } from 'react';
import { searchQuery } from './api';

function AbbyAssistant() {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState('');

    const handleSearch = async () => {
        const result = await searchQuery(query);
        if (result.error) {
            setResponse(`Error: ${result.message}`);
        } else {
            setResponse(result.text ? result.text : "No response found.");
        }
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Enter your question"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button onClick={handleSearch}>Ask Abby</button>
            <div className="response">
                <p>{response}</p>
            </div>
        </div>
    );
}

export default AbbyAssistant;
