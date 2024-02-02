l1 = int(input())
l2 = int(input())
l3 = int(input())

lista = []


vote = 0
total = l1 + l2 + l3

for i in range(0, total):
    vote = int(input())
    lista.append(vote)

lista.sort()
final_list = []
flag = False
c = 0

for i in range(0, total - 1):
    if lista[i] == lista[i+1]:
        final_list.append(lista[i])
        c += 1

real_voters = []

final_list.sort()

for i in final_list: #
    if i not in real_voters:
        real_voters.append(i)

print(real_voters.count())
for j in real_voters:
    print(j)





