tipoJogada = ["Quartzo", "Pergaminho", "Podadeira"]
Jogador1 = [] # vetor jogador 1
JogadorHumano = [] # vetor jogador humano
Jogador2 = [] # vetor jogador 2
JogadorPC=[] # vetor jogador pc
VencedoresA=[] # vetor de vencedores no modo jogador x jogador
VencedoresB=[] # vetor de vencedores no modo humano x pc
placar=[0,0,0,0] # vetor de pontos
decisao = 0 # variavel decisao dos jogadores
NumeroPartidaPC = 0 # numeros de partidas contra o pc
NumeroPartidaJogador = 0 # numero de partidas contra os jogadores
jogo = True # manter o jogo on
import random # importar random
import os # importar clear
clear = lambda:os.system('cls')
def escolherJogada(numero,vetorS): # o jogador 1 e jogador 2 irao escolher um numero
    for contador in range(1,4,1):
        if numero == contador:
            escolhaJ = vetorS[contador-1]
            return escolhaJ
def AcharIndice(Partida,vectorJogador,vectorTipo):
    for contador in range(len(vectorTipo)):
        if vectorJogador[Partida] == vectorTipo[contador]:
            return contador
def compararJogada(partida,indiceJogador1,indiceJogador2,vetorTipoJogada): # compara os indices dos vetores escolhidos pelo jogador 1 e 2 
    if indiceJogador1 != indiceJogador2 and indiceJogador1+indiceJogador2==1: # a soma destes indices determina em uma matriz o resultado do vencedor
        return vetorTipoJogada[1] # 1 para pergaminho
    elif indiceJogador1 != indiceJogador2 and indiceJogador1+indiceJogador2==2:
        return vetorTipoJogada[0] # 2 para quartizo
    elif indiceJogador1 != indiceJogador2 and indiceJogador1+indiceJogador2==3:
        return vetorTipoJogada[2] # 3 para podadeira
    else: # caso os valores dos indices sejam iguais havera empate.
        return vetorTipoJogada[indiceJogador1]
def DefinirVencedor(partida,tipoString,vetorJogador1,vetorJogador2,md): # Modulo de verificacao do vencedor
    vencedorPartida = "" # String que retornara com o nome do vencedor
    if vetorJogador1[partida] == tipoString and vetorJogador2[partida]==tipoString: # verificacao de empate
        vencedorPartida = "Empate"
        return vencedorPartida
    elif vetorJogador1[partida] == tipoString and vetorJogador2[partida]!=tipoString: # verificacao se o jogador 1 ganhou
        vencedorPartida = "Jogador 1"
        return vencedorPartida
    else: # verificacao se o jogador 2 ganhou
        if md==1: # se o modo de jogo for humano x humano
            vencedorPartida = "Jogador 2"
            return vencedorPartida
        else: # se o modo de jogo for humano x pc
            vencedorPartida = "Jogador PC"
            return vencedorPartida
def escolherModoDeJogo(Numero): # entrando com um numero natural para escolher humanoxhumano ou humanoxPC
    while(Numero!=1 and Numero !=2):
        if Numero ==1: # para modo de jogo Humano x Humano
            return 1
        if Numero ==2: # para modo de jogo Humano x PC
            return 2
def GerarJogada(): # Gerador de Jogada Computador
    numero = random.randrange(1,4,1) # Gera um numero Random para o pc
    return numero # Retorna este numero
def MenuEscolhaJogador(jogador):
    numero = 0
    while(numero!=1 and numero !=2 and numero!=3): # escolha do jogador
        print("Vez de Jogador  " + jogador)
        print("Digite:")
        print("1 - Quartzo")
        print("2 - Pergaminho")
        print("3 - Podadeira")
        numero = int(input())
        clear()
    return numero
def IncluirNoVetor(valor,vetorJogador,vetorTipo): # modulo para incluir valores nos vetores desejados
    vetorJogador.append(escolherJogada(valor,vetorTipo))
def Vencer(PartidaNumero,vetorJogador1,vetorJogador2,vetorTipo,Md): # modulo para registrar os vencendores
 tipoGanhador = compararJogada(PartidaNumero,AcharIndice(PartidaNumero,vetorJogador1,vetorTipo),AcharIndice(PartidaNumero,vetorJogador2,vetorTipo),vetorTipo)
 if Md==1: # se modo for de humano x humano
     VencedoresA.append(DefinirVencedor(PartidaNumero,tipoGanhador,vetorJogador1,vetorJogador2,Md))
 if Md==2: # se o modo for de humano x PC
     VencedoresB.append(DefinirVencedor(PartidaNumero,tipoGanhador,vetorJogador1,vetorJogador2,Md))
