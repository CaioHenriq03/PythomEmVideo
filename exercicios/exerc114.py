import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('Não foi possivel acessar o site. ')
else:
    print('Conseguiu acessar o site com sucesso! ')