import "core-js/stable";
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { store } from './store/store';
import App from './App';

try {
    ReactDOM.render(
        <Provider store={store}>
            <React.StrictMode>
                <App />
            </React.StrictMode>,
        </Provider>,
        document.getElementById('root'))
} catch (e) {
    console.log(e.message)
}