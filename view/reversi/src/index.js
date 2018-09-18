import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';

import Tabuleiro from './components/Tabuleiro.js';

ReactDOM.render(
    <div className="container">
        <div className="box">
            <h1 className = "titulo">Reversi</h1>
            <div className="tabuleiro"><Tabuleiro /></div>
        </div>
    </div>
    , 
    document.getElementById('root')
);
registerServiceWorker();
