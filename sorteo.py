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
import random
from collections import namedtuple
from random import shuffle


# load csv files
def cvsReader(filename:str) -> list:    
    with open('{}.csv'.format(filename),'r') as f:
        reader = csv.reader(f)
        data = namedtuple(filename,next(reader))
        return [data(*row) for row in reader ]

     
participants = cvsReader('participants')
reward = cvsReader('reward')

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

def get_reward(data:list) -> str:
    try:
        shuffle(data)
        w = random.choice(data)
        w = '{}'.format(w.premio)
        remove_reward(w)
        return w 
    except IndexError:
        os.kill(os.getpid(), signal.SIGINT)

def exit_app(signal,frame):
    w = "\n".join(winners)
    print("\nFelicitaciones a todos los Ganadores\n{}".format(w))
    sys.exit(0)

def remove_reward(r):
    for reward_object in reward:
        if(reward_object.premio == r):
            reward.remove(reward_object)

signal.signal(signal.SIGINT, exit_app)

n = int(input("Numero de iteraciones: "))
if(n <= len(reward)):    
    for x in range(0,n):
        input("El Ganador es ....")
        print(winner(participants) + " [ PREMIO: "+ get_reward(reward) +" ]")
    w = "\n".join(winners)
    print("\nFelicitaciones a todos los Ganadores\n{}".format(w))
else:
    print("La cantidad de regalos no satisface la cantidad de participantes")
