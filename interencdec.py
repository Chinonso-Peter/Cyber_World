import sys

alaphabets = "wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}"
str(alaphabets)
for c in alaphabets:
    if c.isalpha() and c.isupper():
        code = ord(c)
        # doing a shift of 19 
        code += 19
        if code > 90:
            code = (code - 26)
        
        sys.stdout.write(chr(code))
    elif c.isalpha() and c.islower():
        code = ord(c)
        #doing a shift of 19
        code += 19
        if code > 122:
            code = (code - 26)
        
        sys.stdout.write(chr(code))
    else:
        sys.stdout.write(c)
