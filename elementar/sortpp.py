import math
import time


def p1():
    # Să se ordoneze crescător elementele pătrat perfect ale unui şir dat, fără a afecta elementele care nu sunt
    # pătrat perfect.
    my_list = [9, 15, 16, 4, 5, 1, 7, 9]

    for i in range(len(my_list)):  # cross the list with size of mylist
        index_left = 0
        while index_left < len(my_list):
            # check if left_index is a sqrt
            if round(math.sqrt(my_list[index_left])) * round(math.sqrt(my_list[index_left])) == my_list[index_left]:
                index_right = index_left + 1
                while index_right < len(my_list):
                    # check if second pair is a sqrt
                    if (round(math.sqrt(my_list[index_right])) * round(math.sqrt(my_list[index_right]))
                            == my_list[index_right]):
                        if round(math.sqrt(my_list[index_left])) > round(math.sqrt(my_list[index_right])):
                            temp = my_list[index_left]
                            my_list[index_left] = my_list[index_right]
                            my_list[index_right] = temp
                            index_left += 1  # found a sqrt pair for left we continue with next left
                            break
                        else:
                            index_right += 1
                    else:  # if second pair is not sqrt go and find next second pair
                        index_right += 1
                index_left += 1
            else:
                index_left += 1

    print("Rezultat problema nr. 1: {}".format(my_list))


def p2():
    children = [8, 20, 16, 14, 10, 4, 12]
    children_order_nr = []

    for i in range(len(children)):
        children_order_nr.append(i + 1)

    for i in range(len(children)):
        for j in range(len(children)):
            next_index = j + 1
            if next_index < len(children):
                if children[j] > children[next_index]:
                    temp = children[j]
                    children[j] = children[next_index]
                    children[next_index] = temp
                    temp2 = children_order_nr[j]
                    children_order_nr[j] = children_order_nr[next_index]
                    children_order_nr[next_index] = temp2

    print("Rezultat problema nr. 2: {}".format(children_order_nr))


def p3():
    numbers = [24, 46, 11, 36, 48, 35, 27, 28, 49, 6]
    # numbers = [46]
    dividers = []

    # Dacă două numere au aceeași sumă a divizorilor, se va afișa mai întâi cel mai mic
    for i in range(len(numbers)):  # order the numbers ASC, prepare for next step
        for j in range(len(numbers)):
            next_index = j + 1
            if next_index < len(numbers):
                if numbers[j] > numbers[next_index]:
                    temp = numbers[j]
                    numbers[j] = numbers[next_index]
                    numbers[next_index] = temp
    # suma divizorilor
    for i in range(len(numbers)):
        index = 1
        total = 0
        while math.pow(index, 2) <= numbers[i]:
            if numbers[i] % index == 0:
                total += (numbers[i] / index)
                # Ex: 49:7=7 so we will not sum the 7 twice it represent only one divider.
                if numbers[i] / index != index:
                    total += index
            index += 1
        dividers.append(total)

    # order the final numbers based on the dividers total sum
    for i in range(len(dividers)):
        for j in range(len(dividers)):
            next_index = j + 1
            if next_index < len(dividers):
                if dividers[j] > dividers[next_index]:
                    temp = dividers[j]
                    dividers[j] = dividers[next_index]
                    dividers[next_index] = temp
                    temp2 = numbers[j]
                    numbers[j] = numbers[next_index]
                    numbers[next_index] = temp2

    print("Rezultat problema nr. 3: {}".format(numbers))


