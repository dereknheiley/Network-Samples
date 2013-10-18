#!/usr/bin/python
'''
Created on Oct 18, 2013

@author: Derek Neil B00163969
'''

import sys

#worker method
def stringToASCII(input_string):  
    for x in input_string:
        yield x, ord(x), format(ord(x), 'b')

#read text file
f = open('q1in')
def read1k():
    return f.read(1024)

last=''
trans=0
#convert data to binary
for stream in iter(read1k, ''):
    for word, ascii, binary in iter( stringToASCII(stream) ):
        sys.stdout.write(word +' '+ str( ascii ) +' '+ binary +' ')
        #count NRZ binary transitions
        for i in range(len(binary)):
            if not last is binary[i]:
                last=binary[i]
                trans+=1
                sys.stdout.write('|')
            if binary[i] is "0":
                sys.stdout.write('.')
            else:
                sys.stdout.write('`')
        sys.stdout.write('\n')
        sys.stdout.flush()
    
print '\ntransitions = ' + str(trans)