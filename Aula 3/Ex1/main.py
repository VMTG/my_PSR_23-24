#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python


import time
import math
from colorama import Fore, Back, Style
from datetime import datetime

max_value = 50000000

def calcular_raiz_quadrada():
    for i in range (max_value):
        math.sqrt(i)

tempo_inicio = time.time()

calcular_raiz_quadrada()

tempo_fim = time.time()

data_atual = datetime.now()

tempo_decorrido = tempo_fim - tempo_inicio

print(str(data_atual))

print('Tempo decorrido: ' + Fore.RED + str(tempo_decorrido) + Fore.RESET + 'segundos')