import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

import LandingPage from './pages/LandingPage';

function App() {
  //const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('https://soundalike2.vercel.app//flask/hello').then(response => {
      console.log("SUCCESS", response)
      //setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <LandingPage />
  );
}

export default App;
