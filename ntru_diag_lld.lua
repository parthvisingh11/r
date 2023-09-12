  +--------------------------------------+
  |             Key Generation           |
  +--------------------------------------+
  |                                      |
  |   Decide on the public parameters    |
  |      (N, p, q)                       |
  |   Generate Polynomial f and g        |
  |   Calculate Inverse                  |
  |      Fq = f mod q                    |
  |      Fp = f mod p                    |
  |   Private Key (f, Fp)                |
  |   Calculate Public Key               |
  |      h = g.Fq (mod q)                |
  |                                      |
  +--------------------------------------+
                     |
                     V
  +--------------------------------------+
  |             Encryption               |
  +--------------------------------------+
  |                                      |
  |   Take a Message Polynomial m        |
  |   Choose a random small Polynomial r |
  |   Calculate Ciphertext Polynomial    |
  |      c = p.r.h + m (mod q)           |
  |                                      |
  +--------------------------------------+
                     |
                     V
  +--------------------------------------+
  |             Decryption               |
  +--------------------------------------+
  |                                      |
  |   Calculate s = f*c (mod q)          |
  |   Decrypt the Message Polynomial     |
  |      m = Fp.s (mod p)                |
  |                                      |
  +--------------------------------------+
