from fractions import Fraction
import random
from poly import *
from util import *

# Multiplication f*g in Z[X]/(X^N - 1)
def ntrumul(f, g, N):
    """
    f = poly([2, 5])
    g = poly([4, 3])
    ntrumul(f, g, 3) == f*g % poly([-1, 0, 0, 1])
    >>> True

    where f*g % poly([-1, 0, 0, 1]) means f*g mod (X^3 - 1)
    """
    fg = []
    for j in range(N):
        s = 0
        for i in range(N):
            s = s + f[i]*g[(-i+j)%N]
        fg.append(s)
    return poly(fg)

def lift(x, p):
    """
    Function returns the polynomial 
    coefficients lie between -p/2 and p/2 (centered lift)

    lift(poly([1, 2, 3, 4, 5, 6]), 5)
    >>> poly([1, 2, -2, -1, 0, 1])
    """
    a = []
    for i in x:
        if i>p//2:
            a.append(i - p)
        else:
            a.append(i)
    return poly(a)

def L(d1, d2, N):
    """
    Function to create a polynomial degree N-1 that
    d1 coefficients equal 1, d2 coefficients equal -1, the rest 0.

    >>> L(1, 1, 5)
    poly([1, -1, 0, 0, 0])
    """

    l = [1]*d1 + [-1]*d2 + [0]*(N-d1-d2)
    out = []
    for i in range(N):
        j = random.randrange(0, N-i)
        out.append(l.pop(j))
    return poly(out)

# Function to generate the publickey
def genPublickey(f, g, N=5, p=3, q=128):
    fq = polyinv(f, poly([-1]+[0]*(N-1)+[1]))%q
    h = ntrumul(fq, g, N)%q
    return h

def enc(m, h, N=5, p=3, q=128):
    r = L(3, 3, 5)
    return (ntrumul(p*r, h, N) + m)%q

def dec(e, f, N=7, p=3, q=128):
    a = lift(ntrumul(f, e, N)%q, q)
    fp = polyinv(f, poly([-1]+[0]*(N-1)+[1]))%p
    return lift(ntrumul(fp, a, N)%p, p)

def prepare_encryp(message, h, N, p, q):
    message = str_to_binary_stream(str(message))
    ciphertext = []
    for mess in message:
        m = poly(mess)
        print('PlainText  m: ', m)

        # Encryption
        e = enc(m, h, N, p, q)
        print('Ciphertext e: ', e, ' ( = enc(m, h))')
        ciphertext.append(e)
    return ciphertext    

def output(out):
    out = [i.coef for i in out]
    #print(out)
    for i in range(len(out)):
        out[i] = [str(j) for j in out[i]]
    #print(out)
    out = ["".join(i) for i in out]
    #print(out)
    for i in range(len(out)):
        while(len(out[i]) < 8):
            out[i] = out[i] + '0'
    out = [i[::-1] for i in out]
    #print(out)
    out = [chr(int(i, 2)) for i in out]
    return "".join(out)

def prepare_decrypt(ciphertext, f, N, p, q):
    decryp_message = []
    for c in ciphertext:
        m = dec(c, f, N, p, q)
        print('PlainText  m: ', m, ' ( = dec(e, f))')
        decryp_message.append(m)
    return output(decryp_message)

def prepare_attack(ciphertext, f, N, p, q):
    decryp_message = []
    for c in ciphertext:
        NTRULattice = nl(h.coef, q)
        Lh = intmat(lll(NTRULattice))
        F, G = Lh[0][:len(Lh)//2], Lh[0][len(Lh)//2:]
        decryp_message.append(dec(m, poly(F)))
        for i in range(len(h)+1):
            if f == poly(F).rot(i):
                sign = 1
                break
            if f == -poly(F).rot(i):
                sign = -1
                break
        print('Rotation of F is equal to private key f')
        print('f = ', sign, '*x^', i, '*F')
    return output(decryp_message)