# Se citește de la tastură un număr natural n, apoi n numere naturale.
# Să se afişeze cel mai mic număr care poate fi scris folosind prima cifră a numerelor citite.
def p4():
    n = 5
    numbers = [100, 312, 276, 985, 5021]
    result = []

    # convert int number in string and then back to nr
    # Ex: 1234 --> str(12234) --> extract first element from string "1" --> convert the element found to int to sort.

    # check first input condition
    if n < 0 or n >= 1000:
        print("Numarul nu corespunde datelor de intrare cerute")
        exit()
    # check second input condition
    for i in range(len(numbers)):
        if numbers[i] > 1_000_000_000:
            print("Numarul introdus corespunde datelor de intrare cerute")
            exit()

    # extract the first element from a number
    for i in range(len(numbers)):
        result.append(int(str(numbers[i])[0]))
    # Sort the found numbers
    for i in range(len(result)):
        for j in range(len(result)):
            next_index = j + 1
            if next_index < len(result):
                if result[j] > result[next_index]:
                    temp = result[j]
                    result[j] = result[next_index]
                    result[next_index] = temp
    # concatenate the numbers into a final string
    final_nr = ""
    for i in range(len(result)):
        final_nr += str(result[i])

    print("Rezultat problema nr. 4: {}".format(final_nr))


# Se citește de la tastatură un număr natural n, apoi n numere naturale.
# Să se afişeze cel mai mic număr care poate fi scris folosind cifra minimă a fiecărui număr citit.
def p5():
    n = 5
    numbers = [100, 312, 276, 985, 5021]
    result = []
    # check first input condition
    if n < 0 or n >= 1000:
        print("Numarul nu corespunde datelor de intrare cerute")
        exit()
    # check second input condition
    for i in range(len(numbers)):
        if numbers[i] > 1_000_000_000:
            print("Numarul introdus corespunde datelor de intrare cerute")
            exit()
    # traverse each number from the list
    for i in range(len(numbers)):
        minim = []
        number = str(numbers[i])  # convert to string to be able to extract the digits and to compose a list
        # compose a new list with each digit from a number
        for j in range(len(number)):
            minim.append(int(number[j]))  # reconvert any digit to int, to be much easier to work with it
        # find the minim digit from the number
        lowest_number = minim[0]  # initialize the min number with first element from list
        for j in range(1, len(minim)):  # run a for cycle starting with second element from the list
            if minim[j] < lowest_number:
                lowest_number = minim[j]
        result.append(lowest_number)  # add the lowest digit number into the result

    lowest_number = 99999999999
    lowest_number_index = -1
    for j in range(len(result)):  # find the lowest digit, need to avoid any possible wrong solution like [00]123
        if lowest_number > result[j] > 0:
            lowest_number = result[j]
            lowest_number_index = j

    result.remove(lowest_number_index)  # remove the first min element found from original result

    final_result = [lowest_number]
    for j in range(len(result)):
        final_result.append(result[j])  # populate the new list with all remaining digits

    for i in range(1, len(final_result)):  # final sorting we always exclude digit from position [0] of the list
        for j in range(1, len(final_result)):
            next_index = j + 1
            if next_index < len(final_result):
                if final_result[j] > final_result[next_index]:
                    temp = final_result[j]
                    final_result[j] = final_result[next_index]
                    final_result[next_index] = temp

    # concatenate the numbers into a final string
    final_nr = ""
    for i in range(len(final_result)):
        final_nr += str(final_result[i])

    print("Rezultat problema nr. 5: {}".format(final_nr))


