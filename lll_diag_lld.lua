 ----------------------------
 |   Lattice basis as matrix  |
 ----------------------------
              |
              V
 ----------------------------------------------
|   Compute Gram-Schmidt orthogonalization   |
|   of the matrix                            |
 ----------------------------------------------
              |
              V
 ---------------------------------------
|   Initialize LLL algorithm with the  |
|   orthogonalized matrix and a delta  |
 ---------------------------------------
              |
              V
 --------------------------------------------------------
|   Run LLL algorithm to reduce the matrix and find a    |
|   short vector in the lattice                          |
 --------------------------------------------------------
              |
              V
 ----------------------------------------------
|   Use the short vector to compute a new    |
|   basis for the lattice                    |
 ----------------------------------------------
              |
              V
 --------------------------------------------------------
|   Find the closest vector in the lattice to the      |
|   target vector using the new basis                  |
 --------------------------------------------------------
              |
              V
 --------------------------------------------------------------
|   Use the closest vector to solve for the secret polynomials |
 --------------------------------------------------------------
