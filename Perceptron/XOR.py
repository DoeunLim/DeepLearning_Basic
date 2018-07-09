def XOR(x1, x2):
   s1 = NAND(x1, x2)
   s2 = OR(x1, x2)
   y = AND(s1, s2)
   return y