# În baza de date a unui magazin online există n produse. Fiecare are un cod numeric, alcătuit din cel mult nouă
# cifre, cu următoarea semnificație:
#
# prima cifră reprezintă categoria produsului; a doua cifră reprezintă starea produsului – pară pentru produsele
# existente pe stoc și impară pentru cele cu stoc epuizat; restul cifrelor din cod reprezintă identificatorul
# produsului. Cerința
#
# Se dau cele n coduri ale produselor din baza de date.
#
# 1) Determinați câte produse există pe stoc și câte au stoc epuizat.
# 2) Pentru fiecare categorie, determinați lista produselor, în ordinea crescătoare a codurilor numerice.
#
# Date de intrare Fișierul de intrare produse.in conține pe prima linie numerele c n, iar pe a doua linie n numere
# naturale, separate prin spații, reprezentând codurile produselor.
#
# Date de ieșire Dacă c=1, fișierul de ieșire produse.out va conține pe prima linie numerele S E, separate printr-un
# un spațiu, reprezentând numărul de produse existente pe stoc, respectiv numărul de produse cu stoc epuizat.
#
# Dacă c=2, fișierul de ieșire produse.out va conține mai multe linii, câte una pentru fiecare categorie de produs,
# în ordinea crescătoare a acestora. Fiecare linie începe cu categoria, urmată de un spațiu, apoi de codurile
# produselor din acea categorie, în ordine crescătoare, separate și ele prin câte un spațiu.
#
# Restricții și precizări
# 1 ≤ n ≤ 1000;
# cele n coduri vor fi mai mari decât 99 și mai mici decât 1.000.000.000;
# pentru 30% din teste, c=1.
# Exemplul 1
# produse.in
#
# 1 5
# 15123 24897 4217 142 2736
# produse.out
#
# 3 2
# Explicație
# Produsele existente pe stoc au codurile 24897 4217 142, iar cele cu stoc epuizat au codurile 15123 2736.
#
#
# Exemplul 2
# produse.in
#
# 2 5
# 15123 24897 4217 142 2736
# produse.out
#
# 1 142 15123
# 2 2736 24897
# 4 4217
def p6():
    print("Rezultat problema nr. 6:")
    c = 2
    n = 5
    my_list = [15123, 24897, 4217, 142, 2736]

    if c == 1:
        stock = 0
        out_stock = 0
        for i in range(len(my_list)):
            if int(str(my_list[i])[1]) % 2 == 0:
                stock += 1
            else:
                out_stock += 1
        print("{} {}".format(stock, out_stock))
    else:
        while len(my_list) > 0:
            # traverse the my_list till will be empty. We have "my_list.pop(j)" (see bellow) which will remove the
            # data is already checked

            result = []
            # always first element from list will contain the next search category number
            search_category = int(str(my_list[0])[0])  # first digit is the category

            j = 0
            while j < len(my_list):
                # traverse "my_list" and find the product numbers for the search_category and remove the "my_list[j]"
                # number from the "my_list"
                category_found = int(str(my_list[j])[0])  # first digit is the search_category
                if category_found == search_category:
                    number_string = str(my_list[j])
                    product_nr = ""
                    for k in range(1, len(number_string)):  # compose the product number
                        product_nr += number_string[k]
                    result.append(int(product_nr))  # added to the result the product nr without search_category number
                    my_list.pop(j)  # remove the element from original list already added to result
                else:
                    j += 1

            for z in range(len(result)):  # Sort the product numbers from "search_category"
                for k in range(len(result)):
                    next_index = k + 1
                    if next_index < len(result):
                        if result[k] > result[next_index]:
                            temp = result[k]
                            result[k] = result[next_index]
                            result[next_index] = temp

            products = ""
            for k in range(len(result)):
                products += str(search_category) + str(result[k]) + " "  # final arrangement to display the results

            print("{} {}".format(search_category, products))


