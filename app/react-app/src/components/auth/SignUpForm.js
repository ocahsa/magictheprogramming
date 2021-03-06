import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';
import { login, signUp } from '../../store/session';
import './SignUp.css'
import icon from '../../images/logoIcon.png'

const SignUpForm = () => {
  const history = useHistory();

  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data)
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const handleDemo = () => {
    dispatch(login('demo@aa.io', 'password'))
  }

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <div className="sign-container">
      <div className="sign-hero">
        <img className='sign-hero-bg' src="https://www.moxfield.com/img/hero-bg.jpg" alt="hero" />
        <div className="to-home-container">
          <div onClick={() => history.push('/')} className='to-home'>
            <img className='sign-icon' src={icon} alt="logo" />
            <div className="sign-name">Upkeep</div>
          </div>
        </div>
        <div className="sign-title">Deck building made easy.</div>
        <div className="sign-subtitle">Build your Commander Deck for Magic: the Gathering. </div>
      </div>
      <div className="form-container">
        <form onSubmit={onSignUp}>
          <div>
            {errors.map((error, ind) => (
              <div className='redError' key={ind}>{error}</div>
            ))}
          </div>
          <div className="display-flicker form-home-container">
            <div onClick={() => history.push('/')} className='to-home'>
              <img className='sign-icon' src={icon} alt="logo" />
              <div className="sign-name">Upkeep</div>
            </div>
          </div>
          <h1>Register for Upkeep</h1>
          <h3>User Name</h3>
          <div className='form-item'>
            <input
              type='text'
              name='username'
              onChange={updateUsername}
              value={username}
            ></input>
          </div>
          <h3>Email</h3>
          <div className='form-item'>
            <input
              type='email'
              name='email'
              onChange={updateEmail}
              value={email}
            ></input>
          </div>
          <h3>Password</h3>
          <div className='form-item'>
            <input
              type='password'
              name='password'
              onChange={updatePassword}
              value={password}
            ></input>
          </div>
          <h3>Confirm Password</h3>
          <div className='form-item'>
            <input
              type='password'
              name='repeat_password'
              onChange={updateRepeatPassword}
              value={repeatPassword}
              required={true}
            ></input>
          </div>
          <div className="switch">
            <button type='submit'>Sign Up</button>
            <div>Already have an account? <span onClick={() => history.push('/login')}>Log In</span> or  <span onClick={handleDemo}>Demo Login</span></div>
          </div>
        </form>
        </div>
      </div>
  );
};

export default SignUpForm;
