def dec2bin(dec):
  if dec > 1:
    dec2bin(dec//2)
   print(dec % 2,end = '')
  
print(dec2bin(34)
