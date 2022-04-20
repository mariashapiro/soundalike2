import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'


import LandingPage from './pages/LandingPage';
import InputPage from './pages/InputPage';
import SmoothScroll from './components/SmoothScroll/SmoothScroll';


function App() {
  //const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('https:/soundalike2.vercel.app/flask/hello').then(response => {
      console.log("SUCCESS", response)
      //setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <SmoothScroll>
      <LandingPage flexDirection="row"/>
      <InputPage flexDirection="row-reverse" />
    </SmoothScroll>
  );
}

export default App;
