# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

def accesssite(msg):
    try:
        pudim = urllib.request.urlopen(msg)
    except:
        print('Não foi possível fazer conexão com o site Pudim no momento.')
    else:
        print('Conexão com o site Pudim feita com sucesso.')


accesssite('http://pudim.com.br/')