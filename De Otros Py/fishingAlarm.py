depths = []
alarms = ''

for i in range(4):
    depths.append(int(input()))

if depths.count(depths[0]) == 4:
    print('Fish At Constant Depth')
else:
    for i in range(3):
        if depths[i] < depths[i+1]:
            alarms += 'r'
        elif depths[i] > depths[i + 1]:
            alarms += 'd'
    if alarms == 'rrr':
        print('Fish Rising')
    elif alarms == 'ddd':
        print('Fish Diving')
    else:
        print('No Fish')


            
        

        
    

        
    

    