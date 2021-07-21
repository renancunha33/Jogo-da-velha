i=0
tabuleiro = ['1','2','3','4','5','6','7','8','9']
print("BEM VINDO AO JOGO DA VELHA\n")

def printTab():
    print(tabuleiro[0]+'|'+tabuleiro[1]+'|'+tabuleiro[2]+'\n'+
    "------\n"+
    tabuleiro[3]+'|'+tabuleiro[4]+'|'+tabuleiro[5]+'\n'+
    "------\n"+
    tabuleiro[6]+'|'+tabuleiro[7]+'|'+tabuleiro[8]+'\n')

printTab()

while i < 9:

      if i % 2 == 0:
          jog1 = input('Digite a posição da sua jogada jogador 1:\n')
          jogada = 'X'
          if tabuleiro[int(jog1) - 1] != 'X' and tabuleiro[int(jog1) - 1] != 'O':
              tabuleiro[int(jog1) - 1] = jogada
          else:
              print('POSIÇÃO OCUPADA')
              i = i - 1
      else:
          jog2 = input('Digite a posição da sua jogada jogador 2:\n')
          jogada = 'O'
          if tabuleiro[int(jog2) - 1] != 'X' and tabuleiro[int(jog1) - 1] != 'O':
              tabuleiro[int(jog2) - 1] = jogada
          else:
              print('POSIÇÃO OCUPADA')
              i = i - 1

      printTab()
      if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]or tabuleiro[3] == tabuleiro[4] == tabuleiro[5]or tabuleiro[6] == tabuleiro[7] == tabuleiro[8]or tabuleiro[0] == tabuleiro[3] == tabuleiro[6]or tabuleiro[1] == tabuleiro[4] == tabuleiro[7]or tabuleiro[2] == tabuleiro[5] == tabuleiro[8]or tabuleiro[0] == tabuleiro[4] == tabuleiro[8]or tabuleiro[6] == tabuleiro[4] == tabuleiro[2]:
        print('VITORIA DO JOGADOR '+ str((i % 2)+1)+'!!!')
        break
      elif i==8:
        print('EMPATE !!!')
        break
      i = i + 1

