import { configureStore } from "@reduxjs/toolkit";
import counterReducer from '../reducers/fetchData';
import NavigationListReducer from '../header/navigationSlice';

export const store = configureStore({
    reducer: {
        counter: counterReducer,
        navigationList: NavigationListReducer
    },
})

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;