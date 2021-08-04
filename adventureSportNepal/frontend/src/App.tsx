import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  getData,
  selectData,
  selectStatus
} from './reducers/fetchData';

export default function App() {
  const data = useSelector(selectData);
  const status = useSelector(selectStatus);
  const dispatch = useDispatch();

  useEffect(() => {
    console.log("status: ", status);
    if (status === 'idel'){
        dispatch(getData());
    }
    console.log("data", data);
  }, [data, status, dispatch]);

  return (
    <div>
      {console.log(data)}
      "running"
    </div>
  );
}
