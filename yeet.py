
#Converts text to hex
def EHEX(p):
    c = ''
    for i in p:
        c += hex(ord(i))[2:4]
    c = '0x' + c
    return c


#Adds padding
def PADG(x):
    x = x[2:]
    x += '1'
    while len(x)%40!=0:
        x += '0'
    n = bin(int(str((int(x, 16)**2))[8:-8]))[2:]
    n += '1'
    while len(n)%160!=0:
        n += '0'
    if len(n) < 640:
        n += n
    return n

#Binary Operators
def FXOR(b, a):
    if b == '1' and a == '0':
        return '1'
    elif b == '0' and a == '1':
        return '1'
    else:
        return '0'

def RNOT(a):
    if a == '0':
        return '1'
    else:
        return '0'
            

#Scrambles the message
def SCRM(b):
    t = ''
    #Makes each block size 40
    M = []
    t = ''
    for a in range(len(b)):
        if (a + 1)%(len(b)/160) == 0:
            t += b[a]
            M.append(t)
            t = ''
        else:
            t += b[a]
    hsh = ''
    for q in M:
        char = list(q)
        nt = ''
        for a in range(len(char)):
            char[a] = RNOT(FXOR(RNOT(FXOR(char[0] or char[a], char[0])) and RNOT(FXOR(char[1], RNOT(char[a]))), char[2]))
            char[0] = FXOR(FXOR(char[1] and char[a], char[1]) and FXOR(RNOT(char[2]), char[a]), char[0])
            char[1] = FXOR(FXOR(char[0] or char[a], char[0]) and FXOR(RNOT(char[3]), char[a]), char[1])
        hsh += FXOR(FXOR(FXOR(char[0], char[1]), FXOR(char[1], char[0])), RNOT(FXOR(FXOR(char[0], char[1]), RNOT(FXOR(char[1], char[2])))))
    return hsh
                
                
                
def ENCD(h):
    t = []
    q = ''
    for a in range(len(h)):
        if (a+1)%4==0:
            q += h[a]
            t.append(q)
            q = ''
        else:
            q += h[a]

    hashed = ''
    for i in t:
        if i == '0000':
            hashed += 'T'
        if i == '0001':
            hashed += 'E'
        if i == '0010':
            hashed += 'Y'
        if i == '0011':
            hashed += 'y'
        if i == '0100':
            hashed += 'e'
        if i == '0101':
            hashed += 't'
        if i == '0110':
            hashed += 'Ê'
        if i == '0111':
            hashed += 'Ë'
        if i == '1000':
            hashed += 'È'
        if i == '1001':
            hashed += 'ý'
        if i == '1010':
            hashed += 'Ý'
        if i == '1011':
            hashed += 'ë'
        if i == '1100':
            hashed += 'é'
        if i == '1101':
            hashed += 'è'
        if i == '1110':
            hashed += 'É'
        if i == '1111':
            hashed += 'ÿ'
    return hashed


def Yeet(text):
    return ENCD(SCRM(PADG(EHEX(text))))
    
            
# Y E T y e t Ê Ë È ý Ý ë é è É ÿ
# 16 characters
#length 40