def SairJogo(valor): # modulo para alterar o modo de jogo
        print("")
        print("")
        print("Pressione Enter para jogar novamente")
        print("Sair do Jogo - Pressione 1")
        sair=input()
        if sair=="1": # altera o modo jogo
            return 0
        else: # mantem o modo de jogo
            return valor
def Pontuar(vence,plac,Md,numeroP): # pontuar os jogadores
        if vence[numeroP]== "Jogador 1" and Md==1: # jogador 1
            plac[0]+=2
        if vence[numeroP]== "Jogador 2" and Md==1: # jogador 2
            plac[1]+=2
        elif vence[numeroP]=="Jogador 1" and Md ==2: # jogador humano
            plac[2]+=2
        elif vence[numeroP] =="Jogador PC" and Md ==2: # jogador PC
            plac[3]+=2
        elif vence[numeroP] =="Empate" and Md ==1: # Jogador 1 e 2
            plac[0]+=1
            plac[1]+=1
        elif vence[numeroP]=="Empate" and Md==2: # Jogador Humano e Pc
            plac[2]+=1
            plac[3]+=1
while(jogo): # inicializacao do jogo
    print("Quartzo, Pergaminho e Podadeira")
    print("Escolha o modo de jogo")
    print("")
    print("1 - Jogador X Jogador")
    print("2 - Jogador X PC")
    print("3 - Historico de jogos" )
    modo = int(input()) # variavel para modo de jogo
    clear()
    while modo ==1: # modo humano x humano
        for contador in range(1,3,1): # escolher a opcaos dos jogadores 1 e 2
            decisao =MenuEscolhaJogador(str(contador))
            if contador == 1:
                IncluirNoVetor(decisao,Jogador1,tipoJogada)
            elif contador == 2:
                IncluirNoVetor(decisao,Jogador2,tipoJogada)
        Vencer(NumeroPartidaJogador,Jogador1,Jogador2,tipoJogada,modo) # determinar vencedor
        print("Jogador 1:" + Jogador1[NumeroPartidaJogador]+"   X  "+"Jogador 2:" + Jogador2[NumeroPartidaJogador])
        print("Ganhador:" + VencedoresA[NumeroPartidaJogador])
        modo = SairJogo(modo) # perguntar se gostaria de jogar novamente
        Pontuar(VencedoresA,placar,modo,NumeroPartidaJogador)
        NumeroPartidaJogador+=1 # somar valor de partidas
        clear() # limpar tela
    while modo ==2:
        decisao = MenuEscolhaJogador("1") # escolher opcao de jogador humano
        IncluirNoVetor(decisao,JogadorHumano,tipoJogada) # incluir opcao no vetor
        decisao =GerarJogada() # gerar a jogada do jogador PC
        IncluirNoVetor(decisao,JogadorPC,tipoJogada) # incluir no vetor PC
        Vencer(NumeroPartidaPC,JogadorHumano,JogadorPC,tipoJogada,modo) # Determinar Vencedor
        print("Jogador 1:" + JogadorHumano[NumeroPartidaPC]+"   X  "+"Jogador PC:" + JogadorPC[NumeroPartidaPC])
        print("Ganhador:" + VencedoresB[NumeroPartidaPC])
        modo = SairJogo(modo) # Perguntar se gostaria de jogar novamente
        Pontuar(VencedoresB,placar,modo,NumeroPartidaPC)
        NumeroPartidaPC+=1 # Somar valores de partida
        clear() # limpar tela
    while modo==3:
        print("JOGADOR X JOGADOR")
        print("-------")
        print("Jogador1:",placar[0],"pontos","Jogador2:",placar[1],"pontos")
        print("-------")
        if NumeroPartidaJogador != 0:
            for contador in range(len(VencedoresA)):
                print("Partida ",contador,"|Ganhador : " + VencedoresA[contador])
                print("Jogador 1:" + Jogador1[contador]+"   X  "+"Jogador 2:" + Jogador2[contador])  
                print("") 
        else:
            print("JOGADOR X PC")
            print("-------")
            print("Jogador:",placar[2],"pontos","PC:",placar[3],"pontos")
            print("-------")
            if NumeroPartidaPC != 0:
                for contador in range(len(VencedoresB)):
                    print("Partida ", contador,"|Ganhador:" + VencedoresB[contador])
                    print("Jogador:" + JogadorHumano[contador]+"   X  "+"Jogador 2:" + JogadorPC[contador])
                    print("") 
            else:
                print("-------")
        cont = input("Pressione Enter para continuar")
        modo=0
        clear()
