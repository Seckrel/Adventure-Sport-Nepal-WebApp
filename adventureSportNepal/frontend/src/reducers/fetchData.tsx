import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";


export const fetchData = createAsyncThunk('data/fetch', async () => {
    console.log("working")
    const res = await fetch("https://randomuser.me/api/");
    console.log(res.json())
    return res
})


const initialValue: any = {
    value: [],
    status: 'idel'
}

export const slice = createSlice({
    name: 'data',
    initialState: initialValue,
    reducers: {},
    extraReducers: {
        [fetchData.pending.toString()]: state => state.status = 'pending',
        [fetchData.fulfilled.toString()]: (state, action) => state.value =action.payload,
    }
});

export const selectData = (state: any) => state.value;
export const status = (state: any) => state.status;

export default slice.reducer;