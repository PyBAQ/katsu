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

def winner(data):
    shuffle(data)
    return data.pop()

def exit_app(signal,frame):
    print("\nFelicitaciones a todos los Ganadores\n\n")
    sys.exit(0)

signal.signal(signal.SIGINT, exit_app)
while True:
    input("El Ganador es ....")
    print(winner(test))

    
