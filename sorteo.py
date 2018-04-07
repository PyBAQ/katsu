#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------------------------------------
# Copyright:   (c) Cesar Herdenez 2018
# Licence:     BSD 3-Clause License
#---------------------------------------------

import signal
import sys
from random import shuffle

test = ['Javier', 'Mateo', 'Leonardo', 'Oswal', 'Cesar', 'Ivan', 'Domicilio de Dominos']
asistentes = []
winners = []
def winner(data):
    shuffle(data)
    w = data.pop()
    winners.append(w)
    return w

def exit_app(signal,frame):
    w = "\n".join(winners)
    print("\nFelicitaciones a todos los Ganadores\n{}".format(w))
    sys.exit(0)

signal.signal(signal.SIGINT, exit_app)
while True:
    input("El Ganador es ....")
    print(winner(test))

    
