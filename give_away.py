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

# Defining data type for namedtuple
Participant = namedtuple('participants', ['name', 'lastname'])
Reward = namedtuple('reward', ['item'])

def cvsReader(filename:str) -> list:
    """
    The function `cvsReader` reads a CSV file and returns its data as a list of named tuples.
    """
    with open('{}.csv'.format(filename),'r') as f:
        reader = csv.reader(f)
        data = namedtuple(filename,next(reader))
        return [data(*row) for row in reader ]

def winner(data:list[Participant]) -> str:
    """
    This Python function randomly selects a participant from a list, adds their full name to a winners
    list, and then deletes the participant from the list.
    """
    if not data:
        raise ValueError("The participant list is empty.")

    if not isinstance(data, list):
        raise TypeError("The data must be of type list.")

    if not all(isinstance(participant, tuple) and hasattr(participant, 'name') and hasattr(participant, 'lastname') for participant in data):
        raise AttributeError("All elements in the data must be of type Participant.")

    shuffle(data)
    w = random.choice(data)
    w = '{} {}'.format(w.name,w.lastname)
    winners.append(w)
    delete_participant_by_fullname(w)
    return w

def get_reward(data:list[Reward]) -> str:
    """
    This function randomly selects and returns a reward item from a list, removing it from the list in
    the process, and raises an IndexError exception if the list is empty.
    """
    if not data:
        raise ValueError("The reward list is empty.")

    if not isinstance(data, list):
        raise TypeError("The data must be of type list.")

    if not all(isinstance(reward, tuple) and hasattr(reward, 'item') for reward in data):
        raise AttributeError("All elements in the data must be of type Participant.")

    shuffle(data)
    w = random.choice(data)
    w = '{}'.format(w.item)
    remove_reward(w)
    return w

def exit_app(signal,frame):
    """
    The function `exit_app` prints out a congratulatory message to the winners and exits the
    application.
    """
    w = "\n".join(winners)
    print("\nFelicitaciones a las personas Ganadoras\n{}".format(w))
    sys.exit(0)

def remove_reward(r):
    """
    The function `remove_reward` iterates through a list of reward objects and removes the object with a
    specific item value.
    """
    for reward_object in reward:
        if(reward_object.item == r):
            reward.remove(reward_object)

def delete_participant_by_fullname(fullname: str):
    """
    This function deletes a participant from a list based on their full name.
    """
    name, lastname = fullname.split(" ", 1)

    participants[:] = [p for p in participants if not (p.name.lower() == name.lower() and p.lastname.lower() == lastname.lower())]

def run_app():
    for x in range(0, len(reward)):
        try:
            input("El premio es para ....")
            print(winner(participants) + " [ PREMIO: "+ get_reward(reward) +" ]")
        except Exception as e:
            print('ERROR-HANDLE', e)
            os.kill(os.getpid(), signal.SIGINT)

# Global variable
signal.signal(signal.SIGINT, exit_app)
participants: list[Participant] = cvsReader('participants')
reward: list[Reward] = cvsReader('reward')
winners: list[Participant] = []


if __name__ == '__main__':
    run_app()
    w = "\n".join(winners)
    print("\nFelicitaciones a las personas Ganadoras\n{}".format(w))
