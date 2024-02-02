
city, temp = input().split()
minor, coldest = int(temp), city
 
while city != 'Waterloo':
    city, temp = input().split()
    if int(temp) < minor:
        minor = int(temp)
        coldest = city

print(coldest)
    