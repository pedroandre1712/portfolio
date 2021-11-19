def escolha():
  global tipo_char
  
  print('Você estava em um laboratorio de física e',
        ' decidiu apertar um botao vermelho escrito NAO APERTE. ')
  
  print('Agora você voltou para o ano de 1914,',
        ' o inicio da primeira guerra mundial!')
  
  print('\nVocê deverá representar um país nessa guerra.')

  tipo_char = input('\nCom qual país você deseja jogar\n1 - Alemanha\n2 - França\n3 - Estados Unidos\n')
  print('_'*100)

  if tipo_char == '1':
    print('\nExcelente escolha!')
    print('A Alemanha possui um imenso poder bélico,',
          ' entretanto pode ser atacada por diferentes frentes.')

  elif tipo_char == '2':
    print('\nÓtima escolha!')
    print('A França está em uma posição estratégica para a guerra!',
          'Entretanto, você correrá o risco de ter guerras em seu território.')

  elif tipo_char == '3':
    print('\nMuito boa a escolha!' )
    print('Os Estados Unidos possuem um forte poder bélico e',
          ' não se envolvem diretamente na guerra!',
          'Entretanto, se os seus aliados perderem a Guerra,',
          ' a economia do seu pais estará em risco.')


def guerra_alemanha():
  print('\nA guerra começou!')
  escolha_um = input('\nVocê deseja:\n 1 - Invadir a França na frente Ocidental\n 2 - Combater a Russia na frente Oriental\n')
  print('_'*100)
  if escolha_um == '1':
    print('\nÓtima decisao! O império Russo não está bem estruturado, então pequena parte da suas tropas devem solucionar o problema na fronteira oriental.')
    escolha_dois = input('\nVoce deseja invadir a França pelo:\n 1 - Norte\n 2 - Oeste\n')
    print('_'*100)
    if escolha_dois == '1':
      print('\nParabéns, voce pegou os franceses de surpresa!')
      print('\nEntretanto, a Inglaterra chegou para ajudar a França!')
      print('A Inglaterra cercou o litoral Alemao.')
      print('\nE agora??')
      escolha_tres = input('\nVocê quer:\n1 - Recuar suas tropas\n2 - Solicitar reforço marítimo\n')
      print('_'*100)
      if escolha_tres == '1':
        print('Você foi pego pelo navio ingles!\n\n GAME OVER!')
      elif escolha_tres == '2':
        print('A sua frota de submarinos chegou! Voce afundou 1/3 dos navios ingleses e eles decidiram recuar')
        print('\nParabéns! Você ganhou a Guerra!')
    elif escolha_dois =='2':
      print('Os franceses estavam com suas tropas preparadas!\n\n GAME OVER!')
  elif escolha_um =='2':
    print('\nParabéns! Voce dizimou o exército Russo')
    print('Entretanto, a França derrotou o seu exército na fronteira Ocidental!')
    print('\nGAME OVER!')

def guerra_franca():
  print('\nA guerra começou!')
  escolha_um = input('Você deseja:\n 1 - Fortalecer suas fronteiras\n 2 - Invadir a Alemanha\n')
  print('_'*100)
  if escolha_um == '1':
    print('\nVocê fortaleceu suas fronteiras!')
    print('Agora você está preparado caso haja uma invasão no seu território')
    print('A Alemanha tentou um ataque supresa pelo Norte!')
    escolha_dois = input('Você deseja:\n 1 - Fortalecer suas tropas ao norte\n 2 - Manter sua formacao atual\n')
    print('_'*100)
    if escolha_dois == '1':
      print('\nParabéns, voce acabou com a ofensiva Alema!')
      print('Entretanto, o Império Austro-Húngaro realizou uma ofensiva na fronteira!')
      print('\nE agora??')
      escolha_tres = input('\nVocê deseja:\n1 - Solicitar ajuda inglesa\n2 - Solicitar ajuda americana\n')
      print('_'*100)
      if escolha_tres == '1':
        print('A forca inglesa esta ocupada lidando com os submarinos Alemães!\n\n GAME OVER!')
      elif escolha_tres == '2':
        print('Os Estados Unidos enviaram suas frotas para reforço! Juntos, vocês acabaram com a ofensiva austro-húngara')
        print('\nParabéns! Você ganhou a Guerra!')
    elif escolha_dois =='2':
      print('Os alemães venceram a batalha ao norte!\n\n GAME OVER!')
  elif escolha_um =='2':
    print('\nParabéns! Você conquistou uma pequena parte do território alemão\n')
    print('Entretanto, a Alemanha fez uma invasão surpresa pelo norte no território Francês!\n\n GAME OVER!')

def guerra_eua():
  print('\nA guerra começou')
  escolha_um = input('\nVocê deseja:\n 1 - Investir em armamentos e artigos industrializados\n 2 - Investir somente em armamentos\n')
  print('_'*100)
  if escolha_um == '1':
    print('\nInvestimento feito!\n')
    print('Agora você está preparado para fornecer seus produtos aos seus aliados')
    print('\nA Alemanha começou uma guerra submarina irrestrita!')
    escolha_dois = input('\nVocê deseja:\n 1 - Enviar imediatamente reforços ao Reino Unido\n 2 - Tentar um acordo de paz com a Alemanha\n')
    print('_'*100)
    if escolha_dois == '1':
      print('\nReforcos enviados!\n')
      print('Entretanto, a Franca foi invadida por uma ofensiva surpresa pelo Norte!')
      print('\nE agora??')
      escolha_tres = input('\nVocê deseja:\n1 - Manter todos os reforços as tropas do Reino Unido\n2 - Dividir os reforços com os franceses\n')
      print('_'*100)
      if escolha_tres == '1':
        print('\nOs alemães dominaram o territorio Frances!\n\n GAME OVER!')
      elif escolha_tres == '2':
        print('Os Estados Unidos enviaram parte de suas frotas para reforço na Franca! Juntos, vocês acabaram com a ofensiva Alemã')
        print('\nParabéns! Você ganhou a Guerra!')
    elif escolha_dois =='2':
      print('\nOs alemães derrubaram 1/3 das tropas submarinas inglesas e invadiram a França!\n\n GAME OVER!')
  elif escolha_um =='2':
    print('\nInvestimento feito!\n')
    print('Entretanto, os principais centros de producao de alimentos dos seus aliados foi destruido!\n\n GAME OVER!')

tipo_char = ''
def game():
  global tipo_char
  escolha()
  if tipo_char == '1':
    guerra_alemanha()
  elif tipo_char == '2':
    guerra_franca()
  elif tipo_char =='3':
    guerra_eua()

game()