

$(function(){

    var casa_selecionada = null;
    var peca_selecionada = null;

    function MontarTabuleiro(){
        var i;
        for (i=0; i<8; i++){
            $("#tabuleiro").append("<div id='linha_"+i.toString()+"' class='linha' >");
            if(i < 7) {
                $("#tabuleiro").append("<div class='linhaSeparadora'>");
                // $("#tabuleiro").append("<div class='colunaSeparadora'>");
            }
            for (j=0; j<8; j++){
                
                var nome_casa ="casa_"+i.toString()+"_"+j.toString();
                var classe = (i%2==0?(j%2==0?"casa_branca":"casa_preta"):(j%2!=0?"casa_branca":"casa_preta"));
                $("#linha_"+i.toString()).append("<div id='"+nome_casa+"' class='casa "+classe+"' />");
                
                if(classe == "casa_preta"){
                    if(i < 3){
                        $("#"+nome_casa).append("<img src='peca_preta.png' class='peca' id='"+nome_casa.replace("casa", "peca_preta")+"'/>");
                    }
                    else
                    if(i > 4){
                        $("#"+nome_casa).append("<img src='peca_branca.png' class='peca' id='"+nome_casa.replace("casa", "peca_branca")+"'/>");   
                    }
    
                }
            }
        }
    }

    MontarTabuleiro();
});

$(".casa").click(function(){
    $("#"+casa_selecionada).removeClass("casa_selecionada");
    casa_selecionada = $(this).attr("id");
    $("#"+casa_selecionada).addClass("casa_selecionada");
    $("#info_casa_selecionada").text(casa_selecionada);
 
    peca_selecionada = $("#"+casa_selecionada).children("img:first").attr("id");
    if(peca_selecionada==null){
        peca_selecionada = "NENHUMA PECA SELECIONADA";
    }
    $("#info_peca_selecionada").text(peca_selecionada.toString());
});