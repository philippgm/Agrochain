
Relation = ((1,"Produtor"),(2,"Consumidor"),(3,"Transportador"),(4,"Processador"),)
Fields = ['CNPJ','company_name','organic_numb_certification']
type_transactions = [(1,"Anunciar"),(2,"Checkout"),(3,"Checkin"),(4,"Vender"),(5,"Comprar"),(6,"Consultar"),]
consumidor_transactions = [(1,"Anunciar"),]
produtor_transactions = ["Anunciar","Checkout","Checkin","Vender","Comprar","Consultar",]
processador_transations = [(1,"Anunciar"),(2,"Checkout"),(3,"Checkin"),(4,"Vender"),(5,"Comprar"),(6,"Consultar"),]
transportador_transactions = [(2,"Checkout"),(3,"Checkin"),(6,"Consultar"),]
tipos_pesquisas = ((1,"Tipo de Produto"),(2,"Agente"),(3,"Usuário"),(4,"Data de Anúncio"),)
def MyTypeTransactions(type:int)->str:
    print("asdasdasdasd")
    if type == 1:
        return produtor_transactions
    elif type == 2:
        return consumidor_transactions
    elif type == 3:
        return transportador_transactions
    else:
        return processador_transations
 