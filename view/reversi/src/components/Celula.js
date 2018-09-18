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
    show(id, status){
        var resultado = this.props.handleClick(id, status);
        if(status === "-") {
            if(resultado) {
                this.setState({status: "P"});
            } else {
                this.setState({status: "B"});
            }
        }
    }
    render(){
        return(
            <button className='celula' onClick={this.show.bind(this, this.state.id, this.state.status)}>
            <Peca cor={this.state.status}/>
            </button>
        );
    }
};