'''
Created on 6 dic. 2018

@author: Pablo
'''

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

def remove_letters(string, i):
    return string[:i] + string[i+1:]

def generate_sublists(l, i):
    return list(map(lambda str: remove_letters(str, i), l))


boxes = [s[:-1] for s in open('input.txt').readlines()]

for i in range(len(boxes[0])):
    sublist_inport = generate_sublists(boxes, i)
    if len(set(sublist_inport)) == len(sublist_inport):
        continue
    for k, v in group_letters(sublist_inport).items():
        if v == 2:
            print(k)
            break
        


