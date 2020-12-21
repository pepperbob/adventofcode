#!/usr/bin/env python
import fileinput

class Num:
    def __init__(self, number):
        self.number = number

    def __add__(self, num):
        return Num(self.number + num.number)

    def __sub__(self, num):
        return Num(self.number * num.number)

def pimp(op):
    pimped = ""
    flag = False
    for s in op:
        if(s in list("1234567890")):
            if(not flag):
                pimped += "Num("
                flag=True
        else:
            if flag:
                pimped += ")"
                flag = False
        pimped += s

    if flag:
        pimped += ")"        
    return pimped.replace("*", "-")

ops = [s for s in list(map(lambda  s: s.strip(), fileinput.input())) if len(s) > 1]

solution = sum([eval(pimp(op)).number for op in ops])
print(f"Solution: {solution}")    