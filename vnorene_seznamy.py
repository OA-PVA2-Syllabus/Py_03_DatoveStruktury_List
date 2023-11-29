# Seznam může obsahovat libovolné objekty, dokonce i jiné seznamy (podseznamy). Tato datová struktura se nazývá vnořený seznam.

# Vnořené seznamy můžete použít k uspořádání dat do hierarchických struktur.

# Vnořený seznam lze vytvořit zápisem posloupnosti podseznamů oddělených čárkou:

# Vnořený_seznam = [[1, 2, 3], [4, 5], 6]
# K položkám vnořeného seznamu můžete přistupovat pomocí indexů stejně jako dříve:

#print(nested_list[1])
#print(nested_list[2])
#Výstup:

#[4, 5]
#6
#K položkám v rámci vnořených seznamů můžete přistupovat pomocí více indexů. Pro přístup k číslu 1 z vnořeného_seznamu použijte dvakrát index 0. Nejprve přistupujete k prvku [1,2,3] a poté k prvnímu prvku tohoto vnořeného seznamu:

#print(nested_list[0][0])
#Výstup:

#1
# Použijte indexování pro přístup k prvkům 9 a 10 z vnořeného seznamu my_list a vypište je.

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 10]

print('Print number 9 from the nested list: ')
???


print('Print number 10 from the nested list: ')
???