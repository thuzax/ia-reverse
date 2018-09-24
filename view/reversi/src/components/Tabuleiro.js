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
            pontosP: 2,
            pontosB: 2,
            pronto: true,
        };

        this.renderTabuleiro=this.renderTabuleiro.bind(this)
        // axios.get('http://localhost:5000/').then((response) => {
        //     console.log(response)
        // }, (err) => {
        //     console.log(err)
        // })
    }

    renderTabuleiro() {
        const {tabuleiro} = this.state;
        return(
            tabuleiro.map((linhas, indiceLinha) => (
                linhas.map((celula, indiceColuna) => (
                    <Celula 
                    key={""+indiceLinha+"-"+indiceColuna} 
                    id={""+indiceLinha+"-"+indiceColuna} 
                    status={tabuleiro[indiceLinha][indiceColuna]} 
                    handleClick={this.handleChildClick.bind(this)}
                    />        
                ))
            ))
        );
    }

    renderInformacoes() {
        const{pontosP, pontosB, pretoProx} = this.state
        var jogador = "Branco"
        if(pretoProx) {
            jogador = "Preto"
        }
        return(
            <div>
                Preto: {pontosP} <br></br>
                Branco: {pontosB} <br></br>
                Próximo: {jogador}
            </div>
        );
    }

    componentWillMount() {
        let novoTabuleiro = [];
        for(var i = 0; i < 8; i++){
            novoTabuleiro[i] = [];
            for(var j = 0; j < 8; j++){
                novoTabuleiro[i][j] = "-";
            }
        }
        //console.log(novoTabuleiro);
        novoTabuleiro[3][3] = "P";
        novoTabuleiro[4][4] = "P";
        novoTabuleiro[3][4] = "B";
        novoTabuleiro[4][3] = "B";
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
                "jogador": "${jogador}",
                "tabuleiro": "${this.state.tabuleiro}"
            }
        `);
        return objJSON;
    }

    atualizaTabela(dados){
        var novoTabuleiro = []
        for(var i = 0; i < dados.tamanho; i++) {
            novoTabuleiro[i] = [];
            for(var j = 0; j < dados.tamanho; j++) {
                novoTabuleiro[i][j] = dados.tabuleiro[i][j];
            }
        }
        this.setState({tabuleiro:  novoTabuleiro});
    }

    handleChildClick(id) {
        if(!this.state.pronto) {
           return;
        }
        this.setState({pronto: false});
        var posicoes = id.split("-")
        var obj = this.exportar(posicoes[0], posicoes[1], this.state.pretoProx)
        axios.post('http://localhost:5000/jogar', obj).then((response) => {
            console.log(response.data);
            this.atualizaTabela(response.data.jogador);
            if(response.data.jogador.jogadaFeita) {
                this.setState({pretoProx: !this.state.pretoProx});
            }
            this.setState({pontosB: response.data.jogador.pontuacao.B})
            this.setState({pontosP: response.data.jogador.pontuacao.P})
            var jogoFinalizado = false;
            if(this.state.pontosB + this.state.pontosP == 64) {
                var vencedor = (this.state.pontosB > this.state.pontosP) ? "Branco" : "Preto"
                jogoFinalizado = true;
                alert("Fim de jogo! O vencedor foi " + vencedor)
            } else {
                if(this.state.pontosB == 0) {
                    jogoFinalizado = true;
                    alert("Fim de jogo! O vencedor foi Preto")
                } else {
                    if(this.state.pontosP == 0) {
                        jogoFinalizado = true;
                        alert("Fim de jogo! O vencedor foi Branco")
                    }
                }
            }

            if(!jogoFinalizado) {
                setTimeout(() => {
                    this.atualizaTabela(response.data.ia);
                    if(response.data.ia.jogadaFeita) {
                        this.setState({pretoProx: !this.state.pretoProx});
                    }
                    this.setState({pontosB: response.data.ia.pontuacao.B})
                    this.setState({pontosP: response.data.ia.pontuacao.P})
                    if(this.state.pontosB + this.state.pontosP == 64) {
                        var vencedor = (this.state.pontosB > this.state.pontosP) ? "Branco" : "Preto"
                        alert("Fim de jogo! O vencedor foi " + vencedor)
                    } else {
                        if(this.state.pontosB == 0) {
                            alert("Fim de jogo! O vencedor foi Preto")
                        } else {
                            if(this.state.pontosP == 0) {
                                alert("Fim de jogo! O vencedor foi Branco")
                            }
                        }
                    }
                    this.setState({pronto: true});
                },800);
            } else {
                this.setState({pronto: true});
            }
            // console.log(this.state.tabuleiro);
        }, (err) => {
            console.log(err);
        });
        //console.log(this.state.tabuleiro);
    
    }
    render(){
        return(
            <div>
                <div className="tab">
                    {this.renderTabuleiro()}
                </div>
                <div className="info">
                    {this.renderInformacoes()}
                </div>
            </div>
        );
    }
}