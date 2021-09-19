import { configureStore } from "@reduxjs/toolkit";
import NavigationListReducer from '../header/navigationSlice';

export const store = configureStore({
    reducer: {
        navigationList: NavigationListReducer
    },
})

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;