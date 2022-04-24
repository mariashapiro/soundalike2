import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import {
  Routes,
  Route,
  BrowserRouter
} from 'react-router-dom';

import LandingPage from './pages/LandingPage';
import InputPage from './pages/InputPage';

function App() {
  //const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('https://soundalike2.vercel.app/flask/hello').then(response => {
      console.log("SUCCESS", response)
      //setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<LandingPage />} />
        <Route path="/begin" element={<InputPage />} />
      </Routes>
    </BrowserRouter>
    
    
  );
}

export default App;
