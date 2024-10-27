#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------------------------------------
# Copyright:   MIT
#---------------------------------------------


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
        w = '{}'.format(w.item)
        remove_reward(w)
        return w 
    except IndexError:
        os.kill(os.getpid(), signal.SIGINT)

def exit_app(signal,frame):
    '''
    Exit the loop with Ctrl-C
    '''
    w = "\n".join(winners)
    print("\nFelicitaciones a las personas Ganadoras\n{}".format(w))
    sys.exit(0)

def remove_reward(r):
    for reward_object in reward:
        if(reward_object.item == r):
            reward.remove(reward_object)

signal.signal(signal.SIGINT, exit_app)

def main()->None:
    for x in range(0, len(reward)):
        input("El premio es para ....")
        print(winner(participants) + " [ PREMIO: "+ get_reward(reward) +" ]")
    
    w = "\n".join(winners)
    
    print("\nFelicitaciones a las personas Ganadoras\n{}".format(w))


if __name__ == '__main__':
    main()