#Comparison app takes 2 strings and prints out the % of similarities between the two
import sys
import json

first_string = "This is the first string, it's a very simple string and has nothing special"    #First string taken from console
second_string = "This is the second string, it's a very simple string as well and has nothing special"     #Second string taken from console


def __main__():
    #seprates the words and places them into a dictionary
    print(compare(listthis(first_string.lower()),listthis(second_string.lower())))
    

def compare(first_list,second_list):
    score = 0.0
    print(first_list)
    print(second_list)
    maxlenght = int
    if len(first_list) > len(second_list):
        maxlenght = len(first_list)
    else:
        maxlenght = len(second_list)
    
    #   the algorithm scroll each word from first list with each word from second
    simialrities = 0
    for first in first_list:
        for second in second_list:
            if first == second:
                simialrities = simialrities +1
                
    score = simialrities/maxlenght * 100

    return score



##this function removes every word except keywords
def keythis(thelist):
    rmthis = ["a","is","it","for","it's","as","and","the","has","this","that","there"]
    for counter in range(len(thelist)):
        for rm in rmthis:
            if thelist[counter] == rm.lower():
                thelist[counter] = " "

    while (thelist.count(" ")):
        thelist.remove(" ")
    return thelist
        

#this function takes strings and splits them to a list
def listthis(string):
    dict_words = []
    pos=0
    string = string + " "

    for counter in range(len(string)):
        if string[counter] == " ":
            dict_words.append(string[pos:counter])
            pos = counter+1
    
    return keythis(dict_words)


__main__()