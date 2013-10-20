'''
Created on Oct 19, 2013

@author: Derek
'''

#read text file
f = open('q1in')
def read1k():
    return f.read(1024)

#worker methods
def stringToASCIIBinary(input_string):  
    for x in input_string:
        #convert to ASCII, then format as binary
        yield format(ord(x), 'b')
        
def concatListToEndOfString(stringRef, listRef):  
    for i in range(len(listRef)):
        stringRef+=listRef[i]
    return stringRef

inputStream=''
numStuffedBits = 0
consecutiveOnes = 0
outputStream=''

#convert data to binary
for stream in iter(read1k, ''):
    for binary in iter( stringToASCIIBinary(stream) ):
        
        inputStream+=binary
        
        #check for 5 consecutive 1's
        B = list(binary)
        binaryLength = len(binary)
        for i in range(binaryLength):
            if B[i] is '1':
                if consecutiveOnes is 4:
                    #this is fifth, so bit stuff after it
                    B.insert(i+1, '0')
                    numStuffedBits+=1
                    #increase length for scanning since we inserted
                    binaryLength+=1
                    #reset ones counter
                    consecutiveOnes=0
                else:
                    consecutiveOnes+=1
            else:
                consecutiveOnes=0
        #done working on binary for this char
        outputStream=concatListToEndOfString(outputStream, B)

print 'Initial bits: ' + str(len(inputStream))
print 'Input Binary Stream: ' + str(inputStream)
print 'Stuffed bits: ' + str(numStuffedBits)
print 'Total bits: ' + str(len(inputStream))
print 'Output Binary Stream:' + outputStream
print 'Radio stuffed/total: ' + "%.3g" % ( float(numStuffedBits) / len(outputStream) )