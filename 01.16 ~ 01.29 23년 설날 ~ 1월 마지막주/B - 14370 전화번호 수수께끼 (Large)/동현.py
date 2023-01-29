from collections import deque
import sys

from itertools import combinations
from pprint import pprint

n = int(input())

for t in range(n):
    dict = {}
    ls = list(input())
    for j in range(len(ls)):
        if ls[j] in dict:
            dict[ls[j]] +=1 
        else:
            dict[ls[j]] =1 

    result = []
    if "Z" in dict.keys():
        for _ in range(dict["Z"]):
            result.append("0")
            dict["Z"] -=1
            dict["E"] -=1
            dict["R"] -=1
            dict["O"] -=1
            
    if "W" in dict.keys():
        for _ in range(dict["W"]):
            result.append("2")
            dict["T"] -=1
            dict["W"] -=1
            dict["O"] -=1
    if "U" in dict.keys():
        for _ in range(dict["U"]):
            result.append("4")
            dict["F"] -=1
            dict["O"] -=1
            dict["U"] -=1
            dict["R"] -=1
    if "X" in dict.keys():
        for _ in range(dict["X"]):
            result.append("6")
            dict["S"] -=1
            dict["I"] -=1
            dict["X"] -=1
    if "G" in dict.keys():
        for _ in range(dict["G"]):
            result.append("8")
            dict["E"] -=1
            dict["I"] -=1
            dict["G"] -=1
            dict["H"] -=1
            dict["T"] -=1
    if "R" in dict.keys():
        for _ in range(dict["R"]):
            result.append("3")
            dict["T"] -=1
            dict["H"] -=1
            dict["R"] -=1
            dict["E"] -=2
     

    if "F" in dict.keys():
        for _ in range(dict["F"]):
            result.append("5")
            dict["F"] -=1
            dict["I"] -=1
            dict["V"] -=1
            dict["E"] -=1
    if "V" in dict.keys():
        for _ in range(dict["V"]):
            result.append("7")
            dict["S"] -=1
            dict["E"] -=1
            dict["V"] -=1
            dict["E"] -=1
            dict["N"] -=1

    if "I" in dict.keys():
        for _ in range(dict["I"]):
            result.append("9")
            dict["N"] -=2
            dict["I"] -=1
            dict["E"] -=1
    if "O" in dict.keys():
        for _ in range(dict["O"]):
            result.append("1")
    result.sort()
    a = "".join(result)
    print(f'Case #{t+1}: {a}')