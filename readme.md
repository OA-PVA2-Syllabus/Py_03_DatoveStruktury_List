# PVA2 - Programování a vývoj aplikací
## Cvičení 03: Datové struktury: Seznamy

### Obsah
1. List - úvod
2. Operace
3. Prvky
4. Vnořené seznamy
5. List - souhrn

### List - souhrn
#### 1
Vytvořte seznam `mocniny` s hodnotami `1,2,4,8,16,32`
1. Do seznamu `mocniny` přidejte pomocí vzorce druhé mocniny 6 a 7.
2. Odeberte první prvek 

#### 2
Napište program, který prohodí první prvek seznamu s třetím. Výsledek uložte do `result` a oba seznamy vytiskněte.
```
Vstupní data: 23, 65, 19, 90
Očekávaný výstup: 19, 65, 23, 90
```

#### 3
Napište program, který vytiskne seznam, jenž bude mít odstraněny 1, 4 a pátý prvek z seznamu.
```
Vstupní data: Red, Green, White, Black, Pink, Yellow
Očekávaný výstup: Green, White, Yellow
```

#### 4
`operation: 1456,5,98,4087,012,448,4,8,14,264,10,88,379,32,2971`

S využitím funkcí pro hledání extrémních hodnot napište program, který vrátí nejmenší a největší prvek v seznamu operation. Výsledek s popiskem vytiskněte uživateli.



#### 5
Pro seznam `operation` opět najděte nejmenší a největší prvek. Nalezněte jiný způsob než za požití funkcí pro hledání minima a maxima.


#### 6
Pro seznam `operation` prohodťe pořadí prvků tzn. první prvek bude poslední, druhý předposlední atd.


#### 7
`cars: ['Suzuki','Lamborghini','lexus', 'porsche', 'Ferrari', 'vojvo', 'chevrolet', 'DS', 'Jeep', 'Mini', 'Škoda']`

1. V seznamu cars nahraďte značku auta vojvo hodnotou `Volvo` 
2. Ze seznamu cars zkopírujte druhý až čtvrtý prvek do nového seznamu luxuryCars

#### 8
Najděte funkce, pomocí kterých provedete následující operace s seznamem:
1. Sečíst všechny prvky pole `operation`
2. Součet všech prvků pole operation uložte do proměnné `operationSum`
3. Vrátí z seznamu `cars` index auta _Ferrari_
4. Seřadí všechny prvky seznamu `cars`.

#### 9
Zamyslete/vyzkoušejte a popišete, co provede následující kód. Formou komentáře napište obsah seznamu `myList1` a `myList2`
```
myList1 = [1, 2, 3, 4]
myList2 = myList1 
print(myList1)
print(myList2)
myList1.append(5) 
```