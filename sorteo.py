#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------------------------------------
# Copyright:   (c) Cesar Herdenez 2018
# Licence:     BSD 3-Clause License
#---------------------------------------------

from random import shuffle

test = ['Javier', 'Mateo', 'Leonardo', 'Oswal', 'Cesar', 'Ivan', 'Domicilio de Dominos']
asistentes = []

def winner(data):
    shuffle(data)
    return data.pop()

while True:
    input("El Ganador es ....")
    print(winner(test))

    
