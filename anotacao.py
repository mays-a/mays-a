#básico
teste=True
x=float(input('Digite um número: ')) #float inclui números com vírgula
h=22 #nn faz sentido

if x>2 and x<5:
    pass
if x<=2 or x>=5:
    pass
if not(x>2 and x<5):
    pass

#-----------------------------------------------------------------

if x>0 and x<=20:
    if h>20: #if alinhado, um dentro do outro
        r=x*x
        print('Resposta: ', r)
elif h> 20: #nn faz sentido, nn tem coorrelção
    print('')
else:
    print('Número inválido,deveria ser maior que zero.')

#---------------------------------------------------------------------------------------------------------------
#for repete na lista
l=list(range(10)) #lista de 0 a 9
print(l)
v=list()
v.append(9)
v.append(8)
v.append(7)
v.append(6)
s=0 #multipli s=1
for x in range(len(v)): #[3,8,8,'prampero',6]:   #len é o tamanho
    s=s+v[x] #explícita   #implícita: s+=v[x]          #multipli s=s*v[x]
    print(x,v[x]) #x é a posição e o v[x] é o elemento
print(' a soma é:', s)

#------------------------------------------------------------------------------

for i in range(-29,-19,1):
    print(i)
for i in range(10,-1,-1):
    print(i)

while(i<100):
    print(i,end=' ')
    i=i+1
#---------------------------------------------------------------------------------------------------------------
#ex1
lista = list()
op=0
while op!=3:
    print('1 - Incluir')
    print('2 - Listar')
    print('3 - Sair')
    op = int(input('Escolha uma opção: '))
    if op==1:
        nome= input('Digite um nome: ')
        lista.append(nome)
        print(nome, 'Incluído com sucesso')
    if op==2:
        for i in range(len(lista)):
            if lista[i][0]=='a' or lista[i][0]=='A':
                print(lista[i])
print('Terminou...')
#-------------------------------------------------------------------------------------------------------------
#ex2
import math
from random import randint
import numpy as np

v=list(10)
for i in range(10):
    v.append(randint(0, 10))
print('vetor: ',v)
maior=-math.inf

#Maior
for i in range(10):
    if maior<v[i]:
        maior=v[i]

#Média
s=0
for i in range(10):
    s=s+v[i]
media=s/len(v)
print('Média = ', media)


#Desvio padrão
sdp=0
for i in range(10):
    sdp=sdp+((v[i]-media)**2)
dp=math.sqrt(sdp/len(v))
print('Desvio padrão= ', dp)
print('Com o numpy')
print('Media= ', np.avarage(v), 'Desvio Padrão: ', np.std(v))

#--------------------------------------------------------------------------------------------------------
#Classe
class Pessoa:
    cont=0
    def __init__(self): #construtor -> é o primeiro a ser executado qnd um objeto for instanciado da classe
        self.nome='sebastao' #publico
        self.__peso=0 #privado
        Pessoa.cont+=1 #compartilhado com todos os usuários
    def setPeso(self,p):
        try:
            if not (type(p) is float):
                p=float(p)
            if(p<=0):
                raise Exception('Peso deve ser maior que zero')
            else:
                self.__peso=p
        except Exception as erro:
            print('Erro: ', erro)
    def getPeso(self):
        return self.__peso
    def toString(self):
        #return 'Cont= '+ str(Pessoa.cont)+'Nome= '+obj.nome+ 'Peso= '+ str(obj.getPeso())
        return f'Cont= {Pessoa.cont} Nome= {obj.nome} Peso= {obj.getPeso():.2f}'
#principal
obj=Pessoa()
print('Cont= ', Pessoa.cont, 'Nome= ',obj.nome, 'Peso= ', obj.getPeso())
obj.nome=input('Digite um nome: ')
aux=input('Digite um peso: ')
obj.setPeso(aux)
print('Cont= ', Pessoa.cont, 'Nome= ',obj.nome, 'Peso= ', obj.getPeso())
