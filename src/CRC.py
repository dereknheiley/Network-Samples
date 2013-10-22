'''
Created on Oct 20, 2013

@author: Derek Neil B00163969
'''

#assumes binary inputs and unshifted mx
def CRC(gx, mx):
    #get order of gx
    order = binaryOrderOf(gx)
    
    #bitshift mx by order of gx
    mx = mx << order
    
    #calculate rx
    rx = bitwiseDivision(gx, mx)
    
    #bitwise XOR
    dataToSend = mx ^ rx
    
    return rx, dataToSend


#assumes binary inputs and unmodified received data
def unCRC(gx, received):
    #get order of gx
    order = binaryOrderOf(gx)
    
    #reverse bitshift received by order of gx
    mx = received >> order
    
    #divide received by gx
    rx = bitwiseDivision(gx, received)
    check=0
    if rx is 0:
        check=1
    return check, mx 


#assumes binary inputs and shifted m'x
def bitwiseDivision(gx, mx):
    ordergx = binaryOrderOf(gx)
    if ordergx > binaryOrderOf(mx): #incorrect mx input
        rx=-1 #flag bit
        
    else:#divide (XOR) m'x by gx
        rx = 1
        mxstr = format(mx, 'b')
        # would be more efficient to convert directly
        # from int to binary bit values in linked-list
        # but no built in linked list type, and not worth
        # time to implement or install for assignment
        mxstr = mxstr[1:]
        
        #consume m'x
        while len(mxstr)>0:
            #get next rx
            while len(mxstr)>0 and binaryOrderOf(rx) < ordergx:
                #build rx
                rx = rx << 1
                rx = rx | int(mxstr[0])
                
                #trim m'x
                mxstr = mxstr[1:]
                
            #XOR division
            if binaryOrderOf(rx) is ordergx:
                rx = rx ^ gx
    return rx


#assumes binary input gx
def binaryOrderOf(gx):
    order = 0
    while gx > 1:
        order+=1
        gx = gx >> 1
    return order

#worker method
def stringToASCIIBinary(input_string):  
    for x in input_string:
        #convert to ASCII, then format as binary
        yield format(ord(x), 'b')
        
        
print 'demo'
gx = 0b1101
mx = 0b110100111101
print 'G(x) ' + format(gx, 'b')
print 'M(x) ' + format(mx, 'b')

rx, dataToSend = CRC(gx, mx)
print 'R(x) ' + format(rx, 'b')
print 'dataToSend ' + format(dataToSend, 'b')

check, RTmx = unCRC(gx, dataToSend)
print 'check ' + (['failed', 'passed'][check])
if check:
    print 'M(X) ' + format(RTmx, 'b')


print '\ndemo2'
gx = 0b1101
msg = 'Hi'
bitStream = ''
#convert msg to binary
for binary in iter( stringToASCIIBinary(msg) ):
    bitStream+=binary
mx = int(bitStream) #convert message to ASCII numbers
print 'G(x) ' + format(gx, 'b')
print 'Message ' + msg
print 'M(x) ' + format(mx, 'b')

rx, dataToSend = CRC(gx, mx)
print 'R(x) ' + format(rx, 'b')
print 'dataToSend ' + format(dataToSend, 'b')

check, RTmx = unCRC(gx, dataToSend)
print 'check ' + (['failed', 'passed'][check])
if check:
    print 'M(X) ' + format(RTmx, 'b')


print '\na)'
gx = 0b1011
mx = 0b110100111101
print 'G(x) ' + format(gx, 'b')
print 'M(x) ' + format(mx, 'b')

rx, dataToSend = CRC(gx, mx)
print 'R(x) ' + format(rx, 'b')
print 'dataToSend ' + format(dataToSend, 'b')

check, RTmx = unCRC(gx, dataToSend)
print 'check ' + (['failed', 'passed'][check])
if check:
    print 'M(X) ' + format(RTmx, 'b')


print '\nb)'
gx = 0b1001
px = 0b10110011101
print 'G(x) ' + format(gx, 'b')
print 'P(x) ' + format(px, 'b')

check, RTmx = unCRC(gx, px)
print 'check ' + (['failed', 'passed'][check])
if check:
    print 'M(X) ' + format(RTmx, 'b')