import React from 'react';
import './../index.css';

import Peca from './Peca.js';

export default class Celula extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: this.props.id,
            status: this.props.status,
        }
    }
    show(id){
        this.props.handleClick(id);
        console.log(this.state.status);
    }
    render(){
        return(
            <button className='celula' onClick={this.show.bind(this, this.state.id)}>
            <Peca cor={this.state.status}/>
            </button>
        );
    }
};