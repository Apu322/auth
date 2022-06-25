import './App.css';
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import LoginPage from './components/Pages/LoginPage'
import HomePage from './components/Pages/HomePage'
import SignUpPage from './components/Pages/SignupPage'
function App() {
    return (
      <BrowserRouter>
      <AuthCheck>
      <Routes>
        <Route path = "/" element = {<LoginPage/>}/>
        <Route path = "/home" element = {<HomePage/>}/>
        <Route path = "/signup" element = {<SignUpPage/>}/>
      </Routes>
      </AuthCheck>
      </BrowserRouter>
    );
  }

export default App;