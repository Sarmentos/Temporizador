import time

t = input('Dgite o tempo (em segundos): ')

if t.isdigit():
    t = int(t)
else:
    print('Erro: tempo deve ser um número inteiro')
    quit()
    
while t:   
    minutos, segundos = divmod(t, 60)
    tempo = "{:02d}:{:02d}".format(minutos, segundos)
    print(tempo, end="\r")
    time.sleep(1)
    t = t - 1
    
print("TEMPO ACABOU!!!")