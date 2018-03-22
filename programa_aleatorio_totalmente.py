from random import randint

def escoger_ganador():
  participantes = ['Javier', 'Mateo', 'Leonardo', 'Oswal', 'Cesar', 'Ivan', 'Domicilio de Dominos']
  
  return participantes[randint(0,1000)*(2**0-1)+1]


print('El afortunado ganador es... ' + escoger_ganador())
