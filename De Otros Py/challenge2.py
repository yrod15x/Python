alfabet = "g fmnc wms bgblr rpylqjyrc gr zw fylb . rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
frase = []

for i in range(0, len(alfabet)):
    if alfabet[i] < chr(97) or alfabet[i] > chr(97 + 26):
        frase.append(ord(alfabet[i]))
    elif alfabet[i] == "y":
        frase.append(97)
    elif alfabet[i] == "z":
        frase.append(98)
    else:
        frase.append(ord(alfabet[i]) + 2)

for j in frase:
    print(chr(j), end='')
