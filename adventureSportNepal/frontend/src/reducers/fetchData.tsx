import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const getData = createAsyncThunk(
    'data/getData', async () => {
        return fetch("https://randomuser.me/api/")
            .then(res => res.json())
            .then(data => data.results)
    }
)

export const slice = createSlice({
    name: 'data',
    initialState: {
        value: [],
        status: 'idel'
    },
    reducers: {},
    extraReducers: {
        [getData.pending.toString()]: (state, _) => {
            state.status = "loading";
        },
        [getData.fulfilled.toString()]: (state, action) => {
            state.value = action.payload;
        }
    }
});


export const selectData = (state: any) => state.counter.value;
export const selectStatus = (state: any) => state.counter.status;

export default slice.reducer;


