import { useState } from "react";
import axios from "axios";

import InputBox from "./components/inputBox/InputBox";
import Parties from "./components/parties/Parties";
import styles from "./AppStyles";

function App() {
  const { root } = styles;

  const [results, setResults] = useState();
  const [search, setSearch] = useState();
  const [show, setShow] = useState(true);
  const [cards, setCards] = useState(false);

  const apiCall = async (search) => {
    // use axios to get results
    // pass responses into parties
    setShow(false);
    setCards(true);
    const response = await axios
      .get(`https://poliviews-api.herokuapp.com/api/search?query=${search}`)
      .then((res) => {
        return res.data;
      })
      .catch((err) => {
        console.log(err);
      })
    setResults(response);
    setSearch(search);
    setShow(true);
  };

  return (
    <div style={root}>
      <InputBox show={show} retrieveInfo={apiCall} />
      <Parties cards={cards} results={results} search={search} show={show} />
    </div>
  );
}

export default App;
