#!/usr/bin/python
'''
Created on Oct 18, 2013

@author: Derek Neil B00163969
'''

#worker method
def stringToASCIIBinary(input_string):  
    for x in input_string:
        yield format(ord(x), 'b')

#read text file
f = open('q1in')
def read1k():
    return f.read(1024)

last=''
NRZ=''
NRZtrans=0
M=''
Mtrans=0
#convert data to binary
for stream in iter(read1k, ''):
    for binary in iter( stringToASCIIBinary(stream) ):
        #count binary transitions
        for i in range(len(binary)):
            if not last is binary[i]:
                last=binary[i]
                
                #NRZ count
                NRZtrans+=1
                NRZ+='|'
                
                #Manchester count
                Mtrans+=1
                
            else:
                # no NRZ trans
                Mtrans+=2
                M+='|'
                
            if binary[i] is "0":
                NRZ+='_'
                M+='`|.'
            else:
                NRZ+='`'
                M+='.|`'
        
print 'NRZ transitions = ' + str(NRZtrans)
print NRZ

print '\nManchester transitions = ' + str(Mtrans)
print M