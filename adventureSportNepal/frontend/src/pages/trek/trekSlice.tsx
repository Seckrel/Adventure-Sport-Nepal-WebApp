import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { IParams } from "./types.d";

export const getTrekPackage = createAsyncThunk(
    'trekPackage/getTrekPackage', async (id: string | undefined) => {
        const options = {
            method: 'GET',
            headers: {
                'content-type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                credentials: 'same-origin'
            },
        };
        return await fetch(`http://127.0.0.1:8000/trek-api/${id}/`, options)
            .then(res => res.json())
            .then(data => data.trekPackage)
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
    name: 'trekPackage',
    initialState,
    reducers: {
        resetStatus: (state: SliceState) => { state.status = 'idel' }
    },
    extraReducers: (builder) => {
        builder.addCase(getTrekPackage.pending, (state, _) => {
            state.status = 'loading'
        }),
            builder.addCase(getTrekPackage.fulfilled, (state, action) => {
                state.status = 'finished';
                state.package = action.payload;
            })
    }
});

export const { resetStatus } = slice.actions;
export const selectStatus = (state: { trekPackage: SliceState }) => state.trekPackage.status;
export const selectTrekPackage = (state: { trekPackage: SliceState }) => state.trekPackage.package;

export default slice.reducer