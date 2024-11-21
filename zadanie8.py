pada = False
licznik_nie = 0

while not pada:
    odpowiedz = input("Czy pada? (tak/nie/t lub n)")

    if odpowiedz == "nie":
        licznik_nie += 1
    elif odpowiedz == "tak":
        pada = True
    elif odpowiedz == "tak lub n":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Nie rozumiem odpowiedzi. Proszę wpisz 'tak', 'nie' lub 't lub n'.")

print(f"Liczba odpowiedzi 'nie': {licznik_nie}")
