import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

export const getFaqPackages = createAsyncThunk(
    'faqPackages/getFaqPackages', async () => {
        const options = {
            method: 'GET',
            headers: {
                'content-type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                credentials: 'same-origin'
            },
        };
        return await fetch(`http://127.0.0.1:8000/faq-api/show-all/`, options)
            .then(res => res.json())
            .then(data => data.faqPackages)
            .catch((err: Error) => console.log(err.message))
    }
);

interface SliceState {
    status: 'idel' | 'loading' | 'finished';
    packages?: any;
};

const initialState: SliceState = {
    status: 'idel'
};

export const slice = createSlice({
    name: 'faqPackages',
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(getFaqPackages.pending, (state, _) => {
            state.status = 'loading'
        }),
            builder.addCase(getFaqPackages.fulfilled, (state, action) => {
                state.status = 'finished';
                state.packages = action.payload;
            })
    }
});

export const selectStatus = (state: { faqPackages: SliceState }) => state.faqPackages.status;
export const selectFaqPackages = (state: { faqPackages: SliceState }) => state.faqPackages.packages;

export default slice.reducer