favorite_pizzas = ["margarita",
                   "pepperoni",
                   "italian",]
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("special")
friend_pizzas.append("vegies")  

print("my favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"-{pizza}")
    
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"-{pizza}")
