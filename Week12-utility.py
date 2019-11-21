#Justin Orji
#CSCI 102-E
#Week12-utility

def PrintOutput(printable):
    print('OUTPUT %s' % (printable))

def LoadFile(file):
    with open(file, 'r') as filer:
        filere = filer.read()
        filerio = filere.splitlines()

def UpdateString(stringUno, stringDos, num):
    string_list = []
    for i in stringUno:
        string_list.append(i)
        
    del string_list[num]
    string_list.insert(num, stringDos)

    final_string = ''
    for i in string_list:
        final_string += i
    print('OUTPUT {final}'.format(final=final_string))

def FindWordCount(issalist, issastring):
    list_string = ''
    for i in issalist:
        list_string += i
    count = list_string.count(issastring)
    print('OUTPUT %d' % (count))
