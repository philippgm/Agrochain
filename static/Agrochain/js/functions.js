function exibir_ocultar(){
    var valor = $("#id_Categoria").val();
    
    if(valor == 1){
         $("#id_CNPJ").show();
   
     } else {
         $("#id_CNPJ").hide();
     } };

function Mudarestado(el) {
    if(el == 'q1'){
        document.getElementById('q2').style.display = 'none';
    }else{
        document.getElementById('q1').style.display = 'none';
    }
    document.getElementById(el).style.display = 'block';
}

function MyTypeTransactions(type){
if (type == 1){
    return produtor_transactions
}else {if (type == 2){
    return consumidor_transactions
}else {if (type == 3){
    return transportador_transactions
}else{
    return processador_transations
}}}
}
 