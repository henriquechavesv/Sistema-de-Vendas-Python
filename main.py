
def cadastrar_produto(nome, preco, quantidade):             
    return {
        "nome": nome,
        "preco": float(preco),
        "quantidade": int(quantidade),
        "total": float(preco) * int(quantidade)
    }

def calcular_total(carrinho):                               
    return sum(item["total"] for item in carrinho)          

def aplicar_desconto(valor, taxa=0.1):                      
    return valor * (1 - taxa)                               

def mostrar_carrinho(carrinho):                             
    print("--- Carrinho ---")                               
    for item in carrinho:                                   
        print(f"{item['nome']} - R$ {item['preco']:.2f} x {item['quantidade']} = R$ {item['total']:.2f}")
    print("----------------")                                 

    total = calcular_total(carrinho)                        
    print(f"Total sem desconto: R$ {total:.2f}")            
    return total                                            

def finalizar_compra(carrinho, taxa=0.1):                   
    total = calcular_total(carrinho)                        
    valor_final = aplicar_desconto(total, taxa)             
    return valor_final                                      

# --------- Fluxo principal ---------                       

carrinho = []                                           

qtde_produtos = int(input("Quantos produtos voce ira comprar? "))  

for i in range(qtde_produtos):                          
    nome = input(f"Nome do Produto {i+1}: ")             
    preco = float(input(f"Preço do Produto {i+1}: "))    
    quantidade = int(input(f"Quantidade do Produto {i+1}: ")) 
    carrinho.append(cadastrar_produto(nome, preco, quantidade))

total_sem = mostrar_carrinho(carrinho)                  
total_com = finalizar_compra(carrinho, taxa=0.10)        
print(f"Total com desconto: R$ {total_com:.2f}")         
