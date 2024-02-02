num_acciones, salud = input().split()

num_acciones, salud = int(num_acciones), int(salud)
salud_char, salud_bot = salud, salud
char_acciones, bot_acciones = [],[]
char_ataq, bot_ataq = [], []
acciones, ataques = [], []
resultado = True

for i in range(num_acciones * 2):
    acc, ataq = input().split()
    if i < num_acciones:
        char_acciones.append(acc)
        char_ataq.append(int(ataq))
    else:
        bot_acciones.append(acc)
        bot_ataq.append(int(ataq))
        
for i in range(num_acciones):
    acciones.append(char_acciones[i])
    acciones.append(bot_acciones[i])
    ataques.append(char_ataq[i])
    ataques.append(bot_ataq[i])

dodge = False 

for i in range(len(acciones)):         
    if i % 2 == 0:
        if acciones[i] == "A":
            if not(dodge):
                salud_bot -= ataques[i]
            else:
                dodge = False 
        else: 
            if dodge:
                salud_bot -= ataques[i-1]
            else:
                dodge = True 
    else:
        if acciones[i] == "A":
            if not(dodge):
                salud_char -= ataques[i]
            else:
                dodge = False
        else:
            if dodge:
                salud_char -= ataques[i-1]
            else:
                dodge = True 
                
    if salud_bot <= 0:
        print('VICTORY')
        resultado = False
        break
    elif salud_char <= 0:
        print("DEFEAT")
        resultado = False
        break
        
if resultado:
    if acciones[len(acciones) - 1] == 'D':
        salud_bot -= ataques[len(acciones) - 1]
    else:
         salud_char -= ataques[len(acciones) - 1]
         
    if salud_bot <= 0:
        print('VICTORY')
    elif salud_char <= 0:
        print("DEFEAT")
    else:
        print('TIE')    
