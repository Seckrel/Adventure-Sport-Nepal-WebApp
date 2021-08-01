import { configureStore } from "@reduxjs/toolkit";
import fetchReducer from '../reducers/fetchData';

export const store = configureStore({
    reducer: {
        fetchData: fetchReducer
    },
})

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;