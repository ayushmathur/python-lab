# Author- Ayush Mathur
"""In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter 
in the plain text is replaced by a letter some fixed number of positions down the alphabet. 
For example, with a shift of 3, A would be replaced by D, B would become E, and so on. 
The method is named after Julius Caesar, who used it to communicate with his generals. 
ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13. 
In Python, the key for ROT-13 may be represented by means of the following dictionary:
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 
'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c','q':'d', 'r':'e', 's':'f', 
't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 
'D':'Q', 'E':'R', 'F':'S', 'G':'T','H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 
'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 
'X':'K', 'Y':'L', 'Z':'M'}
Your task in this exercise is to implement an encoder/decoder of ROT-13. 
Once you're done, you will be able to read the following secret message:
Pnrfnepvcure? V zhpucersrePnrfnefnynq!
Note that since English has 26 characters, your ROT-13 program will be able to 
both encode and decode texts written in English."""
##################################################################################################

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key={} # initializing dictionary
for i in range(0,26):  #Interate alphabets and assign key value pair. Value is i+13 th value.
    key[alphabet[i]] = alphabet[(i+13)%26]                  # Assigning 13th alphabet from current one as key value pair 
    key[alphabet[i].upper()] = key[alphabet[i]].upper()     # Also assign upper case letters.

encrypted=input("Enter the string to be decode/encode: ")   # Asking user for string
decrypted=''                                                # Initializing Resulting string variable
for x in encrypted:                                         # Loop to iterate and replace characters
    if x in key:                                            # from the key
        decrypted=decrypted+key[x]
    else:
        decrypted=decrypted+x
print("Decoded string: "+decrypted)