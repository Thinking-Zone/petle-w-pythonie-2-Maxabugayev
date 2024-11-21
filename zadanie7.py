import random

pada = random.choice([True, False])  # Losowanie, czy pada, czy nie
zgaduj = True

while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ").lower()  # Oczekiwanie na odpowiedź użytkownika
    
    if (odpowiedz == 't' and pada) or (odpowiedz == 'n' and not pada):
        print("Brawo! Zgadłeś!")
        zgaduj = False  # Zatrzymujemy pętlę, jeśli odpowiedź jest poprawna
    else:
        print("Niestety, spróbuj ponownie.")
