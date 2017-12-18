import React from 'react';
import ReactDOM from 'react-dom';
import './static/css/index.css';
import App from './static/JS/App';
import registerServiceWorker from './static/JS/registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