# Se dă un vector cu n elemente numere întregi, n fiind număr par.
#
# Cerinţa
# Să se ordoneze crescător elementele din prima jumătate a vectorului și descrescător elementele din a doua jumătate.
#
# Date de intrare Fişierul de intrare halfsort.in conţine pe prima linie numărul n si pe a doua linie n numere
# întregi separate prin spaţii.
#
# Date de ieşire Fişierul de ieşire halfsort.out va conţine pe prima linie cele n elemente ale vectorului,
# ordonate conform cerinței, separate printr-un spațiu.
#
# Restricţii şi precizări
# 1 ≤ n ≤ 100, n număr par
# valoarea absolută a numerelor de pe a doua linie a fişierului de intrare va fi mai mică decât 1.000.000.000
# Exemplu:
#
# halfsort.in
#
# 6
# 8 2 9 4 5 7
# halfsort.out
#
# 2 8 9 7 5 4
def p7():
    my_list = [8, 2, 9, 4, 5, 7]
    half_index = round(len(my_list) / 2)  # split the vector in half
    for i in range(0, half_index):  # sort the first half of the vector
        for j in range(0, half_index):
            next_index = j + 1
            if next_index < half_index:
                if my_list[j] > my_list[next_index]:
                    temp = my_list[j]
                    my_list[j] = my_list[next_index]
                    my_list[next_index] = temp
    for i in range(half_index, len(my_list)):  # sort the second half of the vector
        for j in range(half_index, len(my_list)):
            next_index = j + 1
            if next_index < len(my_list):
                if my_list[j] < my_list[next_index]:
                    temp = my_list[j]
                    my_list[j] = my_list[next_index]
                    my_list[next_index] = temp

    print("Rezultat problema nr. 7: {}".format(my_list))


# Scrie un program care citind un șir de numere naturale afișează numerele citite ordonate crescător după suma
# cifrelor lor, iar dacă suma cifrelor este egală, descrescător după valoarea lor.
#
# Date de intrare
# Fișierul de intrare sortsum.in conține pe prima linie numere naturale separate prin spații.
#
# Date de ieșire
# Fișierul de ieșire sortsum.out va conține pe prima linie numerele ordonate conform cerinței.
#
# Restricții și precizări
# în fișier vor fi mai puțin de 1.000.000 de numere
# numerele din fișierul de intrare vor fi mai mici decât 10.000.000
# Exemplu:
#
# sortsum.in
#
# 102 60 51 600 21 3
# sortsum.out
#
# 102 21 3 600 60 51 Explicație Numerele 102, 21 și 3 au suma cifrelor 3, iar 600, 60, 51 au suma cifrelor 6. Mai
# întâi se afișează numerele ce au suma cifrelor cea mai mică (3), în ordine descrescătoare, apoi cele care au suma
# cifrelor 6, tot în ordine descrescătoare.
def p8():
    my_list = [102, 60, 6, 51, 600, 21, 3]

    sum_list = []
    for i in range(len(my_list)):  # go through each number
        number = str(my_list[i])  # get the current number as a string
        total = 0
        for j in range(len(number)):  # traverse each digit from the number
            total += int(number[j])
        sum_list.append(total)  # populate a new vector with the sum of all digits for a number

    for i in range(len(sum_list)):  # sort the numbers based and mapped to the sum_list
        for j in range(len(sum_list)):
            next_index = j + 1
            if next_index < len(sum_list):
                if sum_list[j] > sum_list[next_index]:
                    temp = sum_list[j]
                    sum_list[j] = sum_list[next_index]
                    sum_list[next_index] = temp
                    temp2 = my_list[j]
                    my_list[j] = my_list[next_index]
                    my_list[next_index] = temp2

    start_index_group = 0
    stop_index_group = start_index_group + 1
    while start_index_group < len(sum_list):  # exit when start_index_group reach the end of the vector list
        # need to find the start and stop indexes of intervals where we will order DESC the numbers
        # having the same SUM(digit_numbers)
        while stop_index_group < len(sum_list) and sum_list[start_index_group] == sum_list[stop_index_group]:
            stop_index_group += 1
        # after I found the start and stop I will proceed forward with the DESC sorting
        # Ex: (102, 21, 3,....) --> (3, 3, 3,....) --> start=0 stop 3
        for i in range(start_index_group, stop_index_group):  # sort the first half of the vector
            for j in range(start_index_group, stop_index_group):
                next_index = j + 1
                if next_index < stop_index_group:
                    if my_list[j] < my_list[next_index]:
                        temp = my_list[j]
                        my_list[j] = my_list[next_index]
                        my_list[next_index] = temp
        # after the sorting was done proceed forward to find the NEXT start and stop indexes
        start_index_group = stop_index_group
        stop_index_group += 1

    print("Rezultat problema nr. 8: {}".format(my_list))


