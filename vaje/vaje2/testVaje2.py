from Minpot import minpot

# Testni primeri
Input_list = [[[11, 14, 12, 6, 1, 2, 13, 6, 17, 3], [6, 12, 18, 18, 19, 11, 11, 6, 20, 7], [12, 8, 13, 10, 13, 3, 18, 14, 9, 5], [8, 6, 7, 6, 16, 17, 17, 20, 19, 13], [19, 17, 2, 14, 4, 18, 14, 19, 3, 6], [18, 16, 8, 12, 7, 17, 20, 6, 14, 2], [17, 5, 5, 3, 11, 16, 9, 20, 14, 9], [13, 8, 15, 15, 13, 4, 19, 11, 1, 7], [20, 20, 8, 6, 1, 17, 15, 19, 9, 13], [13, 2, 2, 5, 1, 2, 15, 2, 10, 4]]]


#pricakovane resitve testnih primerov
Output_list = [(40, [0, 4, 2, 5, 9, 1, 7, 8, 3, 6])]


#izracun posameznih rasitev
Result_list  = list()
for i in Input_list:
    res = minpot(i)
    Result_list.append(res)

# preverjanje resitev
Napaka = False
napake = list()
for j in range(len(Output_list)):
    if Output_list[j] != Result_list[j]:
        print("Ni ok",j)
        napake.append(j)
        Napaka = True

if not Napaka:
    print("Passed all the tests")
else:
    print("Zajebu si na primerih ostevilcenih z:",napake)
