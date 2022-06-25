
import React, { useState, useEffect } from 'react';
import {useNavigate, Routes, Route} from "react-router-dom";
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

const LoginPage = () => {

    const [data, setData] = useState(null)
    const username = localStorage.getItem('username')
    const token = localStorage.getItem('token')
        useEffect(() => {
            const opts = {
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `JWT ${token}`
                }
            }
            const res = await axios.get(`http://127.0.0.1:8000/core/customer/${username}/`, opts)
            setData(res.data)
        }, [])

    const navigate = useNavigate();
    const handle = () => {
        let path = '/';
        navigate(path)
    }
   


    const arr = []
    return (
        <div>
            <p>
                {localStorage.getItem('username')}
                
                {
                    data?.map((e) => (
                        <p>
                            {e.company}
                        </p>
                    )
                    )
                }
            </p>
        </div>
    )
}
export default LoginPage 