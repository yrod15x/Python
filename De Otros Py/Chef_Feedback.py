import sys

bina = input()
good1 = '010'
good2 = '101'
c = 0

for i in bina:
    c += 1

if c < 3:
    print("BAD")
    sys.exit(1)


if bina.find(good1) == -1 or bina.find(good2) == -1:
    print('BAD')
else:
    print("GOOD")