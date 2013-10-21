'''
Created on Oct 20, 2013

@author: Derek Neil B00163969
'''

#assumes binary inputs and shifted m'x
def bitwiseDivision(gx, mx):
    ordergx = binaryOrderOf(gx)
    if ordergx > binaryOrderOf(mx): #incorrect mx input
        rx=-1
        
    else:#divide (XOR) m'x by gx
        rx = 1
        mxstr = format(mx, 'b')
        mxstr = mxstr[1:]
        #get first ordergx bits from m'x
        for i in range(ordergx): 
            #build rx
            rx = rx << 1
            newbit = int(mxstr[0])
            rx = rx | newbit
            
            #trim m'x
            mxstr = mxstr[1:]
            
        #XOR division
        rx = rx ^ gx
        
        #continue until can't divide again
        while len(mxstr)>0:
            #get next rx
            while len(mxstr)>0 and binaryOrderOf(rx) < ordergx:
                #build rx
                rx = rx << 1
                newbit = int(mxstr[0])
                rx = rx | newbit
                
                #trim m'x
                mxstr = mxstr[1:]
            #XOR division
            if binaryOrderOf(rx) is ordergx:
                rx = rx ^ gx
        
        #bitshift remaining number of remaining 0's left in m'x
        if len(mxstr) >0:
            rx = rx << len(mxstr)
        
    return rx

#assumes binary input gx
def binaryOrderOf(gx):
    order = 0
    while gx > 1:
        order+=1
        gx = gx >> 1
    return order

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
    
gx = 0b1011
mx = 0b110100111101
print 'G(x) ' + format(gx, 'b')
print 'M(x) ' + format(mx, 'b')

rx, dataToSend = CRC(gx, mx)
print 'R(x) ' + format(rx, 'b')
print 'dataToSend ' + format(dataToSend, 'b')

check, RTmx = unCRC(gx, dataToSend)
print 'check ' + (['failed', 'passed'][check])
print 'M\'(X) ' + format(RTmx, 'b')