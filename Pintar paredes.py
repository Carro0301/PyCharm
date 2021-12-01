larg= float(input('Digite a largura da parede: '))
alt= float(input('Digite a altura da parede:  '))
Area= larg*alt
print("Sua parede tem a dimensão de {} x {} e sua área é de {} m².".format (larg, alt, Area))
tinta=Area/2
print('Para pintar sua parede, você precisará de {}, litros de timta'.format(tinta))
