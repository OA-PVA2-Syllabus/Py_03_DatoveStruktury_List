# Přiřazení je možné k řezům seznamů, stejně jako k jednotlivým prvkům seznamu.
# Tímto způsobem lze dokonce měnit velikost seznamu nebo jej zcela vymazat pomocí příkazu animals[:] = []

animals = ["elephant", "lion", "tiger", "giraffe", "monkey", "dog"]  # Vytvoření nového seznamu
print(animals)

animals[1:3] = ["cat"]    # Nahrazení 2 položek -- "cat" a "tiger" jednou položkou -- "cat".
print(animals)

animals[1:3] = []     # Odstranění 2 položek -- "cat" a "giraffe" ze seznamu
print(animals)

# Nahrazením posledních dvou položek vytvořte ze všech zvířat slony.
# Očekávaný výstup Lists: ['elephant', 'elephant', 'elephant']

print(animals)