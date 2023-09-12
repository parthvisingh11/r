from lll import *
from ntru import *
from util import *

"""
Ntru parameters: (N, p, q) = (5, 3, 128)
Private key: f = x^4 + x^3 - 1 = poly([-1, 0, 0, 1, 1])
             g = x^3 - x = poly([0, -1, 0, 1])
Message : m = -x^4 + x^2 + x - 1

"""

# NTRU parameter
(N, p, q) = (7, 3, 128)
print('Parameters  :  (N, p, q) = ', (N, p, q))

# Private key
f = poly([-1, 0, 0, 1, 1])
g = poly([0, -1, 0, 1])
print('PrivateKey f: ', f)
print('PrivateKey g: ', g)

# Public key
h = genPublickey(f, g, N, p, q)
print('PublicKey  h: ', h, ' ( = genPublickey(f, g))')

# Message
message = "HELLO"
message = str_to_binary_stream(message)
print('Message    : ', message)
out = []
for mess in message:
    m = poly(mess)
    print('PlainText  m: ', m)

    # Encryption
    e = enc(m, h, N, p, q)
    print('Ciphertext e: ', e, ' ( = enc(m, h))')

    #Decryption
    print('Decryption  : ', dec(e, f, N, p, q), ' ( = dec(e, f))')
    print('>>> dec(m, f) == m')
    print(dec(m, f) == m)

    #Lattice attack
    print('-----------------Lattice Attack----------------------')
    print('The vector [f, g] is in the NTRU lattice ')
    NTRULattice = nl(h.coef, q)
    print(np.array(NTRULattice))

    print('Aplying LLL to NTRU Lattice ')
    Lh = intmat(lll(NTRULattice))
    print(np.array(Lh))

    print('The first row vector [F, G]: ')
    F, G = Lh[0][:len(Lh)//2], Lh[0][len(Lh)//2:]
    print('F, G = ', F, G)

    print('Decrypt massege')
    print('>>> dec(m, poly(F))')
    print(dec(m, poly(F)))
    print('>>> dec(m, poly(F)) == m')
    print(dec(m, poly(F)) == m)

    out.append(dec(m, poly(F)))

    for i in range(len(h)+1):
        if f == poly(F).rot(i):
            sign = 1
            break
        if f == -poly(F).rot(i):
            sign = -1
            break
    print('Rotation of F is equal to private key f')
    print('f = ', sign, '*x^', i, '*F')

#convert all the elements of out to string
out = [i.coef for i in out]
print(out)
for i in range(len(out)):
    out[i] = [str(j) for j in out[i]]
print(out)
out = ["".join(i) for i in out]
print(out)
for i in range(len(out)):
    while(len(out[i]) < 8):
        out[i] = out[i] + '0'
#convert the elements of out to binary
#out = [int(i, 2) for i in out]
#convert the elements of out to ascii
#reverse all the elements of out
out = [i[::-1] for i in out]
print(out)
out = [chr(int(i, 2)) for i in out]
print("".join(out))

# if __name__ == '__main__':
#     import code
#     console = code.InteractiveConsole(locals=locals())
#     console.interact()