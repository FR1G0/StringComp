def __main__():
    '''Algoritmh to compare 2 strings'''
    #Define the strings to be compared
    string1 = "This is the first string, it's a very simple string and has nothing special"
    string2 = "This is the second string, it's a very simple string as well and has nothing special"
    #Clean the strings
    print(f"BEFORE:\n{string1}\n{string2}\n\nAFTER:")
    string1 = stabilise_patient(f"{string1} ")
    string2 = stabilise_patient(f"{string2} ")
    print(f"{string1}\n{string2}\n")
    #Call main function
    compare(string1, string2)

def _get_lenght(string1, string2):
    '''Get the max lenght between 2 strings'''
    len1, len2 = len(string1.split()), len(string2.split())
    if len1 > len2:
        return len1
    else:
        return len2

def stabilise_patient(string):
    '''Make string following standarts'''
    #Define the blacklists
    word_bl = ['a' ,"is", "it", "for",
               "it's", "an" ,"as", "and",
               "the", "has", "this",
               "that", "there"]
    char_bl = ['.', ',', '?', '!']
    #Remove unnecessary stuff
    word, neat = '', ''
    for entry in string:
        if entry == ' ':
            if not word in word_bl:
                neat += f"{word} "
            word = ''
        elif not entry in char_bl:
             word += entry.lower()
    return(neat)

def compare(string1, string2):
    '''Campare word by word 2 strings'''
    lenght, x = _get_lenght(string1, string2), 0
    for entry in string1.split():
        if entry in string2:
            x += 1
    perc = x/lenght*100
    print(f"MATCHINGS:\t{perc}%\n")

if __name__ == '__main__':
    __main__()
