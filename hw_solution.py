'''
check if word appear in file
'''
# easier solution :
def findKeyInFile(word, filepath):
    with open(filepath) as f:
        for line in f.readlines():
            if line.count(word) > 0:
                return line
    return None


