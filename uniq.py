import sys
from os import path
from itertools import zip_longest

def fileopen(file):
    try:
          f = open(file, 'r')
    except FileNotFoundError:
          sys.exit('{}: No Such Use: {}'.format(sys.argv[0],file))
    return f

def option(op):
    optypelist = ['-i','-d','-u']
    for optype in optypelist:
            if op == optype:
                return True

def output(type, datalist):
    if type is not None:
        file = open(type, 'w', encoding='Shift_JIS')
        for data in datalist:
            file.write(data + '\n')
        file.close()
    else:
        for data in datalist:
            print(data)

argc = len(sys.argv)
op = None
outPutFile = None
if argc == 1:
    f = sys.stdin
elif argc < 5:
    if sys.argv[1].startswith('-'):
        if option(sys.argv[1]):
            op = sys.argv[1]
            f = fileopen(sys.argv[2])
            if argc == 4:
                outPutFile = sys.argv[3]
        else:
           sys.exit('{}: No Such Option: {}'.format(sys.argv[0],sys.argv[1])) 
    elif path.isfile(sys.argv[1]):
        f = fileopen(sys.argv[1])
        if argc == 3:
          outPutFile = sys.argv[2]
    else:
       sys.exit('{}: Not Such File: {}'.format(sys.argv[0],sys.argv[1])) 
else:
    sys.exit('{}: No Such argcount:　{}'.format(sys.argv[0],argc))

input = f.read()
sentencelist = input.splitlines()
if op == '-i':
    tmp_lowlist = []
    for sentence in sentencelist:
        tmp_lowlist.append(sentence.lower())
    sentencelist = tmp_lowlist
elif op == '-u':
    sentencelist.sort()

words1 = sentencelist
words2 = words1[1:]
orgwords = []
diffwords = []
for word1,word2 in zip_longest(words1, words2):
    if word1 == word2:
        diffwords.append(word2)
    else:
        orgwords.append(word1)

if op == '-d':
    output(outPutFile, diffwords)
else:
    output(outPutFile, orgwords)