# Cerința Se dă un vector cu n elemente, numere naturale. Afișați în ordine crescătoare elementele iar după fiecare
# element, inserați indicele poziției pe care acesta se afla înainte ca vectorul să fie sortat.
#
# Daca există mai multe elemente cu aceeași valoare, indicii acestora se vor afișa în ordine crescatoare.
#
# Date de intrare
# Programul citește de la tastatură numărul n, iar apoi n numere naturale, separate prin spații.
#
# Date de ieșire
# Programul va afișa pe ecran șirul de numere separate prin spatiu, respectând cerința cerută.
#
# Restricții și precizări
# 1 ≤ n ≤ 100
# cele n numere citite vor fi mai mici decât 1.000.000.000
# numerotarea vectorului începe de la 1
# Exemplu:
#
# Intrare
#
# 7
# 12 8 9 0 19 2 8
# Ieșire
#
# 0 4 2 6 8 2 8 7 9 3 12 1 19 5 Explicație Vectorul sortat este 0 2 8 8 9 12 19; Fostele poziții sunt 4 pentru 0 ; 6
# pentru 2 etc. Elementul 8 apare de două ori, o dată pe poziția 2 și o dată pe poziția 7. Astfel încât, indicii se
# afișează crescător : 8 2 8 7
def p9():
    my_list = [12, 8, 9, 0, 19, 2, 8]
    index_list = []
    for i in range(len(my_list)):
        index_list.append(i)

    # sort the vector with numbers and also maintain the old index positions of index_list
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            next_index = j + 1
            if next_index < len(my_list):
                if my_list[j] > my_list[next_index]:
                    temp = my_list[j]
                    my_list[j] = my_list[next_index]
                    my_list[next_index] = temp
                    temp2 = index_list[j]
                    index_list[j] = index_list[next_index]
                    index_list[next_index] = temp2

    start_index_group = 0
    stop_index_group = start_index_group + 1
    while start_index_group < len(my_list):  # exit when start_index_group reach the end of the vector list
        # need to find the start and stop indexes of intervals where we will order DESC the numbers
        # having the same SUM(digit_numbers)
        while stop_index_group < len(my_list) and my_list[start_index_group] == my_list[stop_index_group]:
            stop_index_group += 1

        # after I found the start and stop I will proceed forward with the ASC sorting
        # Ex: (8, 8, ...) --> (7, 2,....) --> start=X stop=Y
        for i in range(start_index_group, stop_index_group):  # sort the first half of the vector
            for j in range(start_index_group, stop_index_group):
                next_index = j + 1
                if next_index < stop_index_group:
                    if index_list[j] > index_list[next_index]:  # sort by indexes
                        temp = index_list[j]
                        index_list[j] = index_list[next_index]
                        index_list[next_index] = temp
                        temp2 = my_list[j]
                        my_list[j] = my_list[next_index]
                        my_list[next_index] = temp2

        # after the sorting was done proceed forward to find the NEXT start and stop indexes
        start_index_group = stop_index_group
        stop_index_group += 1

    # Final arrangement to output the result exactly how it was required.
    result = ""
    for i in range(len(my_list)):
        result += "{} {} ".format(my_list[i], index_list[i] + 1)
    print("Rezultat problema nr. 9: {}".format(result))


if __name__ == '__main__':
    start_time = time.time()
    # probleme cu liste de dificultate usoara de clasa a 9 de la orele de informatica de la liceul Unirea (Sara Chirila)
    p1()
    p2()
    p3()
    p4()
    p5()
    p6()
    p7()
    p8()
    p9()

    end_time = time.time()
    print("Execution time: {} seconds".format((end_time - start_time)))

#     children[45, 65, 78, 100, 7, 78]
