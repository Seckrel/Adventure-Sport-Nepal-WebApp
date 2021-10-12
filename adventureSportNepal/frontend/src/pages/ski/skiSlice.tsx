import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { IParams } from "./types.d";

export const getSkiPackage = createAsyncThunk(
    'skiPackage/getSkiPackage', async (id: string | undefined) => {
        const options = {
            method: 'GET',
            headers: {
                'content-type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                credentials: 'same-origin'
            },
        };
        return await fetch(`http://127.0.0.1:8000/ski/${id}`, options)
            .then(res => res.json())
            .then(data => data.skiPackage)
            .catch((err: Error) => console.log(err.message))
    }
);

interface SliceState {
    status: 'idel' | 'loading' | 'finished';
    package?: any;
};

const initialState: SliceState = {
    status: 'idel'
};

export const slice = createSlice({
    name: 'skiPackage',
    initialState,
    reducers: {
        resetStatus: (state: SliceState) => { state.status = 'idel' }
    },
    extraReducers: (builder) => {
        builder.addCase(getSkiPackage.pending, (state, _) => {
            state.status = 'loading'
        }),
            builder.addCase(getSkiPackage.fulfilled, (state, action) => {
                state.status = 'finished';
                state.package = action.payload;
            })
    }
});

export const { resetStatus } = slice.actions;
export const selectStatus = (state: { skiPackage: SliceState }) => state.skiPackage.status;
export const selectSkiPackage = (state: { skiPackage: SliceState }) => state.skiPackage.package;

export default slice.reducer