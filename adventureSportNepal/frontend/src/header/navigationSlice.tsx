import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { NavigationItemType } from './types';

export const getNavigationList = createAsyncThunk(
    'navigationList/getNavigationList', async () => {
        const options = {
            method: 'GET',
            headers: {
                'content-type': 'application/json',
                "Access-Control-Allow-Origin": "*",
                credentials: "same-origin"
            },

        };
        return await fetch('http://127.0.0.1:8000/navigation/show-nav', options)
            .then(res => {
                return res.json();
            })
            .then(data => data.expeditionList)
            .catch((err: Error) => console.log(err.message))

    })

interface SliceState {
    status: 'idel' | 'loading' | 'finished';
    expeditions?: NavigationItemType;
}


const initialState: SliceState = {
    status: 'idel'
};


export const slice = createSlice({
    name: 'navigationList',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(getNavigationList.pending, (state, _) => {
            state.status = 'loading'
        }),
            builder.addCase(getNavigationList.fulfilled, (state, action) => {
                state.status = 'finished';
                state.expeditions = action.payload;
            })
    }
});

export const selectStatus = (state: { navigationList: SliceState }) => state.navigationList.status;
export const selectExpeditionList = (state: { navigationList: SliceState }) => state.navigationList.expeditions

export default slice.reducer
