'''
Created on 6 dic. 2018

@author: Pablo
'''

def group_letters(input):
    patterns = {}
    for letra in input:
        patterns[letra] = patterns.get(letra, 0) + 1
    return patterns


def getRepetitions(input):
    values = group_letters(input)
    return(2 in values.values(), 3 in values.values())
        

boxes = [s[:-1] for s in open('input.txt').readlines()]

#repetitions: Tupla de dos
# - [0] True: letra se repite dos veces
# - [1] True: letra se repite tres veces
repetitions = list(map(getRepetitions, boxes))

boxes_2 = len(list(filter(lambda x: x[0] is True, repetitions)))
boxes_3 = len(list(filter(lambda x: x[1] is True, repetitions)))

print(boxes_2)
print(boxes_3)

print(boxes_2 * boxes_3)


