import "core-js/stable";
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { store } from './store/store';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import path from 'path';

declare global {
    interface Window {
        PUBLIC:string;
    }
}

window.PUBLIC = path.resolve(__dirname, '../static');

try {
    ReactDOM.render(
        <BrowserRouter>
            <Provider store={store}>
                <React.StrictMode>
                    <App />
                </React.StrictMode>,
            </Provider>
        </BrowserRouter>,
        document.getElementById('root'))
} catch (e) {
    console.log(e.message)
}