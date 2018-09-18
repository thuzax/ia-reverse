import React from 'react';
import './../index.css';

export default class Peca extends React.Component{
    render(){
        if(this.props.cor ==="PRETO"){
            return(
                <div className="pecaPreta"></div>
            );
        }
        if(this.props.cor ==="BRANCO"){
            return(
                <div className="pecaBranca"></div>
            );
        }
        return(false);
    }
};