def __main__():
    '''Algoritmh to compare 2 strings'''
    #Define the strings
    string1 = "This is the first string, it's a very simple string and has nothing special"
    string2 = "This is the second string, it's a very simple string as well and has nothing special"
    #Call main function
    compare(string1, string2)

def _max_lenght(string1, string2):
    '''Get the max lenght between the 2 strings'''
    if len(string1.split()) > len(string2.split()):
        return len(string1.split())
    else:
        return len(string2.split())

def _normalise(string):
    '''Make string following standarts'''
    #Define the blacklist
    blacklist = [" a " ," is ", " it ", " for ",
                 " it's ", " an " ," as ", " and ",
                 " the ", " has ", " this ", " that ",
                 " there ", '.', ',', '?', '!']
    #Remove unnecessary stuff
    for entry in blacklist:
        string = string.replace(entry, ' ')
    return string

def compare(string1, string2):
    '''Campare word by word 2 strings'''
    #Clean the strings
    string1 = _normalise(f"{string1} ".lower())
    string2 = _normalise(f"{string2} ".lower())
    #Calculate matches
    lenght, c = _max_lenght(string1, string2), 0
    for entry in string1.split():
        if entry in string2:
            c += 1
    print(f"\n[+] There are {c} matching words out of {lenght}\n")

if __name__ == '__main__':
    __main__()
