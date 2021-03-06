import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router';
import { logout } from '../../store/session';
import './logoutbutton.css'

const LogoutButton = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  
  const onLogout = async (e) => {
    await dispatch(logout());
    history.push("/")
  };

  return <button className="logout-button" onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
