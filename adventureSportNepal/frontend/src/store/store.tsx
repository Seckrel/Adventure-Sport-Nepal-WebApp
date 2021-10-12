import { configureStore } from "@reduxjs/toolkit";
import NavigationListReducer from '../header/navigationSlice';
import SkiPackageReducer from '../pages/ski/skiSlice';
import TrekPackageReducer from '../pages/trek/trekSlice';

export const store = configureStore({
    reducer: {
        navigationList: NavigationListReducer,
        skiPackage: SkiPackageReducer,
        trekPackage: TrekPackageReducer,
    },
})

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;