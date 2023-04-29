distancia_total = 100 # km 
velocidade_carro = 110 # km/h 
velocidade_caminhao = 80 # km/h

tempo_encontro = distancia_total / (velocidade_carro + velocidade_caminhao) # horas 
distancia_carro_encontro = velocidade_carro * tempo_encontro # km

#Agora que sabemos a distância que o carro percorreu até o ponto de encontro, podemos calcular a distância que o caminhão percorreu:

distancia_caminhao_encontro = distancia_total - distancia_carro_encontro # km

#Como o caminhão passa por dois pedágios que atrasam sua viagem, precisa adicionar esse tempo extra ao tempo de viagem total do caminhão. Supondo que cada pedágio acrescenta 5 minutos à viagem do caminhão, podemos fazer o seguinte:

tempo_extra_pedagios = 0.0833 # horas (5 minutos em horas) 
tempo_total_caminhao = tempo_encontro + (tempo_extra_pedagios * 2) 
distancia_caminhao_rp = velocidade_caminhao * tempo_total_caminhao

#Finalmente, podemos comparar as distâncias do carro e do caminhão Ribeirão Preto para determinar qual veículo está mais próximo da cidade:

distancia_rp_carro = distancia_total - distancia_carro_encontro 
distancia_rp_caminhao = distancia_total - distancia_caminhao_rp

if distancia_rp_carro < distancia_rp_caminhao:
    print("O carro está mais próximo de Ribeirão Preto.") 
else: 
    print("O caminhão está mais próximo de Ribeirão Preto.")