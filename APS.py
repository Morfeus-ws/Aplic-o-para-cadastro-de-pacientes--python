import os
import json
import collections

os.system("cls")

clientes = {'nome_completo' : [],'cod' : [],'nome_pai' : [],'nome_mae' : [],'idade' : [],'sexo' : [],'est_civil' : [],'rg' : [],'cpf' : [],'email' : [],'profissao' : [],'telefone' : [],'endereco' : [],'cidade' : [],'cep' : [],'tipo_sangue' : []}
op = "sim"
op3 = 0
x = 0
c = 0

#pegar o indice do nome e deletar
def getIndexandDel(p):
    clientes['nome_completo'].sort()
    print(clientes['nome_completo'])
    print("_"*50)
    consultar = input("Informe o nome do cliente: ")
    consultarV = consultar in clientes['nome_completo']
    if consultarV == True:
        pos = clientes['nome_completo'].index(consultar)
        clientes['cod'].pop(pos)
        clientes['nome_completo'].pop(pos)
        clientes['nome_pai'].pop(pos)
        clientes['nome_mae'].pop(pos)
        clientes['idade'].pop(pos)
        clientes['sexo'].pop(pos)
        clientes['est_civil'].pop(pos)
        clientes['rg'].pop(pos)
        clientes['email'].pop(pos)
        clientes['profissao'].pop(pos)
        clientes['telefone'].pop(pos)
        clientes['endereco'].pop(pos)
        clientes['cidade'].pop(pos)
        clientes['cep'].pop(pos)
        clientes['tipo_sangue'].pop(pos)
        p = p - 1
        
        print("Removido com sucesso")
        print(clientes)
    else:
        print("Codigo invalido!!!")

#cadastrar o usuario       
def cadUsuario():
    clientes['cod'].append(c)
    clientes['nome_completo'].append(input("Insira o nome completo: "))
    clientes['nome_pai'].append(input("Insira o nome do pai: "))
    clientes['nome_mae'].append(input("Insira o nome da mae: "))
    clientes['idade'].append(input("Insira a idade: "))
    clientes['sexo'].append(input("Insira o sexo: "))
    clientes['est_civil'].append(input("Insira o estado civil: "))
    clientes['rg'].append(input("Insira o rg: "))
    clientes['email'].append(input("Insira o email: "))
    clientes['profissao'].append(input("Insira a profissao: "))
    clientes['telefone'].append(input("Insira o telefone: "))
    clientes['endereco'].append(input("Insira o endereco: "))
    clientes['cidade'].append(input("Insira a cidade: "))
    clientes['cep'].append(input("Insira o cep: "))
    clientes['tipo_sangue'].append(input("Insira o tipo sanguineo: "))


while op == "sim" or op == "s" or op == "Sim":
    os.system("cls")
    cadUsuario()
    x += 1
    c += 1
    print("_"*50)
    op = str(input("Deseja inserir um novo cadastro ? sim - nao : "))
    print("_"*50)

else:
    if (op != "nao" and op != "sim"):
        os.system("cls")
        print("Comando invalido ! Insira o valor de acordo.")
        print("_"*50)
        op = str(input("Deseja inserir um novo cadastro ? sim - nao : "))
        print("_"*50)
    else:
        while op3 == 0:
            os.system("cls")
            op2 = int(input(" Oque deseja fazer agora?\n 1 - Exibir os nomes em ordem Alfabética.\n 2 - Exibir todos os cadastros.\n 3 - Excluir um cadastro pelo nome.\n 4 - SAIR \n INSIRA O NUMERO QUE DESEJA: "))
            print("_"*50)
            print(" ")

            if(op2 == 1):
                os.system("cls")
                clientes['nome_completo'].sort()
                print(clientes['nome_completo'])
                print("_"*50)
                op3 = 0

            elif(op2 == 2):
                os.system("cls")   
                listaCod = clientes['cod']
                listaNomecompleto = clientes['nome_completo']
                listaPai = clientes['nome_pai']
                listaMae = clientes['nome_mae']
                listaIdade = clientes['idade']
                listaSexo = clientes['sexo']
                listaEstCivil = clientes['est_civil']
                listaRG = clientes['rg']
                listaEmail = clientes['email']
                listaProfissao = clientes['profissao']
                listaTell = clientes['telefone']
                lisitaCidade = clientes['cidade']
                listaEndereço = clientes['endereco']
                listaCEP =clientes['cep']
                listaTP = clientes['tipo_sangue']
                
                for i in range(0, x):
                    print("_"*30)
                    print(f"Cod: {listaCod[i]} Nome: {listaNomecompleto[i]}\nIdade: {listaIdade[i]}\nNome Pai :{listaPai[i]}\nNome Mâe: {listaMae[i]}\nSexo: {listaSexo[i]}\nEstado Civil: {listaEstCivil[i]}\nRG: {listaRG[i]}\nEmail: {listaEmail[i]}\nProfissão: {listaProfissao[i]}\nTelefone: {listaTell[i]}\nCidade: {lisitaCidade[i]}\nEndereço: {listaEndereço[i]}\nCEP: {listaCEP[i]}\nTipo do Sangue: {listaTP[i]}")
                    print("_"*30)                     
                op3 = 0
                    
            elif(op2 == 3):  
                os.system("cls")
                getIndexandDel(x)  

            elif(op2 == 4):
                os.system("cls")
                sair = str(input("Tem certeza que deseja sair ? sim - nao:   "))
                if( sair == "sim"):
                    print("Até Mais !")
                   

                    f = open("jsonAps.json","w")
                    json.dump(clientes,f, sort_keys=True,indent=4)
                    f.close()
                    break
                else: 
                    op3 = 0




                