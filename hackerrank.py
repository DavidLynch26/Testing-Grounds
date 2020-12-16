#!/bin/python3

import math
import os
import random
import re
import sys

def queue(lst):
    return ("queue", lst)

def cycle(lst, l, n):
    que = queue(lst)
    cycle_count = 0
    while get_item(que) - l > 0:
        dequeue(que, l)
        cycle_count += l
    cycle_count += get_item(que)
    print(cycle_count)

def dequeue(queue, l):
    new_item = get_item(queue)
    new_item -= l
    contents(queue).pop(0)
    contents(queue).insert(len(contents(queue))+1, new_item)
    return queue

def contents(queue):
    return queue[1]

def get_item(queue):
    return contents(queue)[0]

if __name__ == '__main__':
    ln = input().rstrip().split()

    l = int(ln[0])

    n = int(ln[1])

    processes = list(map(int, input().rstrip().split()))
    
    cycle(processes, l, n)