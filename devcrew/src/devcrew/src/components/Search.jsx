import React from 'react';
import { useState } from 'react';
import { CSVLink } from 'react-csv';
import axios from 'axios';

const Search = () => {
  const [results, setResults] = useState([]);

  const fetchResults = async () => {
    const response = await axios.get(`${process.env.REACT_APP_CASPIO_API_URL}/search`);
    setResults(response.data);
  };

  const headers = [
    { label: 'First Name', key: 'First_Name' },
    { label: 'Description', key: 'Description' },
  ];

  return (
    <div>
      <button onClick={fetchResults}>Search</button>
      <CSVLink data={results} headers={headers} filename='search_results.csv'>
        <button>Export to CSV</button>
      </CSVLink>
      <ul>
        {results.map((result, index) => (
          <li key={index}>{result.First_Name}: {result.Description}</li>
        ))}
      </ul>
    </div>
  );
};

export default Search;