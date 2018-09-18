import React from 'react';
import './../index.css';
import axios from 'axios';

import Celula from './Celula.js';

export default class Tabuleiro extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            jogador: "P",
            pretoProx: true,
            tabuleiro: [],
        };

        
        // axios.get('http://localhost:5000/').then((response) => {
        //     console.log(response)
        // }, (err) => {
        //     console.log(err)
        // })
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


    exportar(posI, posJ, pretoProx){
        var jogador = "B";
        if(pretoProx)
            jogador = "P";

        // var objJSON = JSON.parse('{"posicaoI":' + posI + ', "posicaoJ":' + posJ + ', "jogador":' + jogador + '}');
        var objJSON = JSON.parse(`
            {
                "posicaoI": "${posI}",
                "posicaoJ": "${posJ}",
                "jogador": "${jogador}"
            }
        `)
        return objJSON;
    }

    handleChildClick(id, status) {
        if (id !== undefined) {
            var posicoes = id.split("-")
            var obj = this.exportar(posicoes[0], posicoes[1], this.state.pretoProx)
            axios.post('http://localhost:5000/jogar', {json: obj}).then((r) => {
                console.log(r);
            }, (err) => {
                console.log(err);
            });
        }
        this.setState({pretoProx: !this.state.pretoProx});
        return this.state.pretoProx;
    }
    render(){
        const {tabuleiro} = this.state
        return(
            <div className="tab">
                {tabuleiro.map((linhas, indiceLinha) => (
                    linhas.map((celula, indiceColuna) => (
                        <Celula id={""+indiceLinha+"-"+indiceColuna} status={tabuleiro[indiceLinha][indiceColuna]} handleClick={this.handleChildClick.bind(this)}/>        
                    ))
                ))}
            </div>
        );
    }
}