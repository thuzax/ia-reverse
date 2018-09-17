import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';


class Peca extends React.Component{
    render(){
        if(this.props.id ==="PRETO"){
            return(
                <div className="pecaPreta"></div>
            );
        }
        if(this.props.id ==="BRANCO"){
            return(
                <div className="pecaBranca"></div>
            );
        }
        return(false);
    }
};

class Celula extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: this.props.id,
            status: this.props.status,
        }
    }
    show(id, status){
        alert(id + ' ' + status);
        this.props.handleClick(id, status);
        if(status === "VAZIO") {
            if(this.props.handleClick()) {
                this.setState({status: "PRETO"});
            } else {
                this.setState({status: "BRANCO"});
            }
        }
    }
    render(){
        return(
            <button className='celula' onClick={this.show.bind(this, this.state.id, this.state.status)}>
            <Peca id={this.state.status}/>
            </button>
        );
    }
};

class Tabuleiro extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            pretoProx: true,
            tabuleiro: [],


        };
    }

    componentWillMount() {
        let novoTabuleiro = [];
        for(var i = 0; i < 8; i++){
            novoTabuleiro[i] = [];
            for(var j = 0; j < 8; j++){
                novoTabuleiro[i][j] = "VAZIO";
            }
        }
        console.log(novoTabuleiro);
        novoTabuleiro[3][3] = "PRETO";
        novoTabuleiro[4][4] = "PRETO";
        novoTabuleiro[3][4] = "BRANCO";
        novoTabuleiro[4][3] = "BRANCO";
        this.setState({tabuleiro: novoTabuleiro});
    }

    handleChildClick(id, status) {
        this.setState({pretoProx: !this.state.pretoProx});
        if(this.state.status === "BRANCO"){
            this.setState({status: "PRETO"})
        } else {
            this.setState({status: "BRANCO"})
        }
        return this.state.pretoProx;
    }

    render(){
        const {tabuleiro} = this.state
        return(
            <div className="tab">
                {tabuleiro.map((linhas, indiceLinha) => (
                    linhas.map((celula, indiceColuna) => (
                        <Celula id={""+indiceLinha+indiceColuna} status={tabuleiro[indiceLinha][indiceColuna]} handleClick={this.handleChildClick.bind(this)}/>        
                    ))
                ))}
            </div>
        );
    }
}


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
