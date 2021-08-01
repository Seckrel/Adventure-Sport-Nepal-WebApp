import { useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { fetchData, selectData, status } from "./reducers/fetchData";

export default () => {
    const data = useSelector(selectData);
    const fetchStatus = useSelector(status);
    const dispatch = useDispatch();
    useEffect(() => {
        console.log(fetchStatus);
        if (fetchStatus === 'idel') {
            dispatch(fetchData);
        } else {
            console.log("data");
            console.log(data)
        }
    }, [fetchStatus, dispatch])
    return (
        <div>
            {console.log(data)}
            running
        </div>
    );
}