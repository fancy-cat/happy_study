import './App.css'
import Home from './views/home'
import NotFound from './views/notfound'
import Login from './views/login'
import Add from './views/add'
import { Routes, Route,BrowserRouter } from 'react-router'
import React from 'react';
function App() {
  return (
      <BrowserRouter>
          <Routes>
            <Route path="/" element={<Home />}/>
            <Route path="/login" element={<Login />}/>
            <Route path="/add" element={<Add />}/>
            <Route path="*" element={<NotFound />}/>
          </Routes>
      </BrowserRouter>
  )
}

export default App
