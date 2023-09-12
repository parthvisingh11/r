 -------------------
 |   Lattice basis   |
 -------------------
          |
          V
 ------------------------------
|   Apply LLL lattice reduction |
|   algorithm to find a short   |
|   vector in the lattice       |
 ------------------------------
          |
          V
 -----------------------------------------
|   Use the short vector to compute the    |
|   Gram-Schmidt orthogonalization of the  |
|   lattice basis                          |
 -----------------------------------------
          |
          V
 ------------------------------------------------------
|   Find the closest vector in the lattice to the      |
|   target vector using the LLL-reduced basis          |
 ------------------------------------------------------
          |
          V
 -------------------------------------------------------
|   Use the closest vector to find the secret functions |
 -------------------------------------------------------
