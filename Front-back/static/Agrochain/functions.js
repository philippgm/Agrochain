function exibir_ocultar(){
    var valor = $("#id_Categoria").val();
    
    if(valor == 1){
         $("#id_CNPJ").show();
    
     } else {
         $("#id_CNPJ").hide();
     } };