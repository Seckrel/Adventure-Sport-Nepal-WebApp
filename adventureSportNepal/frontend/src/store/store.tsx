import { configureStore } from "@reduxjs/toolkit";
import NavigationListReducer from '../header/navigationSlice';
import SkiPackageReducer from '../pages/ski/skiSlice';
import TrekPackageReducer from '../pages/trek/trekSlice';

export const store = configureStore({
    reducer: {
<<<<<<< HEAD
        navigationList: NavigationListReducer
=======
        navigationList: NavigationListReducer,
        skiPackage: SkiPackageReducer,
        trekPackage: TrekPackageReducer,
>>>>>>> 3c2d9902d29b389b3eccda9acd29f886cf6bcad3
    },
})

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;