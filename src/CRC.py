'''
Created on Oct 20, 2013

@author: Derek Neil B00163969
'''

#assumes binary inputs and shifted m'x
def bitwiseDivision(gx, mx):
    rx =0b0
    #divide (XOR) mx by gx
    
    return rx

#assumes binary input gx
def binaryOrderOf(gx):
    order = 0
    
    return order

#assumes binary inputs and unshifted mx
def CRC(gx, mx):
    #get order of gx
    order = binaryOrderOf(gx)
    
    #bitshift mx by order of gx
    mx << order
    
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
    mx >> order
    
    #divide received by gx
    rx = bitwiseDivision(gx, received)
    check=1
    if not rx is 0:
        check=0
    return check, mx 
    
gx = 0b1011 #1011
mx = 0b110100111101 #110100111101

rx, dataToSend = CRC(gx, mx)

check, RTmx = unCRC(gx, dataToSend)

print 'G(x) ' + str(gx)
print 'M(x) ' + str(mx)
print 'R(x) ' + str(rx)
print 'dataToSend ' + str(dataToSend)
print 'check ' + str(check)
print 'M(X) ' + str(RTmx)

