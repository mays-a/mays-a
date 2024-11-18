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
