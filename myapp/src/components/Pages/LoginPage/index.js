
import React, { useState, useEffect } from 'react';
import {useNavigate, Routes, Route} from "react-router-dom";
import axios from 'axios';

const LoginPage = () => {

    async function handleLogin (e) {
    e.preventDefault();
    console.log('' + arr[0] +  arr[1])
    fetch('http://localhost:8000/token-auth/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(
        {username: arr[0],
         password: arr[1]}
      )
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token);
        localStorage.setItem('username', json.user.username);
        navigate('/home')
      });
    }


    const navigate = useNavigate();
    const handle = () => {
        let path = '/';
        navigate(path)
    }
   


    const arr = []
    return (
        <div>
        <input type = 'text' value = {arr[0]} onChange = {(e) => {arr[0] = e.currentTarget.value}}></input>
        <input type = 'password' value = {arr[1]} onChange = {(e) => {arr[1] = e.currentTarget.value}}></input>
        <button onClick = {(e, username, password) => handleLogin(e, username, password)}>Log in</button>
        </div> 
    )
}
export default LoginPage 