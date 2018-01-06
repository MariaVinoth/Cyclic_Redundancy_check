import binascii

gx = '1101'
mx = '1101011'
m_x = '1101011000'
divisor0 = ""

for i in range(len(gx)):
    divisor0 += "0"
    
divisor1 = int(gx,2)
divisor0 = int(divisor0,2)
dividend = m_x[:len(gx)]
incr = 0
rng = (len(m_x) - len(gx)) + 1  # + 1 is for, after the last bit in m'x is used
                                # the loop stops, so to obtain final remainder
                                # it is added.

#***sender***

for i in range(rng):
    if (dividend[0] == '1'):
        divisor = divisor1
    else:
        divisor = divisor0

    dividend = int(dividend,2)
        
    remndr = bin(dividend^divisor).replace('b','')

    
    if(len(remndr) == len(gx)):
        remndr = list(remndr)
        remndr.pop(0)
        remndr = "".join(str(x) for x in remndr)   
                
    next_bit = len(gx) +  incr
    if(i != (rng - 1)):
        dividend = remndr+(m_x[next_bit])
        if(len(dividend) == 1):
            dividend = "000"+dividend
        elif(len(dividend) == 2):
            dividend = "00"+dividend
        elif(len(dividend) == 3):
            dividend = "0"+dividend
            

    incr += 1


#***genearteP(x)***


px = bin(int(m_x,2) ^ int(remndr,2))[2:]

print("Transmitted data :%s" % px)


#***reciever***

incr = 0
dividend = px[:len(gx)]
next_bit = 0
rng = (len(px) - len(gx)) + 1

for i in range(rng):
    if (dividend[0] == '1'):
        divisor = divisor1
    else:
        divisor = divisor0

    dividend = int(dividend,2)
        
    remndr = bin(dividend^divisor).replace('b','')

    
    if(len(remndr) == len(gx)):
        remndr = list(remndr)
        remndr.pop(0)
        remndr = "".join(str(x) for x in remndr)   
                
    next_bit = len(gx) +  incr
    if(i != (rng - 1)):
        dividend = remndr+(px[next_bit])
        if(len(dividend) == 1):
            dividend = "000"+dividend
        elif(len(dividend) == 2):
            dividend = "00"+dividend
        elif(len(dividend) == 3):
            dividend = "0"+dividend           
       

    incr += 1

#final result

if(int(remndr,2) == 0):
    print("Data received intact and its error free!!")
    print("The Original data: %s" % px[:len(mx)])
else:
    print("Data is corrupted!!")

















