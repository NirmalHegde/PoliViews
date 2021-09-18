import { useState } from "react";
import axios from "axios";

import InputBox from "./components/inputBox/InputBox";
import Parties from "./components/parties/Parties";
import styles from "./AppStyles";

function App() {
  const { root } = styles;

  const [results, setResults] = useState();
  const [search, setSearch] = useState();
  const apiCall = (search) => {
    // use axios to get results
    // pass responses into parties
    setResults(["Hello", "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn", "Hello", "Hello", "Hello", "Hello"]);
    setSearch(search);
  };

  return (
    <div style={root}>
      <InputBox retrieveInfo={apiCall} />
      <Parties results={results} search={search} />
    </div>
  );
}

export default App;