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
 