#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------------------------------------
# Copyright:   (c) Cesar Herdenez 2018
#---------------------------------------------

'''
PUNTOS PENDIENTES 
Los premios deben poderse cargar de un .csv (Los premios varían en cada meetup)
Los premios deben ser escogidos al azar de un listado
Un premio al azar se asigna al ganador (Se obtiene un premio al azar del listado de premios y se asigna a un ganador al azar. El resultado debe imprimirse por consola)
'''

import csv
import signal
import sys
import os 
from collections import namedtuple
from random import shuffle

# load csv files
def cvsReader(filename:str) -> list:    
    with open('{}.csv'.format(filename),'r') as f:
        reader = csv.reader(f)
        data = namedtuple(filename,next(reader))
        return [data(*row) for row in reader ]

     
participants = cvsReader('participants')
premios = cvsReader('reward')

winners = []
def winner(data:list) -> str:
    try:
        shuffle(data)
        w = data.pop()
        w = '{} {}'.format(w.name,w.lastname)
        winners.append(w)
        return w 
    except IndexError:
        os.kill(os.getpid(), signal.SIGINT)

rewards = []
def reward(data:list) -> str:
    try:
        shuffle(data)
        r = data.pop()
        r = '{}'.format(r.reward)
        rewards.append(r)
        return r 
    except IndexError:
        os.kill(os.getpid(), signal.SIGINT)

def exit_app(signal,frame):
    w = "\n".join(winners)
    print("\nFelicitaciones a todos los Ganadores\n{}".format(w))
    sys.exit(0)

signal.signal(signal.SIGINT, exit_app)
while True:
    input("El premios es ....")
    print(reward(premios))
    input("El Ganador es ....")
    print(winner(participants))
    print("\n\n")