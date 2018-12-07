'''
Created on 7 dic. 2018

@author: Pablo
'''
    
def operation(input):
    number = 0
    for a in input:
        if a[:1] == '+':
            number += int(a[1:])
        else:
            number -= int(a[1:])
    
    return number

    
puzzle = [s[:-1] for s in open('input.txt').readlines()]
print(operation(puzzle))