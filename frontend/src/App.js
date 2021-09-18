import { useState } from 'react';
import axios from 'axios';
import { CircularProgress } from '@chakra-ui/progress';

import InputBox from './components/inputBox/InputBox';
import Parties from './components/parties/Parties';
import './App.css';

function App() {
  const [result, setResult] = useState("")
  const apiCall = () => {
    // use axios to get results
    // pass responses into parties

  }

  return (
    <div className="App">
      <InputBox retrieveInfo={apiCall} />
      <Parties results={result} />
      <div>
        <CircularProgress isIndeterminate color="green" />
      </div>
    </div>
  );
}

export default App;
