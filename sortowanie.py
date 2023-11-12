#! python3

import random
import sys

przykladowa_lista = [8, 9, 3, 1, 10, 6, 4, 2, 5, 7, 11]
losowa_lista = random.sample(range(1, 100), random.randint(5, 20))


def printhelp() -> None:
    '''Wypisuje pomoc'''
    print(
        """sortowanie.py - Pokazuje działanie wybranych algorytmów sortowania

Użycie: sortowanie.py [OPCJE] liczba1, liczba2, liczba3...

Opcje:
    -a         sortowanie bąbelkowe (domyślne)
    -b         sortowanie szybkie
    -c         sortowanie przez scalanie
    -d         sortowanie przez wybieranie
    -e         sortowanie przez wstawianie)"""
    )


def sort_babelkowe(lista: list[int]) -> list[int]:
    """Implementacja algorytmu sortowania bąbelkowego"""
    print("SORTOWANIE BĄBELKOWE\n")
    nr_iteracji = 1

    for i in range(len(lista) - 1, 0, -1):
        poprzednia_lista = lista.copy()

        if nr_iteracji < 4:
            print("Iteracja " + str(nr_iteracji) + ":")

        for j in range(i):
            if i > (len(lista) - 4):
                liczba, nastepna_liczba = lista[j], lista[j + 1]
                lista[j] = "[" + str(liczba)
                lista[j + 1] = str(nastepna_liczba) + "]"
                printlist(lista)
                lista[j], lista[j + 1] = liczba, nastepna_liczba

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

        # Porównuje obecną iterację z poprzednią. Jeśli nie dokonano zmian, przerywa algorytm.
        tablice_rowne = True
        for k in range(len(lista)):
            if lista[k] != poprzednia_lista[k]:
                tablice_rowne = False
                break
        if tablice_rowne:
            print("Gotowe!")
            break

        if nr_iteracji == 4:
            print("I tak dalej...")

        printlist(lista)

        if i > (len(lista) - 4):
            print()

        nr_iteracji += 1

    return lista


def sort_szybkie(lista: list[int], l: int = 0, p: int = None) -> list[int]:
    """Implementacja algorytmu sortowania szybkiego"""

    def printlista_sort_szybkie(
        lista: list[int], l_liczba: int, srodek: int, p_liczba: int
    ) -> None:
        lista1 = lista.copy()
        srodek = "|" + str(srodek) + "|"
        lista1[(l + p) // 2] = srodek
        lista1[i] = "[" + str(l_liczba) + "]"
        lista1[j] = "[" + str(p_liczba) + "]"
        printlist(lista1)

    print("SORTOWANIE SZYBKIE\n")

    if p is None:
        p = len(lista) - 1
    i, j = l, p
    pivot = lista[(l + p) // 2]
    print("pivot: " + str(pivot))

    while i <= j:
        while lista[i] < pivot:
            printlista_sort_szybkie(lista, lista[i], pivot, lista[j])

            i += 1

        while lista[j] > pivot:
            printlista_sort_szybkie(lista, lista[i], pivot, lista[j])

            j -= 1

        if i <= j:
            printlista_sort_szybkie(lista, lista[i], pivot, lista[j])

            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1

    if l < j:
        print("Lewa strona")
        sort_szybkie(lista, l, j)
    if p > i:
        print("Prawa strona")
        sort_szybkie(lista, i, p)

    return lista


def sort_przez_scalanie(lista):
    pass


def sort_przez_wybieranie(lista):
    pass


def sort_przez_wstawianie(lista):
    pass


def printlist(lista: list[int], end="\n") -> None:
    """Wypisuje listę bez nawiasów"""
    for i in range(len(lista)):
        if i == len(lista) - 1:
            print(lista[i], end=end)
        else:
            print(lista[i], end=", ")


def nowa_tablica(start: int) -> list[int]:
    """Tworzy tablicę do posortwania i sprawdza, czy wszystkie jej elementy są liczbami całkowitymi"""
    tablica = []
    for i in range(start, len(sys.argv)):
        try:
            numer = int(sys.argv[i])
        except ValueError:
            print(f"{sys.argv[i]} nie jest liczbą całkowitą")
            sys.exit(1)
        else:
            tablica.append(numer)
    return tablica


opcje = ("-a", "-b", "-c", "-d", "-e")

# Sprawdzenie długości ciągu
if len(sys.argv) == 1 or sys.argv[1] == "-h":
    printhelp()
    sys.exit(1)
if sys.argv[1] in opcje:
    if len(sys.argv) < 5:
        print("Podaj conajmniej trzycyfrowy ciąg.")
        sys.exit(1)
    else:
        tablica = nowa_tablica(2)
else:
    if len(sys.argv) < 4:
        print("Podaj conajmniej trzycyfrowy ciąg.")
        sys.exit(1)
    else:
        tablica = nowa_tablica(1)

# Sortowanie ciągu
if sys.argv[1] in opcje:
    if sys.argv[1] == "-a":
        sort_babelkowe(tablica)
    if sys.argv[1] == "-b":
        sort_szybkie(tablica)
    if sys.argv[1] == "-c":
        sort_przez_scalanie(tablica)
    if sys.argv[1] == "-d":
        sort_przez_wybieranie(tablica)
    if sys.argv[1] == "-e":
        sort_przez_wstawianie(tablica)
else:
    sort_babelkowe(tablica)
