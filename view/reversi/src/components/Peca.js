import React from 'react';
import './../index.css';

export default class Peca extends React.Component{
    render(){
        if(this.props.cor ==="P"){
            return(
                <div className="pecaPreta"></div>
            );
        }
        if(this.props.cor ==="B"){
            return(
                <div className="pecaBranca"></div>
            );
        }
        return(false);
    }
};