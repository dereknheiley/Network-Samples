'''
Created on Oct 19, 2013

@author: Derek
'''

#read text file
f = open('q1in')
def read1k():
    return f.read(1024)

#worker method
def stringToASCIIBinary(input_string):  
    for x in input_string:
        #convert to ASCII, then format as binary
        yield format(ord(x), 'b')

inputStream=''
numStuffedBits = 0
consecutiveOnes = 0
binaryLength=0
outputStream=''

#convert data to binary
for stream in iter(read1k, ''):
    for binary in iter( stringToASCIIBinary(stream) ):
        
        #check for 5 consecutive 1's
        inputStream+=binary
        binaryLength=len(binary)
        B = list()
        for i in range(binaryLength):
            if binary[i] is 1:
                if consecutiveOnes is 4:
                    #this is fifth, so bit stuff after it
                    
                    #lazy create list to better handle multiple insertions
                    if len(B) < 1:
                        B=list(binary)
                    #bit stuff a zero
                    B.insert(i+1, '0')
                    numStuffedBits+=1
                    #reset counter
                    consecutiveOnes=0
                else:
                    consecutiveOnes+=1
            else:
                consecutiveOnes=0
        #done looking at binary for this char
        outputStream+=B.__str__()

total = binaryLength + numStuffedBits

print 'Initial bits: ' + len
print 'Input Binary Stream: ' + inputStream
print 'Stuffed bits: ' + numStuffedBits
print 'Total bits: ' + total
print 'Output Binary Stream' + outputStream
print 'Radio stuffed/total' + (numStuffedBits/total)