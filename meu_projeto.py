'''
Projeto Final - Ad Verbum 
2025.06.30
Ana Vitória Schactae Brandão
'''

# Objetivo: Desenvolver um programa onde o usuário deve adivinhar uma palavra que contém 4 letras, baseado nas dicas que serão fornecidas pelas cores de cada letra a partir das tentativas
#BIBLIOTECAS --> Espaço reservado para a declaração de bibliotecas
from random import choice # Importa a função choice da biblioteca random
from termcolor import colored # Importa a função colored da biblioteca termcolor
from time import sleep #Importa a função sleep da biblioteca time
from palavras4l import palavrasSort # Importa a lista palavrasSort da biblioteca palavras4l
from cabeçalho import drawLine, msgCenter, msgLeft, mostraCabecalho, mostraInst, getValue, playAgain 

# VARIÁVEIS --> Espaço reservado para a declaração de variáveis
resposta = ''    # Variável que guarda a resposta do jogador
palavra = ''     # Variável que guarda a palavra sorteada
tentativas = 6   # Variável que guarda o número de tentativas do jogador

# LISTAS--> Espaço reservado para declaração de listas

MSGS = []
# Lista que guarda msgs do cabeçalho
msgsCab = ['AD VERBUM!',
           ' Desenvolvido por Ana Vitória Schactae Brandão'] 
 
# Lista que guarda msgs de instruções
msgsInst = ['DESCUBRA A PALAVRA SECRETA!', 
             'Depois de cada tentativa, as cores indicam quão perto você está da solução:', 
             'VERDE - A letra faz parte da palavra e está na posição correta', 
             'AMARELO - A letra faz parte da palavra mas em outra posição',
             'VERMELHO - A letra não faz parte da palavra'] 
# Lista que armazena as letras da resposta do usuário já analisadas
usadas = []
# Lista que armazena as letras analisadas ordenadas e na cor correspondente
resultado_final = []

# FUNÇÕES --> Espaço reservado para a declaração das funções

# Função que sorteia uma palavra dentro da lista de palavras importada
# # Função para Sortear um Número
def sortPal(palavrasSort): # 
    return choice(palavrasSort)    # Usa a Função choice para sortear uma palavra 

# Função Principal do Jogo
def playGame():
    global resposta, palavra, MSGS # modifica uma variável fora da função
    mostraCabecalho(msgsCab)    # Mostra o Cabeçalho do Jogo
    sleep(1) # Pausa de 1 segundo para evitar uma poluição de mensagens
    mostraInst(msgsInst)       # Mostra as Instruções do jogo

    # Chama função que sorteia uma palavra
    palavra = sortPal(palavrasSort).upper()

# Loop principal do jogo
    for i in range(tentativas): # Loop para repetir enquanto houverem tentativas
    # Ler uma tentativa de 4 letras do usuário
        while True: # Loop infinito, até que seja interrompido manualmente no código
            resposta = input("Digite uma palavra de 4 letras: ").upper() # Solicita uma palavra de 4 letras e transforma a resposta em letras maiúsculas para facilitar a análise
            if len(resposta) == 4 and resposta.isalpha(): # Se o comprimento da tentativa do usuário tiver 4 letras e não conter símbolos
                break # Interrompe o loop
            print("Palavra inválida! Digite novamente.") # Solicita novamente uma entrada com 4 letras e que não contenha símbolos
        
        resultado = '' # Variável que armazena a palavra colorida 
        usadas = list(palavra) # Cria uma lista com as letras já analisadas

        # Análise da entrada do usuário, onde:
        # VERDE --> Letra e posição corretas.
        # AMARELO --> Letra correta, posição incorreta.
        # VERMELHO --> Letra e posição incorretas.

        for i in range(4): # Laço para repetir entre as 4 letras da palavra
            if resposta[i] == palavra[i]: # Se a posição da letra na tentativa do usuário for a mesma contida na palavra
                resultado += colored(resposta[i], 'white', 'on_green') + " " # Acrescentará no resultado a letra colorida de verde
                usadas[i] = None # Evita a repetição de uma mesma letra já analisada.
            else: 
                resultado += "_ " # Placeholder para a segunda passada

        resultado_final = resultado.split() # Armazena em uma lista o resultado final

        for i in range(4): # Laço para repetir entre as 4 letras da palavra
            if resposta[i] == palavra[i]: # Se a posição da letra na resposta do usuário for igual a posição da palavra original
                continue # Pula essa repetição se a condição for verdadeira
            if resposta[i] in usadas: # Se a posição da palavra tentada pelo jogador for diferente na palavra sorteada mas a letra existir na palavra:
                    resultado_final[i] = colored(resposta[i], 'white', 'on_yellow') # Acrescentará no resultado a letra colorida de amarelo
                    usadas[usadas.index(resposta[i])] = None # Verifica se a letra já foi analisada, também evitando que seja assinalada como correta novamente.
            else: 
                    resultado_final[i] = colored(resposta[i], 'white', 'on_red') # Acrescentará no resultado a letra colorida de vermelho

        print("Resultado:", ' '.join(resultado_final)) # Mostra o resultado da tentativa do jogador, com o separador sendo um espaço em branco.

        if resposta == palavra: # Se a tentativa do usuário corresponder a palavra sorteada.
            mostraCabecalho(["Ad Verbum! "]) # Mostrará a mensagem.
            break # E encerrará o looping
    else: # Se o jogador não acertar a palavra secreta.
        mostraCabecalho([f" Game Over! A palavra era {palavra}"]) # Então mostrar a mensagem final seguida da palavra secreta.
while True: #Laço para repetir infinitamente, até que seja interrompido
    playGame() # Função que inicia o jogo
    if not playAgain(): # Se o jogador não jogar novamente
         mostraCabecalho(["Obrigada por jogar!"]) # Mostra a mensagem dentro do padrão 
         break # E interrompe o loop
