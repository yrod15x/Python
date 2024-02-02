import sys

max_bob = int(input())
max_limak = int(input())
bob_candies = 0
limak_candies = 0

while bob_candies < max_bob or limak_candies < max_limak:
    limak_candies = bob_candies + 1
    if limak_candies >= max_limak:
        print("Limak")
        break

    bob_candies = limak_candies + 1
    if bob_candies >= max_bob:
        print("Bob")
        break

