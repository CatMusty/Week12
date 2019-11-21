#Justin Orji
#CSCI 102-E
#Week12-utility

def PrintOutput(printable):
    print('OUTPUT %s' % (printable))

def LoadFile(file):
    with open(file, 'r') as filer:
        filere = filer.read()
        filerio = filere.splitlines()
        return filerio
        
