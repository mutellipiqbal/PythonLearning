# -*- coding: cp1252 -*-

def yunilish_kilish01(x):
        
        if x[-1] == "p" or x[-1] == "s" or x[-1] == "f" or x[-1] == "t" or x[-1] == "k" or x[-1] == "ch" or x[-1] == "sh" or x[-1] == "h" or x[-1] == "q" or x[-1] == "gh":
                return x+"qa"
        elif x[-1] == "q" and x[-2] == "i":
                 return x+"qa"
                
            
        
        else:
                
                
                if x[-1] != "p" or x[-1] != "s" or x[-1] != "f" or x[-1] != "t" or x[-1] != "k" or x[-1] != "ch" or x[-1] != "sh" or x[-1] != "h":
                        if x[-1] == "a" and x[-3] == "a":
                                x1 = x[:-1]
                                return  x1+"igha"
                        elif x[-1] == "a" and x[-4] == "a":
                                x1 = x[:-1]
                                return  x1+"igha"
                        elif x[-2] == "a" or x[-2] == "o" or x[-2] == "u" or x[-2] == "é":
                                return x+"gha"
                        elif x[-1] == "o" or x[-1] == "u" or x[-1] == "é":
                                return x+"gha"
                        elif x[-1] == "a":
                                return x+"gha"
                        elif x[-4] == "a" and x[-2] == "i":
                                return x+"gha"
                        elif x[-3] == "a" and x[-2] == "i":
                                return x+"gha"
                        elif x[-3] == "i" and x[-1] == "i":
                                return x+"gha"
                        elif x[-3] == "é" and x[-1] == "i":
                                return x+"gha"
                        elif x[-3] == "o" and x[-1] == "i":
                                return x+"gha"
        
myList=[]
while True:
    input1 = raw_input("soz qoshung: ")
    if input1 == 'ok':
        break
    myList.append(input1)

print myList
for x in myList:
    myNewList = [yunilish_kilish01(x)]
    print myNewList
'''
        if x[-2] == "e" or x[-2] == "i" or x[-2] == "ü" or x[-2] == "ö":
            if x[-1] == "p" or x[-1] == "s" or x[-1] == "f" or x[-1] == "t" or x[-1] == "k" or x[-1] == "ch" or x[-1] == "sh" or x[-1] == "h" or x[-1] == "q":
                return x+"ke"
            else:
                x[-1] != "p" or x[-1] != "s" or x[-1] != "f" or x[-1] != "t" or x[-1] != "k" or x[-1] != "ch" or x[-1] != "sh" or x[-1] != "h"
                return x+"ge"
        elif x[-1] == "e" or x[-1] == "i" or x[-1] == "ü" or x[-1] == "ö":
            return x+"ge"

'''

