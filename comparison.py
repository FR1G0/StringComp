#Comparison app takes 2 strings and prints out the % of similarities between the two
import sys
import json

first_string = "This is the first string, it's a very simple string and has nothing special"    #First string taken from console
second_string = "This is the second string, it's a very simple string as well and has nothing special"     #Second string taken from console


def __main__():
    #seprates the words and places them into a dictionary
    list_first = list
    list_second = list
    list_first = listthis(first_string)
    print(list_first)

##this function removes every word except keywords
def keythis(thelist):
    rmthis = ["a","is","it","for","it's","as","and","the","has","this","that","there"]
    for counter in thelist: ## for each element on the list
        print(thelist)
        for rm in rmthis:
            if counter == rm:
                thelist.remove(counter)
                
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